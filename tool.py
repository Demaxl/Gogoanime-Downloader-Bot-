import time
import os
import threading
import re
import requests
from enum import Enum
from configparser import ConfigParser, NoOptionError, NoSectionError
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from typing import Optional

from selenium_utils import *
from broken import num

# Function to validate video quality (must be 360p, 480p, 720p, or 1080p)


def is_valid_quality(quality: str) -> bool:
    return quality in {'360p', '480p', '720p', '1080p'}


def load_config(file_path: str) -> Optional[ConfigParser]:
    """
    Load the configuration file and return the ConfigParser object
    """
    config = ConfigParser()
    config.read(file_path)

    try:
        username = config.get('AUTHENTICATION', 'username')
        password = config.get('AUTHENTICATION', 'password')
        quality = config.get('SETTINGS', 'quality')
        idm_folder_path = config.get('SETTINGS', 'idm_folder_path')
        download_path = config.get('SETTINGS', 'download_path')

        # if not is_valid_quality(quality):
        #     raise ValueError(f"Invalid quality setting: {quality}")

        return config

    except (NoSectionError, NoOptionError, ValueError) as e:
        print(f"Configuration error: {e}")
        return None


class Settings:
    """
    Enum to store the settings of the bot
    """
    USERNAME: str
    PASSWORD: str
    QUALITY: str
    IDM_FOLDER_PATH: str
    DOWNLOAD_PATH: str

    @classmethod
    def load_from_config(cls, config: ConfigParser) -> None:
        """
        Take the values from the config file and store them in Enum
        """
        cls.USERNAME = config.get('AUTHENTICATION', 'username')
        cls.PASSWORD = config.get('AUTHENTICATION', 'password')
        cls.QUALITY = config.get('SETTINGS', 'quality')
        cls.IDM_FOLDER_PATH = config.get('SETTINGS', 'idm_folder_path')
        cls.DOWNLOAD_PATH = config.get('SETTINGS', 'download_path')


class Bot:
    def __init__(self, start, end) -> None:

        self.start = start
        self.end = end

        self.driver = get_driver()
        self.login()

    def _download_video(self, link):
        """
        Download the video from the link
        """
        folder = r'D:\Videos\download'
        os.chdir(Settings.IDM_FOLDER_PATH)

        command = fr'idman /n /p "{folder}" /d "{link}"'
        os.system(command)

    def login(self):
        """
        Login to the website
        """
        self.driver.get("https://gogoanime3.net/login.html")

        wait(self.driver, By.NAME, "email", time=50).send_keys(
            Settings.USERNAME)
        self.driver.find_element(By.NAME, "password").send_keys(
            Settings.PASSWORD, Keys.ENTER)

        time.sleep(3)

    def download_episodes(self, episodes):
        if not episodes:
            return

        start = 0
        end = len(episodes) - 1

        while start <= end:
            time.sleep(3)
            i = episodes[start]
            # try:
            self.driver.get(f'https://gogoanime3.co/one-piece-episode-{i}')

            try:
                quality = '854x480' if (i % 5) != 0 else '1280x720'
                tag = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                    (By.XPATH, f"//a[contains(text(), '{quality}')]")))
            except TimeoutException:
                try:
                    tag = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                        (By.XPATH, "/html/body/div[2]/div/div/section/section[1]/div[1]/div[2]/div[6]/div/a[1]")))
                except:
                    start += 1
                    continue

            except:
                start += 1
                continue

            link = tag.get_attribute('href')

            r = requests.get(link, allow_redirects=False)

            # Get the redirected URL from the response headers
            redirected_url = r.headers.get('Location')

            # print("Redirected URL:", redirected_url)

            d = threading.Thread(
                target=self._download_video, args=(redirected_url, ))
            d.start()
            start += 1
            # except:
            #     pass

    def run(self):
        animes_path = Settings.DOWNLOAD_PATH

        videos = [num(vid) for vid in os.listdir(
            animes_path) if vid.endswith("mp4")]

        redownload = [eps for eps in range(start, end+1) if eps not in videos]

        print(redownload)

        self.download_episodes(redownload)


if __name__ == "__main__":
    # Load the config.ini file
    config = load_config(os.path.join(".", 'settings.ini'))

    if config:
        Settings.load_from_config(config)

        # start and end are inclusive
        start = 1055
        end = 1070

        bot = Bot(start, end)
        bot.run()

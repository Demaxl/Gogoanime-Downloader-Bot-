import time
import os
import threading
import pickle
import subprocess
from selenium import webdriver
import re
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import undetected_chromedriver as uc
import requests

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from broken import num

# PATH = ChromeDriverManager().install()
PATH = r"C:\Users\maxis\.wdm\drivers\chromedriver\win64\120.0.6099.109\chromedriver-win32/chromedriver.exe"
print(PATH)


def wait(driver, locator, id, time=10):
    element = WebDriverWait(driver, time).until(
        EC.presence_of_element_located((locator, id)))
    return element


def download(link):
    folder = r'D:\Videos\download'
    command = fr'idman /n /p "{folder}" /d "{link}"'
    os.system(command)

    def login(self):
        """
        Login to the website
        """
        self.driver.get("https://gogoanime3.net/login.html")
        time.sleep(5)
        wait(self.driver, By.NAME, "email", time=50).send_keys(
            "username")
        self.driver.find_element(By.NAME, "password").send_keys(
            "password", Keys.ENTER)


os.chdir(r'C:\Program Files (x86)\Internet Download Manager')

time.sleep(3)


def main(numbers):
    if not numbers:
        return

    start = 0
    end = len(numbers) - 1

    while start <= end:
        time.sleep(3)
        i = numbers[start]
        # try:
        driver.get(f'https://gogoanimehd.io/one-piece-episode-{i}')

        try:
            quality = '854x480'  # if (i % 5) != 0 else '1280x720'
            tag = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH, f"//a[contains(text(), '{quality}')]")))
        except TimeoutException:
            try:
                tag = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
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

        d = threading.Thread(target=download, args=(redirected_url, ))
        d.start()
        start += 1
        # except:
        #     pass


def broken():
    animes_path = r"D:\Videos\download"

    videos = [num(vid) for vid in os.listdir(
        animes_path) if vid.endswith("mp4")]

    redownload = [eps for eps in range(start, end+1) if eps not in videos]

    print(redownload)

    main(redownload)


def op():
    episodes = get_episodes()[:20]
    animes_path = r"D:\Videos\download"

    videos = [num(vid) for vid in os.listdir(
        animes_path) if vid.endswith("mp4")]

    redownload = [eps for eps in episodes if eps not in videos]

    print(redownload)

    main(redownload)


def get_episodes():
    def num(vid): return re.match(r"EP (\d+).mp4", vid).group(1)
    path = r"D:\One Piece"

    vids = set([int(num(vid)) for vid in os.listdir(path)])

    all_vids = set(range(1, 200))

    return sorted(list(all_vids - vids))


# start and end are inclusive
start = 1055
end = 1070


# main(list(range(start, end+1)))
broken()
# op()

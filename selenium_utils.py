import time
import pickle
# import undetected_chromedriver as uc

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
# from seleniumbase import Driver
# from seleniumwire import webdriver as WireDriver


def save_cookies(driver, path): return pickle.dump(
    driver.get_cookies(), open(path, 'wb'))


def load_cookies(driver, path):
    cookies = pickle.load(open(path, "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()


def scroll_down(driver):
    # Get current page height
    page_height = driver.execute_script("return document.body.scrollHeight")

    # Define scroll step size
    step_size = 500

    # Scroll down gradually until the end of the page
    for i in range(0, page_height, step_size):
        driver.execute_script("window.scrollTo(0, {});".format(i))
        time.sleep(0.5)  # adjust the sleep time as needed
    # ====


def click(driver, element):
    action = ActionChains(driver)
    action.click(element)
    action.perform()


def wait(driver, locator, id, time=10):
    element = WebDriverWait(driver, time).until(
        EC.presence_of_element_located((locator, id)))
    return element


def waitVisible(driver, locator, id, time=10):
    elements = WebDriverWait(driver, time).until(
        EC.visibility_of_all_elements_located((locator, id)))
    return elements


def get_driver():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    options.set_capability("pageLoadStrategy", "none")

    # options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    # options.add_experimental_option('useAutomationExtension', False)
    # chrome_path = r"C:\Users\maxis\AppData\Local\Google\Chrome\User Data"
    # options.add_argument(f'--user-data-dir={chrome_path}')
    options.add_argument(r'--profile-directory=Default')

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    return driver


# def get_undetected_driver():
#     # PATH = ChromeDriverManager().install()
#     # driver = uc.Chrome(driver_executable_path=PATH)
#     driver = Driver(uc=True)
#     driver.maximize_window()
#     return driver


# def getWireDriver() -> WireDriver.Chrome:
#     PATH = r"C:/Users/maxis/.wdm/drivers/chromedriver/win64/118.0.5993.70/chromedriver-win32/chromedriver.exe"
#     options = Options()
#     options.add_experimental_option('excludeSwitches', ['enable-logging'])
#     driver = WireDriver.Chrome(service=Service(PATH), options=options)

#     driver.maximize_window()
#     return driver

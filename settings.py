import os
from selenium import webdriver

valid_email = 'your email'
valid_password = 'your password'
base_url = 'https://petfriends.skillfactory.ru/'
chrome_location = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
chrome_driver = os.path.join(os.path.dirname(__file__), 'Scripts', 'chromedriver.exe')
default_timeout = 3

if not os.path.exists(chrome_driver):
    chrome_driver = None


def chrome_cfg_options(chrome_options: webdriver.ChromeOptions()):
    chrome_options.binary_location = chrome_location
    # chrome_options.add_extension('/path/to/extension.crx')
    chrome_options.add_argument('no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1400,1000')
    chrome_options.add_argument('--headless')
    chrome_options.headless = True
    return chrome_options
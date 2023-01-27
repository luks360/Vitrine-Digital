import time

from django.test import TestCase
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--window-size=1920x1080")

class MainBaseFunctionalTeste(TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(options=chrome_options)
        return super().setUp()


    def sleep(self, seconds=5):
        time.sleep(seconds)
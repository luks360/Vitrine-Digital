import time

from django.test import TestCase
from selenium import webdriver


class MainBaseFunctionalTeste(TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        return super().setUp()


    def sleep(self, seconds=5):
        time.sleep(seconds)
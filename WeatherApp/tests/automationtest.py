from selenium import webdriver
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import requests
import unittest

#open_chrome = webdriver.Chrome()
#open_chrome.get("http://127.0.0.1:5000/")
#city_string = open_chrome.find_element(By.ID, value='name')
#city_string.send_keys("London")
#city_string.send_keys(Keys.ENTER)
#time.sleep(3)

class UnitTest(unittest.TestCase):
    def test_is_weather_up(self):
        self.assertEqual(requests.get("http://127.0.0.1:5000/").status_code, 200)


#try:
#    if requests.get("http://127.0.0.1:5000/").status_code == 200:
#        print("The website is reachable.")
#except Exception:
#    print("The website is NOT reachable.")
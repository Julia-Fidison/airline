from lib2to3.pgen2 import driver
import os
import pathlib
import unittest

from selenium.webdriver.common.by import By
from selenium import webdriver

# Finds the Uniform Resourse Identifier of a file
def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

# Sets up web driver using Google chrome
driver = webdriver.Chrome('C:/chromedriver_win32/chromedriver.exe')

class WebpageTests(unittest.TestCase):
    def test_title(self):
        driver.get(file_uri("counter.html"))
        self.assertEqual(driver.title, "Counter")
    
    def test_increase(self):
        driver.get(file_uri("counter.html"))
        increase = driver.find_element("id", "increase")
        increase.click()
        self.assertEqual(driver.find_element("tag name", "h1").text, "1")
    
    def test_decrease(self):
        driver.get(file_uri("counter.html"))
        decrease = driver.find_element("id", "decrease")
        decrease.click()
        self.assertEqual(driver.find_element("tag name", "h1").text, "-1")

    def test_multi_increase(self):
        driver.get(file_uri("counter.html"))
        increase = driver.find_element("id", "increase")
        for i in range(3):
            increase.click()
        self.assertEqual(driver.find_element("tag name", "h1").text, "3")

if __name__ == "__main__":
    unittest.main()
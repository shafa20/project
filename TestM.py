import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class SimpleTest(unittest.TestCase):

    def test1_LOGINLogout(self):
        self.driver = webdriver.Chrome(executable_path="D:/chromedriver_win32/chromedriver.exe")
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        userName='Admin'

        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[5]/input').click()
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[3]/input').send_keys(userName)  # password
        self.assertNotEqual(self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[5]/input').text,'LOGIN',"did not matched")

    def test2_OrangeHRM(self):
        self.driver = webdriver.Chrome(executable_path="D:/chromedriver_win32/chromedriver.exe")
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        t_OrangeHRM = self.driver.title
        self.assertEqual("OrangeHRM",t_OrangeHRM,"Values matches")


if __name__ == '__main__':
    unittest.main()







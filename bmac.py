__author__ = 'sr1k4n7h'

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import urllib


class Bmac(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(50)
        self.base_url = "http://www.espncricinfo.com"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_bmac(self):
        driver = self.driver
        driver.get(
            self.base_url + "/ci/content/image/941125.html?object=37737;page=1;dir=next")
        file_count = 0
        for i in range(1025):
            try:
                WebDriverWait(driver, 6).until(lambda driver: driver.find_element_by_id("imgMain"))
                img_url = driver.find_element_by_id("imgMain").get_attribute('src')
                img_name = img_url.split("/")
                print (str(file_count) + ": Downloading '" + str(img_name[-1]) + "' from ..." + str(img_url))
                urllib.urlretrieve(str(img_url), str(img_name[-1]))
                file_count += 1
            except TimeoutException:
                print "Loading took too much time!"

            try:
                driver.find_element_by_css_selector("span.nextBtn.small-2").click()
            except NoSuchElementException:
                print "\t --- " + str(file_count) + " Files has been downloaded ! --- "
                driver.quit()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()

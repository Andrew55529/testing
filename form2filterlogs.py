import time
import unittest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

PASSWORD= '12345'

class unitTest(unittest.TestCase):
    webdriver
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)
        cls.auth(cls)


    def setUp(self) -> None:

        self.join_logs()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def auth(self):
        self.driver.get("https://test.key.help");
        input_username = self.driver.find_element("id", "password")
        login_button = self.driver.find_element("id","auth")
        input_username.send_keys(PASSWORD);
        login_button.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(2000)
        time.sleep(1)

    def join_logs(self):
        driver = self.driver
        driver.get("https://test.key.help");
        driver.find_element(By.CLASS_NAME, "burger").click()
        driver.find_element(By.LINK_TEXT, "ЛОГИ").click()
        self.driver.find_element(By.ID, "filter_open").click()

    def setError(self,text):
        print(self._testMethodName,"failed.",text)
        self.driver.assertTrue(False)

    def test_1_1(self):
        driver = self.driver

        input = driver.find_element(By.ID, "from")
        input.clear();
        btn=self.driver.find_element(By.ID, "filter_apply")
        if btn.get_attribute("style") == "display: none;":
            self.setError("Btn unavailable")
        else:
            print(self._testMethodName, "passed.")

    def test_1_2(self):
        driver = self.driver
        input = driver.find_element(By.ID, "from")
        input.clear();
        input.send_keys("2022.01.01")
        btn = self.driver.find_element(By.ID, "filter_apply")
        if btn.get_attribute("style") == "display: none;":
            print(self._testMethodName, "passed.")
        else:
            self.setError("Btn available")

    def test_1_3(self):
        driver = self.driver
        input = driver.find_element(By.ID, "from")
        input.clear();
        input.send_keys("2022.01.01 12:00:00")
        btn = self.driver.find_element(By.ID, "filter_apply")
        if btn.get_attribute("style") == "display: none;":
            self.setError("Btn unavailable")
        else:
            print(self._testMethodName, "passed.")

    def test_2_1(self):
        driver = self.driver
        input = driver.find_element(By.ID, "to")
        input.clear();
        btn = self.driver.find_element(By.ID, "filter_apply")
        if btn.get_attribute("style") == "display: none;":
            self.setError("Btn unavailable")
        else:
            print(self._testMethodName, "passed.")

    def test_2_2(self):
        driver = self.driver
        input = driver.find_element(By.ID, "to")
        input.clear();
        input.send_keys("2022.01.01")
        btn = self.driver.find_element(By.ID, "filter_apply")
        if btn.get_attribute("style") == "display: none;":
            print(self._testMethodName, "passed.")
        else:
            self.setError("Btn available")


    def test_2_3(self):
        driver = self.driver
        input = driver.find_element(By.ID, "to")
        input.clear();
        input.send_keys("2022.01.01 12:00:00")
        btn = self.driver.find_element(By.ID, "filter_apply")
        if btn.get_attribute("style") == "display: none;":
            self.setError("Btn unavailable")
        else:
            print(self._testMethodName, "passed.")



if __name__ == '__main__':
    unittest.main()


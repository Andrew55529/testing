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

        self.join_user()

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

    def join_user(self):
        driver = self.driver
        driver.get("https://test.key.help");
        driver.find_element(By.CLASS_NAME, "burger").click()
        driver.find_element(By.LINK_TEXT, "ПОЛЬЗОВАТЕЛИ").click()

    def setError(self,text):
        print(self._testMethodName,"failed.",text)
        self.driver.assertTrue(False)


    def openUser(self,name):

        try:
            self.driver.implicitly_wait(1)
            self.driver.find_element(By.LINK_TEXT, name).click()
        except Exception as e:
            self.setError("No user")

    def checkPopup(self):
        try:
            popup = self.driver.find_element(By.ID, "userpopup")
            return True;
        except Exception as e:
            return False;




    def test_1_1(self):
        driver = self.driver
        self.openUser("123")
        try:
            popup = driver.find_element(By.ID, "userpopup")
        except Exception as e:
            self.setError("No popup")

        input = driver.find_element(By.ID, "from")
        input.clear();
        self.driver.find_element("id", "userpopup_btn-ok").click()

        if popup.get_attribute("style")=="display: none;":
            self.setError("Windows closed")

        print(self._testMethodName, "passed.")

    def test_1_2(self):
        driver = self.driver
        self.openUser("123")
        try:
            popup = driver.find_element(By.ID, "userpopup")
        except Exception as e:
            self.setError("No popup")

        input = driver.find_element(By.ID, "from")
        input.clear();
        input.send_keys("2022-07-27")
        self.driver.find_element("id", "userpopup_btn-ok").click()

        if popup.get_attribute("style")=="display: none;":
            self.setError("Windows closed")

        print(self._testMethodName, "passed.")

    def test_1_3(self):
        driver = self.driver
        self.openUser("123")
        try:
            popup = driver.find_element(By.ID, "userpopup")
        except Exception as e:
            self.setError("No popup")

        input = driver.find_element(By.ID, "from")
        input.clear();
        input.send_keys("2022-07-27 22:00:00")
        self.driver.find_element("id", "userpopup_btn-ok").click()

        if popup.get_attribute("style")=="display: none;":
            print(self._testMethodName, "passed.")
        else:
            self.setError("Windows closed")

    def test_2_1(self):
        driver = self.driver
        self.openUser("123")
        try:
            popup = driver.find_element(By.ID, "userpopup")
        except Exception as e:
            self.setError("No popup")

        input = driver.find_element(By.ID, "to")
        input.clear();
        self.driver.find_element("id", "userpopup_btn-ok").click()

        if popup.get_attribute("style")=="display: none;":
            self.setError("Windows closed")

        print(self._testMethodName, "passed.")

    def test_2_2(self):
        driver = self.driver
        self.openUser("123")
        try:
            popup = driver.find_element(By.ID, "userpopup")
        except Exception as e:
            self.setError("No popup")

        input = driver.find_element(By.ID, "to")
        input.clear();
        input.send_keys("2022-07-27")
        self.driver.find_element("id", "userpopup_btn-ok").click()

        if popup.get_attribute("style")=="display: none;":
            self.setError("Windows closed")

        print(self._testMethodName, "passed.")

    def test_2_3(self):
        driver = self.driver
        self.openUser("123")
        try:
            popup = driver.find_element(By.ID, "userpopup")
        except Exception as e:
            self.setError("No popup")

        input = driver.find_element(By.ID, "to")
        input.clear();
        input.send_keys("2022-07-27 22:00:00")
        self.driver.find_element("id", "userpopup_btn-ok").click()

        if popup.get_attribute("style")=="display: none;":
            print(self._testMethodName, "passed.")
        else:
            self.setError("Windows closed")

    def test_3_1(self):
        driver = self.driver
        self.openUser("123")
        try:
            popup = driver.find_element(By.ID, "userpopup")
        except Exception as e:
            self.setError("No popup")

        input = driver.find_element(By.ID, "info")
        input.clear();
        self.driver.find_element("id", "userpopup_btn-ok").click()

        if popup.get_attribute("style")=="display: none;":
            print(self._testMethodName, "passed.")
        else:
            self.setError("Windows closed")

    def test_3_2(self):
        driver = self.driver
        self.openUser("123")
        try:
            popup = driver.find_element(By.ID, "userpopup")
        except Exception as e:
            self.setError("No popup")

        input = driver.find_element(By.ID, "info")
        input.clear()
        input.send_keys(" ")
        self.driver.find_element("id", "userpopup_btn-ok").click()

        if popup.get_attribute("style")=="display: none;":
            print(self._testMethodName, "passed.")
        else:
            self.setError("Windows closed")

    def test_3_3(self):
        driver = self.driver
        self.openUser("123")
        try:
            popup = driver.find_element(By.ID, "userpopup")
        except Exception as e:
            self.setError("No popup")

        input = driver.find_element(By.ID, "info")
        input.clear()
        input.send_keys("!")
        self.driver.find_element("id", "userpopup_btn-ok").click()

        if popup.get_attribute("style") == "display: none;":
            print(self._testMethodName, "passed.")
        else:
            self.setError("Windows closed")
    def test_3_4(self):
        driver = self.driver
        self.openUser("123")
        try:
            popup = driver.find_element(By.ID, "userpopup")
        except Exception as e:
            self.setError("No popup")

        input = driver.find_element(By.ID, "info")
        input.clear()
        input.send_keys("Book")
        self.driver.find_element("id", "userpopup_btn-ok").click()

        if popup.get_attribute("style")=="display: none;":
            print(self._testMethodName, "passed.")
        else:
            self.setError("Windows closed")
    def test_4_1(self):
        driver = self.driver
        self.openUser("123")
        try:
            popup = driver.find_element(By.ID, "userpopup")
        except Exception as e:
            self.setError("No popup")

        input = driver.find_element(By.ID, "password")
        input.clear()
        self.driver.find_element("id", "userpopup_btn-ok").click()

        if popup.get_attribute("style")=="display: none;":
            print(self._testMethodName, "passed.")
        else:
            self.setError("Windows closed")
    def test_4_2(self):
        driver = self.driver
        self.openUser("123")
        try:
            popup = driver.find_element(By.ID, "userpopup")
        except Exception as e:
            self.setError("No popup")

        input = driver.find_element(By.ID, "password")
        input.clear()
        input.send_keys(" ")
        self.driver.find_element("id", "userpopup_btn-ok").click()

        if popup.get_attribute("style")=="display: none;":
            self.setError("Windows closed")
        else:
            print(self._testMethodName, "passed.")
    def test_4_3(self):
        driver = self.driver
        self.openUser("123")
        try:
            popup = driver.find_element(By.ID, "userpopup")
        except Exception as e:
            self.setError("No popup")

        input = driver.find_element(By.ID, "password")
        input.clear()
        input.send_keys("!")
        self.driver.find_element("id", "userpopup_btn-ok").click()

        if popup.get_attribute("style")=="display: none;":
            self.setError("Windows closed")
        else:
            print(self._testMethodName, "passed.")

    def test_4_4(self):
        driver = self.driver
        self.openUser("123")
        try:
            popup = driver.find_element(By.ID, "userpopup")
        except Exception as e:
            self.setError("No popup")

        input = driver.find_element(By.ID, "password")
        input.clear()
        input.send_keys("Book")
        self.driver.find_element("id", "userpopup_btn-ok").click()

        if popup.get_attribute("style")=="display: none;":
            print(self._testMethodName, "passed.")
        else:
            self.setError("Windows closed")

    def test_4_5(self):
        driver = self.driver
        self.openUser("123")
        try:
            popup = driver.find_element(By.ID, "userpopup")
        except Exception as e:
            self.setError("No popup")

        input = driver.find_element(By.ID, "password")
        input.clear()
        input.send_keys("!№ЙЦУфыв123")
        self.driver.find_element("id", "userpopup_btn-ok").click()

        if popup.get_attribute("style")=="display: none;":
            print(self._testMethodName, "passed.")
        else:
            self.setError("Windows closed")

    def test_5_1(self):
        driver = self.driver
        # Проверка наличия пользователя
        self.openUser("123")

        # Проверка Наличия всплывающего окна
        try:
            popup = driver.find_element(By.ID, "userpopup")
        except Exception as e:
            self.setError("No popup")

        # Ввод данных
        input = self.driver.find_element("id", "fio")
        input.clear();
        self.driver.find_element("id", "userpopup_btn-ok").click()
        if popup.get_attribute("style")=="display: none;":
            self.setError("Windows closed")
        else:
            print(self._testMethodName, "passed.")

    def test_5_2(self):
        driver = self.driver
        # Проверка наличия пользователя
        self.openUser("123")

        # Проверка Наличия всплывающего окна
        try:
            popup = driver.find_element(By.ID, "userpopup")
        except Exception as e:
            self.setError("No popup")

        # Ввод данных
        input = self.driver.find_element("id", "fio")
        input.clear();
        input.send_keys(" ")

        self.driver.find_element("id", "userpopup_btn-ok").click()
        if popup.get_attribute("style")=="display: none;":
            self.setError("Windows closed")

        else:
            print(self._testMethodName, "passed.")

    def test_5_3(self):
        driver = self.driver
        # Проверка наличия пользователя
        self.openUser("123")

        # Проверка Наличия всплывающего окна
        try:
            popup = driver.find_element(By.ID, "userpopup")
        except Exception as e:
            self.setError("No popup")

        # Ввод данных
        input = self.driver.find_element("id", "fio")
        input.clear();
        input.send_keys("Book")

        self.driver.find_element("id", "userpopup_btn-ok").click()
        if popup.get_attribute("style") == "display: none;":
            print(self._testMethodName, "passed.")
        else:
            self.setError("Windows closed")




if __name__ == '__main__':
    unittest.main()


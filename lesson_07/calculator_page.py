from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get(
         "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.driver.maximize_window()

    def close_driver(self):
        self.driver.quit()

    def delay(self, delay):
        seconds = self.driver.find_element(By.ID, "delay")
        seconds.clear()
        seconds.send_keys(delay)

    def click_button(self, button):
        xpath = f"//span[text()='{button}']"
        self.driver.find_element(By.XPATH, xpath).click()

    def result(self, result):
        self.wait = WebDriverWait(self.driver, 60)
        self.wait.until(EC.text_to_be_present_in_element((
            By.CLASS_NAME, "screen"), result))
        get_result = self.driver.find_element(By.CLASS_NAME, "screen").text
        return get_result

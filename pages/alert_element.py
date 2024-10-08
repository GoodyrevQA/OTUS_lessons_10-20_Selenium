from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class AlertSuccessElement(BasePage):
    SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert-success")
    CLOSE_SUCCESS = (By.CSS_SELECTOR, ".btn-close")

    @allure.step("Close alert")
    def close_alert(self):
        return self.click(self.CLOSE_SUCCESS)

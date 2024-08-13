from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RegisterPage(BasePage):
    FIRST_NAME = (By.CSS_SELECTOR, "#input-firstname")
    LAST_NAME = (By.CSS_SELECTOR, "#input-lastname")
    PASSWORD = (By.CSS_SELECTOR, "#input-password")
    EMAIL = (By.CSS_SELECTOR, "#input-email")
    AGREE_BUTTON = (By.CSS_SELECTOR, "[name=agree]")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "[type=submit]")
    SUCCESS_REGISTRATION_MESSAGE = (
        By.XPATH,
        "//*[@id='content']/h1[text()='Your Account Has Been Created!']",
    )

    def open(self):
        self.browser.get(self.browser.url + "/index.php?route=account/register")

    def fill_first_name(self, value: str):
        self.input_value(self.FIRST_NAME, value)

    def fill_last_name(self, value: str):
        self.input_value(self.LAST_NAME, value)

    def fill_password(self, value: str):
        self.input_value(self.PASSWORD, value)

    def fill_email(self, value: str):
        self.input_value(self.EMAIL, value)

    def click_agree_privacy_policy_button(self):
        self.click(self.AGREE_BUTTON)

    def click_continue_button(self):
        self.click(self.CONTINUE_BUTTON)

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class ShoppingCartPage(BasePage):
    FIRST_PRODUCT_NAME = (By.CSS_SELECTOR, ".text-start a")

    @allure.step("Get name of first product")
    def get_first_product_name(self):
        return self.get_elements(self.FIRST_PRODUCT_NAME)[0].text

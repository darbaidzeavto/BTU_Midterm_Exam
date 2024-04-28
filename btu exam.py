from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.men_category_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Men"))
        )

    def click_men_category(self):
        self.men_category_link.click()

class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.add_to_cart_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "product-addtocart-button"))
        )

    def click_add_to_cart(self):
        self.add_to_cart_button.click()

    def get_error_message(self):
        error_element = WebDriverWait(self, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "message-error"))
        )
        return error_element.text


driver = webdriver.Chrome()


main_page = MainPage(driver)
product_page = None


driver.get("https://magento.softwaretestingboard.com/")

main_page.click_men_category()


product_page = ProductPage(driver) 

product_page.click_add_to_cart()

error_message = product_page.get_error_message()
assert error_message != "", "Expected error message but none found"


driver.quit()

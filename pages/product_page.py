from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket_btn.click()

    def should_be_message_about_adding_product_to_basket(self):
        added_product_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert added_product_name == product_name, f"Product name in the message after adding the " \
                                                   f"product to the basket {added_product_name} is not " \
                                                   f"equal actual product name {product_name}"

    def should_be_correct_basket_counter(self):
        added_product_price = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_PRICE).text
        print(added_product_price)
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        print(product_price)
        assert added_product_price == product_price, f"Product price in the message after adding the " \
                                                     f"product to the basket {added_product_price} is not " \
                                                     f"equal actual product price {product_price}"

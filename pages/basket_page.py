from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        # basket items container (sections with items) will appear only if we add
        # at least one item. So check is that this section is not present
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS_CONTAINER), \
            "There is at least one item in the basket"

    def should_be_message_about_empty_basket(self):
        # checking message about empty basket only for 1 locale that used in our tests
        basket_empty_message = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE).text
        basket_empty_message_text = "Your basket is empty. Continue shopping"
        assert basket_empty_message == basket_empty_message_text, f"message in basket page is {basket_empty_message} " \
                                                                  f"instead of {basket_empty_message_text}"


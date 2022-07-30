from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        # just enter needed email and password to register form
        reg_email_input = self.browser.find_element(*LoginPageLocators.REG_EMAIL_INPUT)
        reg_email_input.send_keys(email)
        reg_password_input = self.browser.find_element(*LoginPageLocators.REG_PASSWORD_INPUT)
        reg_password_input.send_keys(password)
        reg_password_input_2 = self.browser.find_element(*LoginPageLocators.REG_PASSWORD_INPUT_2)
        reg_password_input_2.send_keys(password)
        reg_button = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        reg_button.click()

    def should_be_login_page(self):
        # this complex check contains 3 small checks
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # validate if we have login in url on login page
        current_url = self.browser.current_url
        login_string = "login"
        assert str(current_url).find(login_string) >= 0, \
            f"Login page URL '{current_url}' does not contain '{login_string}' "

    def should_be_login_form(self):
        # in this check I found all needed elements for login form and validate
        # that all of them are present on the page
        is_login_button_present = self.is_element_present(*LoginPageLocators.LOGIN_BUTTON)
        is_login_password_present = self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD_INPUT)
        is_login_email_present = self.is_element_present(*LoginPageLocators.LOGIN_EMAIL_INPUT)
        assert is_login_button_present and is_login_password_present and is_login_email_present, \
            "Login form is not fully displayed on the page"

    def should_be_register_form(self):
        # in this check I found all needed elements for register form and validate
        # that all of them are present on the page
        is_reg_button_present = self.is_element_present(*LoginPageLocators.REG_BUTTON)
        is_reg_password1_present = self.is_element_present(*LoginPageLocators.REG_PASSWORD_INPUT)
        is_reg_password2_present = self.is_element_present(*LoginPageLocators.REG_PASSWORD_INPUT_2)
        is_reg_email_present = self.is_element_present(*LoginPageLocators.REG_EMAIL_INPUT)
        assert is_reg_button_present and is_reg_password1_present and is_reg_password2_present \
               and is_reg_email_present, "Registration form is not fully displayed on the page"

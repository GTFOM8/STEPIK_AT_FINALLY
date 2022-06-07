from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "URL is not correct"

    def should_be_login_form(self):
        login_link = self.browser.find_element(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
       # login_link.click()
        assert True

    def should_be_register_form(self):
        register_link = self.browser.find_element(*LoginPageLocators.REGISTER_FORM), \
                     "Register form is not presented"
        #register_link.click()
        assert True

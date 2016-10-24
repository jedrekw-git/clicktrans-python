# coding=utf-8
import datetime
from pages.base import BasePage
from selenium.webdriver.common.by import By
from time import sleep
from utils.utils import *



class ProviderPage(BasePage):
    _title = "Provider page"
    _ask_for_offer_button = (By.LINK_TEXT, "Poproś o ofertę")
    _first_aucton_checkbox = (By.XPATH, "//tr[3]/td/input")
    _close_cookies_bar = (By.ID, "cookiesBarClose")
    _ask_for_offer_submit_button = (By.XPATH, "//input[@value='Poproś o ofertę']")

    def ask_for_offer_on_provider_page(self):
        # self.click(self._close_cookies_bar)
        self.click(self._ask_for_offer_button)
        self.check(self._first_aucton_checkbox)
        self.click(self._ask_for_offer_submit_button)


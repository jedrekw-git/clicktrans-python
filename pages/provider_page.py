# coding=utf-8
import datetime
from pages.base import BasePage
from selenium.webdriver.common.by import By
from time import sleep
from utils.utils import *



class ProviderPage(BasePage):
    _title = "Provider page"
    _ask_for_offer_button = (By.PARTIAL_LINK_TEXT, u"Poproś o ofertę")
    _first_aucton_checkbox = (By.XPATH, "//input[@name='offer_request[auctionIds][]']")
    _ask_for_offer_submit_button = (By.ID, "offer_request_submit")

    def ask_for_offer_on_provider_page(self):
        self.click(self._ask_for_offer_button, "The Ask for offer on provider page button didn't appear")
        self.condition_click(self._first_aucton_checkbox, "The attempt to click the first auction on ask for offer on provider page list was unsuccessful")
        self.click(self._ask_for_offer_submit_button, "The Ask for offer submit button on provider page wasn't visible")
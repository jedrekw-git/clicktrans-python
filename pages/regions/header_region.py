# coding=utf-8
from pages.page import Page
from pages.searchcriyrtia import SearchCriteriaPage
from selenium.webdriver.common.by import By




class HeaderRegion(Page):
    _login_field = (By.ID, "_username")
    _base_url = "https://www.gsmarena.com/"

    def search_criteria_page(self):
        self.get(self._base_url + "search.php3?")
        return SearchCriteriaPage(self.get_driver())

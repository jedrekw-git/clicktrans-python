# coding=utf-8
from pages.base import BasePage


class HomePage(BasePage):
    _title = "homepage"
    _url_https = "https://www.gsmarena.com/search.php3?"
    _url = "https://www.gsmarena.com/search.php3?"

    def __init__(self, driver):
        super(HomePage, self).__init__(driver, self._title, self._url)

    def open_home_page(self):
        self.get(self._url_https)

        HomePage._base_url = self._url_https
        return self

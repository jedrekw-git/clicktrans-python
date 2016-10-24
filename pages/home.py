# coding=utf-8
from pages.base import BasePage


class HomePage(BasePage):
    _title = "Transport i przeprowadzki | Gie\u0142da Transportowa - Clicktrans.pl"
    _url = "http://clicktrans_dev:czx1mcc713d@dev.clicktrans.pl/"
    _url2 = "http://clicktrans_dev:czx1mcc713d@dev.clicktrans.pl/app_dev.php/"

    def __init__(self, driver):
        super(HomePage, self).__init__(driver, self._title, self._url)

    def open_home_page(self):
        self.get(self._url)
        self.is_the_current_page()
        # alert = self.get_driver().switch_to_alert()
        # alert.send_keys(login)
        # self.send_keys(Keys.TAB)
        # self.send_keys(password)
        # self.accept_alert()
        return self
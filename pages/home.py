# coding=utf-8
from pages.base import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):
    _title = "Transport i przeprowadzki | Gie\u0142da Transportowa - Clicktrans.pl"
    _url = "http://clicktrans_dev:czx1mcc713d@dev.clicktrans.pl/"
    _url_https = "https://clicktrans_dev:czx1mcc713d@dev.clicktrans.pl/"
    _url2 = "http://clicktrans_dev:czx1mcc713d@dev.clicktrans.pl/app_dev.php/"
    _url_test = "https://clicktrans_dev:czx1mcc713d@www.dev.clicktrans.pl/"

    def __init__(self, driver):
        super(HomePage, self).__init__(driver, self._title, self._url)

    def open_home_page(self):
        self.get(self._url_https)
        # self.get(self._url)
        # self.get_driver().Navigate().GoToUrl(self._url_https)
        # alert = WebDriverWait(self.get_driver(), 10).until(EC.alert_is_present())
        # alert.authenticateUsing()
        # self.is_the_current_page()
        # alert = self.get_driver().switch_to_alert()
        # alert.accept()
        # alert.send_keys(login)
        # self.send_keys(Keys.TAB)
        # self.send_keys(password)
        # self.accept_alert()
        return self
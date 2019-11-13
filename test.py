# coding=utf-8
import unittest
from htmltestrunner import HTMLTestRunner
from selenium import webdriver
from unittestzero import Assert
from pages.home import HomePage
from utils.config import *
import os
from datetime import datetime
from time import sleep
from change_password import *
from time import gmtime, strftime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException

SCREEN_DUMP_LOCATION = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'screendumps'
)

run_locally = True
#@on_platforms(browsers)

class SmokeTest(unittest.TestCase):

    def test_add_new_consignment_not_logged_in_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        search_crityeria_page = home_page.header.search_criteria_page()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(search_crityeria_page._phone_finder_header, u"Phone finder"), u"Było chujowo")

    def test_fill_search_crityeria_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        search_crityeria_page = home_page.header.search_criteria_page()
        search_crityeria_page.chose_random_brand()
        search_crityeria_page.move_slider_year()

    # def test_zz_generate_plot_and_send_email(self):
    #     self._save_plot()
    #     self._convert_to_html()
    #     self._send_email()

    def tally(self):
        return len(self._resultForDoCleanups.errors) + len(self._resultForDoCleanups.failures)

    def setUp(self):
        self.timeout = 30
        if run_locally:
            # os.environ["webdriver.gecko.driver"] = "C:/BACKUP 2017-01/gecko/geckodriver.exe"
            # firefox_capabilities = DesiredCapabilities.FIREFOX
            # firefox_capabilities['binary'] = 'C:/Program Files (x86)/Mozilla Firefox'
            # fp = webdriver.FirefoxProfile("C:/Users/jj/AppData/Roaming/Mozilla/Firefox/Profiles/woebxsbi.default-1458919598960")
            # geckoPath = 'C:\BACKUP 2017-01\gecko\geckodriver.exe'
            # self.driver = webdriver.Firefox(capabilities=firefox_capabilities, firefox_profile=fp)
            sr_args = ["--verbose", "--log-path=chromedriver.log"]
            self.driver = webdriver.Chrome(executable_path='C:\Downloads\chromedriver.exe',  service_args=sr_args)
            # self.driver = webdriver.Firefox()
            # self.driver.set_window_size(1024,768)
            self.driver.maximize_window()
            self.driver.implicitly_wait(self.timeout)
            self.errors_and_failures = self.tally()
        else:
            self.desired_capabilities['name'] = self.id()
            sauce_url = "http://%s:%s@ondemand.saucelabs.com:80/wd/hub"

            self.driver = webdriver.Remote(
                desired_capabilities=self.desired_capabilities,
                command_executor=sauce_url % (USERNAME, ACCESS_KEY)
            )

            self.driver.implicitly_wait(self.timeout)

    def tearDown(self):
        if run_locally:
                if self.tally() > self.errors_and_failures:
                    if not os.path.exists(SCREEN_DUMP_LOCATION):
                        os.makedirs(SCREEN_DUMP_LOCATION)
                    for ix, handle in enumerate(self.driver.window_handles):
                        self._windowid = ix
                        self.driver.switch_to.window(handle)
                        # self.take_screenshot()
                        # self.dump_html()
                self.driver.quit()

#     def _get_filename(self):
#         timestamp = datetime.now().isoformat().replace(':', '.')[:19]
#         self._saved_filename = "{classname}.{method}-window{windowid}-{timestamp}".format(
#             classname=self.__class__.__name__,
#             method=self._testMethodName,
#             windowid=self._windowid,
#             timestamp=timestamp
#         )
#         return "{folder}/{classname}.{method}-window{windowid}-{timestamp}".format(
#             folder=SCREEN_DUMP_LOCATION,
#             classname=self.__class__.__name__,
#             method=self._testMethodName,
#             windowid=self._windowid,
#             timestamp=timestamp
#         )
#
#     def _get_filename_for_plot(self):
#         timestamp = datetime.now().isoformat().replace(':', '.')[:19]
#         self._saved_filename_plot = "{classname}.plot-{timestamp}".format(
#             classname=self.__class__.__name__,
#             timestamp=timestamp
#         )
#         return "{folder}/{classname}.plot-{timestamp}".format(
#             folder=SCREEN_DUMP_LOCATION,
#             classname=self.__class__.__name__,
#             timestamp=timestamp
#             )
#
#     def _save_plot(self):
#         import matplotlib.pyplot as plt
#         filename = self._get_filename_for_plot() + ".png"
#         err = len(self._resultForDoCleanups.errors)
#         fail = len(self._resultForDoCleanups.failures)
#
#         # The slices will be ordered and plotted counter-clockwise.
#         labels = 'Errors', 'Failures', 'Passes'
#         sizes = [err, fail, 61-fail-err]
#         colors = ['red', 'gold', 'green']
#         explode = (0.1, 0.1, 0.1)
#
#         plt.pie(sizes, explode=explode, labels=labels, colors=colors,
#                 autopct='%1.1f%%', shadow=True, startangle=90)
#         plt.axis('equal')
#         print "\n WYKRES:\n", filename
#         plt.savefig(filename)
#         text_file = open("ClicktransRaportScreeny.txt", "a")
#         text_file.write("<br><br>Wykres statystyczny: <a href=""http://ci.testuj.pl/job/Clicktrans/ws/screendumps/"+self._saved_filename_plot+".png>Wykres</a>")
#         text_file.close()
#
#     def take_screenshot(self):
#         filename = self._get_filename() + ".png"
#         print "\n{method} SCREENSHOT AND HTML:\n".format(
#             method=self._testMethodName)
#         print 'screenshot:', filename
#         self.driver.get_screenshot_as_file(filename)
#         text_file = open("ClicktransRaportScreeny.txt", "a")
#         text_file.write("<br><br>{method} SCREENSHOT AND HTML:<br>".format(
#             method=self._testMethodName)+"<br>Screenshot: <a href=""http://ci.testuj.pl/job/Clicktrans/ws/screendumps/"+self._saved_filename+".png>"+self._saved_filename+"</a>")
#         text_file.close()
#
#     def dump_html(self):
#         filename = self._get_filename() + '.html'
#         print 'page HTML:', filename
#         with open(filename, 'w') as f:
#             f.write(self.driver.page_source.encode('utf-8'))
#         text_file = open("ClicktransRaportScreeny.txt", "a")
#         text_file.write("<br>Html: <a href=""http://ci.testuj.pl/job/Clicktrans/ws/screendumps/"+self._saved_filename+".html>"+self._saved_filename+"</a>")
#         text_file.close()
#
    # def _send_email(self):
    #     from mailer import Mailer
    #     from mailer import Message
    #
    #     message = Message(From="jedrzej.wojcieszczyk@testuj.pl",
    #                       To=["sergii.demianchuk@clicktrans.pl", "michal.brzezinski@clicktrans.pl"])
    #     message.Subject = "RAPORT CLICKTRANS TESTY AUTOMATYCZNE JENKINS"
    #     message.Html = """<p>Cześć!<br>
    #        Oto wygenerowany automatycznie raport z testów Clicktrans.pl<br>
    #        Plik zawierający Screenshoty i kod html testów które nie przeszły oraz wykres statystyczny: <a href="http://ci.testuj.pl/job/Clicktrans/ws/ClicktransRaportScreeny.html">Screenshoty, HTML i wykres</a><br>
    #        Tabela raportowa z logami wykonanych testów: <a href="http://ci.testuj.pl/job/Clicktrans/ws/ClicktransReportLogi.html">Tabela z logami</a></p>"""
    #
    #     sender = Mailer('smtp.gmail.com', use_tls=True, usr='maildoklientow@gmail.com', pwd='useme1988')
    #     sender.send(message)
#
#     def _convert_to_html(self):
#         html_file = open("ClicktransRaportScreeny.html", "a")
#         html_file.write("<!DOCTYPE html><html><head><title>Clicktrans Report</title></head><body>")
#         f = open('ClicktransRaportScreeny.txt')
#         for line in f.readlines():
#             html_file.write(line)
#         f.close()
#         html_file.write("</body></html>")
#         html_file.close()
#
# open("ClicktransRaportScreeny.txt", 'w').close()
# open("ClicktransRaportScreeny.html", 'w').close()
# suite = unittest.TestLoader().loadTestsFromTestCase(SmokeTest)
# outfile = open("ClicktransReportLogi.html", "wb")
# runner = HTMLTestRunner(stream=outfile, title='Test Report', description='Clicktrans', verbosity=2)
# runner.run(suite)

if __name__ == '__main__':
     unittest.main()

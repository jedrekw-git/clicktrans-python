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
from time import gmtime, strftime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from change_password import *
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

SCREEN_DUMP_LOCATION = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'screendumps'
)

run_locally = True
#@on_platforms(browsers)

class SmokeTest(unittest.TestCase):

    def test_add_new_consignment_not_logged_in_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        Assert.contains(u"Jeszcze tylko chwila...", add_consignment_page.get_page_source(), u"The text <Jeszcze tylko chwila> didn't appear on confirmation page after entering congigment details consignment, probably the consignment details were wrongly entered")
        Assert.contains(u"Twoje ogłoszenie o przesyłce  zostało zapisane, ale musisz się zalogować, aby było widoczne dla Przewoźników.", add_consignment_page.get_page_source(), u"The text <Twoje ogłoszenie o przesyłce  zostało zapisane, ale musisz się zalogować, aby było widoczne dla Przewoźników> didn't appear on confirmation page after adding consignment, probably the consignment details were wrongly entered")
        Assert.contains(u"Nie masz konta? <b>Zarejestruj si\u0119 w 1 minut\u0119 (za darmo).</b> Twoje dane s\u0105 chronione i nie b\u0119d\u0105 upublicznione.", add_consignment_page.get_page_source(), u"The text <Nie masz konta? <b>Zarejestruj si\u0119 w 1 minut\u0119 (za darmo).</b> Twoje dane s\u0105 chronione i nie b\u0119d\u0105 upublicznione.> didn't appear on confirmation page after adding consignment, probably the consignment details were wrongly entered")
        home_page.header.login_after_adding_consignment(USER, PASSWORD)

        Assert.contains(u"Twoja przesyłka", add_consignment_page.get_page_source(), u"The text <Twoja przesyłka> didn't appear on confirmation page after adding consignment and logging")
        Assert.contains(add_consignment_page._title_uuid, add_consignment_page.get_page_source(), u"The consignment title didn't appear on confirmation page after adding consignment and logging")
        Assert.contains(u"została wystawiona!", add_consignment_page.get_page_source(), u"The text <została wystawiona!> didn't appear on confirmation page after adding consignment and logging")

    def test_add_new_consignment_not_activated_user_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        registeration_page = home_page.header.continue_to_registration_page()
        registeration_page.add_new_consignment_unactivated_fill_username_field()
        registeration_page.add_new_consignment_unactivated_fill_email_field()
        registeration_page.new_user_fill_data()

        Assert.contains(u"Odbierz pocztę", registeration_page.get_page_source(), u"The text <Odbierz pocztę> wasn't found on confirmastion page after entering new user data")
        Assert.contains(registeration_page._email_user_add_new_consignment, registeration_page.get_page_source(), u"The user email wasn't found on confirmastion page after entering new user data")
        Assert.contains(u'i kliknij link aktywacyjny, aby ukończyć rejestrację.', registeration_page.get_page_source(), u"The text <i kliknij link aktywacyjny, aby ukończyć rejestrację> wasn't found on confirmastion page after entering new user data")

    def test_zz_generate_plot_and_send_email(self):
        self._save_plot()
        # self._convert_to_html()
        self._send_email()

    def tally(self):
        return len(self._resultForDoCleanups.errors) + len(self._resultForDoCleanups.failures)

    def setUp(self):
        self.timeout = 30
        if run_locally:
            # fp = webdriver.FirefoxProfile()
            # fp.set_preference("browser.startup.homepage", "about:blank")
            # fp.set_preference("startup.homepage_welcome_url", "about:blank")
            # fp.set_preference("startup.homepage_welcome_url.additional", "about:blank")
            # fp.set_preference(" xpinstall.signatures.required", "false")
            # fp.set_preference("toolkit.telemetry.reportingpolicy.firstRun", "false")
            # binary = FirefoxBinary('/__stare/firefox45/firefox')
            # self.driver = webdriver.Firefox(firefox_binary=binary, firefox_profile=fp)
            sr_args = ["--verbose", "--log-path=chromedriver.log"]
            from selenium.webdriver.chrome.options import Options
            opts = Options()
            opts.binary_location = "/usr/bin/google-chrome"
            # opts.binary_location = "/usr/lib/chromium-browser/chromium-browser"
            opts.add_argument("--no-sandbox") #This make Chromium reachable
            opts.add_argument("--no-default-browser-check") #Overrides default choices
            opts.add_argument("--no-first-run")
            opts.add_argument("--disable-default-apps")
            self.driver = webdriver.Chrome(executable_path="/usr/lib/chromium-browser/chromedriver", service_args=sr_args, chrome_options=opts)
            # self.driver = webdriver.Chrome(service_args=sr_args, chrome_options=opts)
            self.driver.set_window_size(1024,768)
            # self.driver.implicitly_wait(self.timeout)
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
                        self.take_screenshot()
                        self.dump_html()
                self.driver.quit()

    def _get_filename(self):
        timestamp = datetime.now().isoformat().replace(':', '.')[:19]
        self._saved_filename = "{classname}.{method}-window{windowid}-{timestamp}".format(
            classname=self.__class__.__name__,
            method=self._testMethodName,
            windowid=self._windowid,
            timestamp=timestamp
        )
        return "{folder}/{classname}.{method}-window{windowid}-{timestamp}".format(
            folder=SCREEN_DUMP_LOCATION,
            classname=self.__class__.__name__,
            method=self._testMethodName,
            windowid=self._windowid,
            timestamp=timestamp
        )

    def _get_filename_for_plot(self):
        timestamp = datetime.now().isoformat().replace(':', '.')[:19]
        self._saved_filename_plot = "{classname}.plot-{timestamp}".format(
            classname=self.__class__.__name__,
            timestamp=timestamp
        )
        return "{folder}/{classname}.plot-{timestamp}".format(
            folder=SCREEN_DUMP_LOCATION,
            classname=self.__class__.__name__,
            timestamp=timestamp
            )

    def _save_plot(self):
        import matplotlib.pyplot as plt
        filename = self._get_filename_for_plot() + ".png"
        err = len(self._resultForDoCleanups.errors)
        fail = len(self._resultForDoCleanups.failures)

        # The slices will be ordered and plotted counter-clockwise.
        labels = 'Errors', 'Failures', 'Passes'
        sizes = [err, fail, 61-fail-err]
        colors = ['red', 'gold', 'green']
        explode = (0.1, 0.1, 0.1)

        plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=90)
        plt.axis('equal')
        print "\n WYKRES:\n", filename
        plt.savefig(filename)
        text_file = open("Clicktrans3RaportScreeny.txt", "a")
        text_file.write("<br><br>Wykres statystyczny: <a href=""http://ci.testuj.pl/job/Clicktrans3/ws/screendumps/"+self._saved_filename_plot+".png>Wykres</a>")
        text_file.close()

    def take_screenshot(self):
        filename = self._get_filename() + ".png"
        print "\n{method} Screenshot and HTML:\n".format(
            method=self._testMethodName)
        print 'screenshot:', filename
        self.driver.get_screenshot_as_file(filename)
        text_file = open("Clicktrans3RaportScreeny.txt", "a")
        text_file.write("<br><br>{method} Screenshot and HTML:<br>".format(
            method=self._testMethodName)+"<br>Screenshot: <a href=""http://ci.testuj.pl/job/Clicktrans3/ws/screendumps/"+self._saved_filename+".png>"+self._saved_filename+"</a>")
        text_file.close()

    def dump_html(self):
        filename = self._get_filename() + '.html'
        print 'page HTML:', filename
        with open(filename, 'w') as f:
            f.write(self.driver.page_source.encode('utf-8'))
        text_file = open("Clicktrans3RaportScreeny.txt", "a")
        text_file.write("<br>Html: <a href=""http://ci.testuj.pl/job/Clicktrans3/ws/screendumps/"+self._saved_filename+".html>"+self._saved_filename+"</a>")
        text_file.close()

    def _send_email(self):
        from mailer import Mailer
        from mailer import Message

        message = Message(From="jedrzej.wojcieszczyk@testuj.pl",
                          To=["jedrzej.wojcieszczyk@testuj.pl"])
        message.Subject = "Raport Clicktrans3 Testy Automatyczne Jenkins"
        message.Html = """<head><meta http-equiv="Content-Type" content="text/html;charset=UTF-8"></head><p>Cześć!<br>
           Oto wygenerowany automatycznie raport z testów Clicktrans 3<br><br>
           Tabela raportowa z logami wykonanych testów, a pod nią linki do screenshotów i kodu html testów które nie przeszły oraz wykres statystyczny:  <a href="http://ci.testuj.pl/job/Clicktrans3/ws/Clicktrans3ReportLogi.html">Tabela z logami, screenshoty i wykres</a></p>"""

        sender = Mailer('smtp.gmail.com', use_tls=True, usr='jedrzej.wojcieszczyk@testuj.pl', pwd='paluch88')
        sender.send(message)

open("Clicktrans3RaportScreeny.txt", 'w').close()
suite = unittest.TestLoader().loadTestsFromTestCase(SmokeTest)
outfile = open("Clicktrans3ReportLogi.html", "wb")
runner = HTMLTestRunner(stream=outfile, title='Test Report', description='Clicktrans3', verbosity=2)
runner.run(suite)

     # htmltestrunner.main()
     # unittest.main()
     # import xmlrunner
     # unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
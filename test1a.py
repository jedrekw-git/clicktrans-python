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

    def test_user_add_new_consignment_urgent_and_highlited_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.add_consignment_parcel()
        add_consignment_page.set_urgent()
        add_consignment_page.set_highlited()
        add_consignment_page.save_transport()

        Assert.contains(u"Twoje ogłoszenie zostało zapisane i będzie opublikowane po dokonaniu wpłaty.", add_consignment_page.get_page_source())

        add_consignment_page.pay_with_test_payment()
        # Assert.contains(strftime("%d.%m.%Y", gmtime()), add_consignment_page.get_first_payment_date())

        add_consignment_page.get_consignment_title_from_result_page_after_payment()

        if u"Twoja przesy\u0142ka" in add_consignment_page.get_page_source():
            Assert.equal(add_consignment_page.consignment_title_result_page_after_payment, add_consignment_page._title_uuid)
            Assert.contains(u"zosta\u0142a wystawiona! Wyr\xf3\u017cnienie og\u0142oszenia b\u0119dzie widoczne od razu po zaksi\u0119gowaniu wp\u0142aty w systemie PayU.", add_consignment_page.get_page_source())
        else:
            Assert.contains(u"Operacja przebiegła pomyślnie. Wyróżnienie Twojego ogłoszenia będzie widoczne od razu po zaksięgowaniu wpłaty w systemie PayU. Zobacz swoje ogłoszenie:", add_consignment_page.get_page_source())
            Assert.equal(add_consignment_page.consignment_title_result_page_after_payment, add_consignment_page._title_uuid)

    def test_user_add_new_consignment_urgent_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.add_consignment_parcel()
        add_consignment_page.set_urgent()
        add_consignment_page.save_transport()

        Assert.contains(u"Twoje ogłoszenie zostało zapisane i będzie opublikowane po dokonaniu wpłaty.", add_consignment_page.get_page_source())

        add_consignment_page.pay_with_test_payment()
        # Assert.contains(strftime("%d.%m.%Y", gmtime()), add_consignment_page.get_first_payment_date())

        add_consignment_page.get_consignment_title_from_result_page_after_payment()

        if u"Twoja przesy\u0142ka" in add_consignment_page.get_page_source():
            Assert.equal(add_consignment_page.consignment_title_result_page_after_payment, add_consignment_page._title_uuid)
            Assert.contains(u"zosta\u0142a wystawiona! Wyr\xf3\u017cnienie og\u0142oszenia b\u0119dzie widoczne od razu po zaksi\u0119gowaniu wp\u0142aty w systemie PayU.", add_consignment_page.get_page_source())
        else:
            Assert.contains(u"Operacja przebiegła pomyślnie. Wyróżnienie Twojego ogłoszenia będzie widoczne od razu po zaksięgowaniu wpłaty w systemie PayU. Zobacz swoje ogłoszenie:", add_consignment_page.get_page_source())
            Assert.equal(add_consignment_page.consignment_title_result_page_after_payment, add_consignment_page._title_uuid)

    def test_user_add_new_consignment_highlited_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.add_consignment_parcel()
        add_consignment_page.set_highlited()
        add_consignment_page.save_transport()

        Assert.contains(u"Twoje ogłoszenie zostało zapisane i będzie opublikowane po dokonaniu wpłaty.", add_consignment_page.get_page_source())

        add_consignment_page.pay_with_test_payment()
        # Assert.contains(strftime("%d.%m.%Y", gmtime()), add_consignment_page.get_first_payment_date())

        add_consignment_page.get_consignment_title_from_result_page_after_payment()

        if u"Twoja przesy\u0142ka" in add_consignment_page.get_page_source():
            Assert.equal(add_consignment_page.consignment_title_result_page_after_payment, add_consignment_page._title_uuid)
            Assert.contains(u"zosta\u0142a wystawiona! Wyr\xf3\u017cnienie og\u0142oszenia b\u0119dzie widoczne od razu po zaksi\u0119gowaniu wp\u0142aty w systemie PayU.", add_consignment_page.get_page_source())
        else:
            Assert.contains(u"Operacja przebiegła pomyślnie. Wyróżnienie Twojego ogłoszenia będzie widoczne od razu po zaksięgowaniu wpłaty w systemie PayU. Zobacz swoje ogłoszenie:", add_consignment_page.get_page_source())
            Assert.equal(add_consignment_page.consignment_title_result_page_after_payment, add_consignment_page._title_uuid)

    def test_user_login_while_adding_new_consignment_set_highlited_and_urgent_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.add_consignment_parcel()
        add_consignment_page.set_urgent()
        add_consignment_page.set_highlited()
        add_consignment_page.save_transport()
        account_page = home_page.header.login(USER, PASSWORD)

        Assert.contains(u"Twoje ogłoszenie zostało zapisane i będzie opublikowane po dokonaniu wpłaty.", add_consignment_page.get_page_source())
        Assert.contains(u"Zalogowałeś się", add_consignment_page.get_page_source())

        add_consignment_page.pay_with_test_payment()
        # Assert.contains(strftime("%d.%m.%Y", gmtime()), add_consignment_page.get_first_payment_date())

        add_consignment_page.get_consignment_title_from_result_page_after_payment()

        if u"Twoja przesy\u0142ka" in add_consignment_page.get_page_source():
            Assert.equal(add_consignment_page.consignment_title_result_page_after_payment, add_consignment_page._title_uuid)
            Assert.contains(u"zosta\u0142a wystawiona! Wyr\xf3\u017cnienie og\u0142oszenia b\u0119dzie widoczne od razu po zaksi\u0119gowaniu wp\u0142aty w systemie PayU.", add_consignment_page.get_page_source())
        else:
            Assert.contains(u"Operacja przebiegła pomyślnie. Wyróżnienie Twojego ogłoszenia będzie widoczne od razu po zaksięgowaniu wpłaty w systemie PayU. Zobacz swoje ogłoszenie:", add_consignment_page.get_page_source())
            Assert.equal(add_consignment_page.consignment_title_result_page_after_payment, add_consignment_page._title_uuid)

    def test_user_login_while_adding_new_consignment_set_highlited_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.add_consignment_parcel()
        add_consignment_page.set_highlited()
        add_consignment_page.save_transport()
        account_page = home_page.header.login(USER, PASSWORD)

        Assert.contains(u"Twoje ogłoszenie zostało zapisane i będzie opublikowane po dokonaniu wpłaty.", add_consignment_page.get_page_source())
        Assert.contains(u"Zalogowałeś się", add_consignment_page.get_page_source())

        add_consignment_page.pay_with_test_payment()
        # Assert.contains(strftime("%d.%m.%Y", gmtime()), add_consignment_page.get_first_payment_date())

        add_consignment_page.get_consignment_title_from_result_page_after_payment()

        if u"Twoja przesy\u0142ka" in add_consignment_page.get_page_source():
            Assert.equal(add_consignment_page.consignment_title_result_page_after_payment, add_consignment_page._title_uuid)
            Assert.contains(u"zosta\u0142a wystawiona! Wyr\xf3\u017cnienie og\u0142oszenia b\u0119dzie widoczne od razu po zaksi\u0119gowaniu wp\u0142aty w systemie PayU.", add_consignment_page.get_page_source())
        else:
            Assert.contains(u"Operacja przebiegła pomyślnie. Wyróżnienie Twojego ogłoszenia będzie widoczne od razu po zaksięgowaniu wpłaty w systemie PayU. Zobacz swoje ogłoszenie:", add_consignment_page.get_page_source())
            Assert.equal(add_consignment_page.consignment_title_result_page_after_payment, add_consignment_page._title_uuid)

    def test_user_login_while_adding_new_consignment_set_urgent_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.add_consignment_parcel()
        add_consignment_page.set_urgent()
        add_consignment_page.save_transport()
        account_page = home_page.header.login(USER, PASSWORD)

        Assert.contains(u"Twoje ogłoszenie zostało zapisane i będzie opublikowane po dokonaniu wpłaty.", add_consignment_page.get_page_source())
        Assert.contains(u"Zalogowałeś się", add_consignment_page.get_page_source())

        add_consignment_page.pay_with_test_payment()
        # Assert.contains(strftime("%d.%m.%Y", gmtime()), add_consignment_page.get_first_payment_date())

        add_consignment_page.get_consignment_title_from_result_page_after_payment()

        if u"Twoja przesy\u0142ka" in add_consignment_page.get_page_source():
            Assert.equal(add_consignment_page.consignment_title_result_page_after_payment, add_consignment_page._title_uuid)
            Assert.contains(u"zosta\u0142a wystawiona! Wyr\xf3\u017cnienie og\u0142oszenia b\u0119dzie widoczne od razu po zaksi\u0119gowaniu wp\u0142aty w systemie PayU.", add_consignment_page.get_page_source())
        else:
            Assert.contains(u"Operacja przebiegła pomyślnie. Wyróżnienie Twojego ogłoszenia będzie widoczne od razu po zaksięgowaniu wpłaty w systemie PayU. Zobacz swoje ogłoszenie:", add_consignment_page.get_page_source())
            Assert.equal(add_consignment_page.consignment_title_result_page_after_payment, add_consignment_page._title_uuid)

    def test_user_after_adding_consignment_set_highlited_and_urgent_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        profile_page = home_page.header.open_profile_page()
        profile_page.user_open_my_consignments_menu()
        profile_page.user_click_first_consignment_distinguish_button()
        profile_page.set_consignment_highlited_and_urgent()
        add_consignment_page.pay_with_test_payment()

        add_consignment_page.get_consignment_title_from_result_page_after_payment()

        if u"Twoja przesy\u0142ka" in add_consignment_page.get_page_source():
            Assert.equal(add_consignment_page.consignment_title_result_page_after_payment, add_consignment_page._title_uuid)
            Assert.contains(u"zosta\u0142a wystawiona! Wyr\xf3\u017cnienie og\u0142oszenia b\u0119dzie widoczne od razu po zaksi\u0119gowaniu wp\u0142aty w systemie PayU.", add_consignment_page.get_page_source())
        else:
            Assert.contains(u"Operacja przebiegła pomyślnie. Wyróżnienie Twojego ogłoszenia będzie widoczne od razu po zaksięgowaniu wpłaty w systemie PayU. Zobacz swoje ogłoszenie:", add_consignment_page.get_page_source())
            Assert.equal(add_consignment_page.consignment_title_result_page_after_payment, add_consignment_page._title_uuid)

    def test_user_after_adding_consignment_set_highlited_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        profile_page = home_page.header.open_profile_page()
        profile_page.user_open_my_consignments_menu()
        profile_page.user_click_first_consignment_distinguish_button()
        profile_page.set_consignment_highlited()
        add_consignment_page.pay_with_test_payment()

        add_consignment_page.get_consignment_title_from_result_page_after_payment()

        if u"Twoja przesy\u0142ka" in add_consignment_page.get_page_source():
            Assert.equal(add_consignment_page.consignment_title_result_page_after_payment, add_consignment_page._title_uuid)
            Assert.contains(u"zosta\u0142a wystawiona! Wyr\xf3\u017cnienie og\u0142oszenia b\u0119dzie widoczne od razu po zaksi\u0119gowaniu wp\u0142aty w systemie PayU.", add_consignment_page.get_page_source())
        else:
            Assert.contains(u"Operacja przebiegła pomyślnie. Wyróżnienie Twojego ogłoszenia będzie widoczne od razu po zaksięgowaniu wpłaty w systemie PayU. Zobacz swoje ogłoszenie:", add_consignment_page.get_page_source())
            Assert.equal(add_consignment_page.consignment_title_result_page_after_payment, add_consignment_page._title_uuid)

    def test_user_after_adding_consignment_set_urgent_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        profile_page = home_page.header.open_profile_page()
        profile_page.user_open_my_consignments_menu()
        profile_page.user_click_first_consignment_distinguish_button()
        profile_page.set_consignment_urgent()
        add_consignment_page.pay_with_test_payment()

        add_consignment_page.get_consignment_title_from_result_page_after_payment()

        if u"Twoja przesy\u0142ka" in add_consignment_page.get_page_source():
            Assert.equal(add_consignment_page.consignment_title_result_page_after_payment, add_consignment_page._title_uuid)
            Assert.contains(u"zosta\u0142a wystawiona! Wyr\xf3\u017cnienie og\u0142oszenia b\u0119dzie widoczne od razu po zaksi\u0119gowaniu wp\u0142aty w systemie PayU.", add_consignment_page.get_page_source())
        else:
            Assert.contains(u"Operacja przebiegła pomyślnie. Wyróżnienie Twojego ogłoszenia będzie widoczne od razu po zaksięgowaniu wpłaty w systemie PayU. Zobacz swoje ogłoszenie:", add_consignment_page.get_page_source())
            Assert.equal(add_consignment_page.consignment_title_result_page_after_payment, add_consignment_page._title_uuid)

    def test_zz_generate_plot_and_send_email(self):
        self._save_plot()
        self._send_email()

    def tally(self):
        return len(self._resultForDoCleanups.errors) + len(self._resultForDoCleanups.failures)

    def setUp(self):
        self.timeout = 30
        if run_locally:
            fp = webdriver.FirefoxProfile()
            fp.set_preference("browser.startup.homepage", "about:blank")
            fp.set_preference("startup.homepage_welcome_url", "about:blank")
            fp.set_preference("startup.homepage_welcome_url.additional", "about:blank")
            fp.set_preference(" xpinstall.signatures.required", "false")
            fp.set_preference("toolkit.telemetry.reportingpolicy.firstRun", "false")
            binary = FirefoxBinary('/__stare/firefox45/firefox')
            self.driver = webdriver.Firefox(firefox_binary=binary, firefox_profile=fp)
            self.driver.set_window_size(1024,768)
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
        text_file = open("ClicktransRaportScreeny.txt", "a")
        text_file.write("<br><br>Wykres statystyczny: <a href=""http://ci.testuj.pl/job/Clicktrans/ws/screendumps/"+self._saved_filename_plot+".png>Wykres</a>")
        text_file.close()

    def take_screenshot(self):
        filename = self._get_filename() + ".png"
        print "\n{method} Screenshot and HTML:\n".format(
            method=self._testMethodName)
        print 'screenshot:', filename
        self.driver.get_screenshot_as_file(filename)
        text_file = open("ClicktransRaportScreeny.txt", "a")
        text_file.write("<br><br>{method} Screenshot and HTML:<br>".format(
            method=self._testMethodName)+"<br>Screenshot: <a href=""http://ci.testuj.pl/job/Clicktrans/ws/screendumps/"+self._saved_filename+".png>"+self._saved_filename+"</a>")
        text_file.close()

    def dump_html(self):
        filename = self._get_filename() + '.html'
        print 'page HTML:', filename
        with open(filename, 'w') as f:
            f.write(self.driver.page_source.encode('utf-8'))
        text_file = open("ClicktransRaportScreeny.txt", "a")
        text_file.write("<br>Html: <a href=""http://ci.testuj.pl/job/Clicktrans/ws/screendumps/"+self._saved_filename+".html>"+self._saved_filename+"</a>")
        text_file.close()

    def _send_email(self):
        from mailer import Mailer
        from mailer import Message

        message = Message(From="jedrzej.wojcieszczyk@testuj.pl",
                          To=["jedrzej.wojcieszczyk@testuj.pl"])
        message.Subject = "Raport Clicktrans Testy Automatyczne Jenkins"
        message.Html = """<head><meta http-equiv="Content-Type" content="text/html;charset=UTF-8"></head><p>Cześć!<br>
           Oto wygenerowany automatycznie raport z testów Clicktrans.pl<br><br>
           Tabela raportowa z logami wykonanych testów, a pod nią linki do screenshotów i kodu html testów które nie przeszły oraz wykres statystyczny:  <a href="http://ci.testuj.pl/job/Clicktrans/ws/ClicktransReportLogi.html">Tabela z logami, screenshoty i wykres</a></p>"""

        sender = Mailer('smtp.gmail.com', use_tls=True, usr='jedrzej.wojcieszczyk@testuj.pl', pwd='paluch88')
        sender.send(message)

open("ClicktransRaportScreeny.txt", 'w').close()
suite = unittest.TestLoader().loadTestsFromTestCase(SmokeTest)
outfile = open("ClicktransReportLogi.html", "wb")
runner = HTMLTestRunner(stream=outfile, title='Test Report', description='Clicktrans', verbosity=2)
runner.run(suite)
# coding=utf-8
import unittest
from selenium import webdriver
from time import sleep
from unittestzero import Assert
from pages.home import HomePage
from pages.profile_page import *



run_locally = False

# it's best to remove the hardcoded defaults and always get these values
# from environment variables
# USERNAME = os.environ.get('SAUCE_USERNAME', "clicktrans")
# ACCESS_KEY = os.environ.get('SAUCE_ACCESS_KEY', "88a7db15-e558-413f-b55d-288e883ff00c")
USERNAME = os.environ.get('SAUCE_USERNAME', "testuj")
ACCESS_KEY = os.environ.get('SAUCE_ACCESS_KEY', "0029898f-54be-48b2-9166-9306282bef0c")
sauce = SauceClient(USERNAME, ACCESS_KEY)

browsers = [{"platform": "Windows 8",
             "browserName": "firefox",
             "version": "35.0"}]

def on_platforms(platforms):
    def decorator(base_class):
        module = sys.modules[base_class.__module__].__dict__
        for i, platform in enumerate(platforms):
            d = dict(base_class.__dict__)
            d['desired_capabilities'] = platform
            name = "%s_%s" % (base_class.__name__, i + 1)
            module[name] = new.classobj(name, (base_class,), d)

    return decorator

@on_platforms(browsers)
class SmokeTest(unittest.TestCase):

    #ABY URUCHOMIC TESTY NA SAUCELABS'IE PRZENIEŚ TUTAJ SKRYPT KTÓRY CHCESZ WYKONAC Z PLIKU test.py Z FOLDERU tests np.
    # I URUCHAMIAJ KLIKAJĄC PRAWYM KLAWISZEM NA def on_platforms(platforms): I KLIKAJĄC Run 'Unittests in saucelabs'

    def test_register_user_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        registeration_page = home_page.header.open_registration_page()
        registeration_page.new_user_click_register()
        registeration_page.new_user_fill_data()

        Assert.contains(u"Odbierz pocztę", registeration_page.get_page_source())
        Assert.contains(registeration_page._email, registeration_page.get_page_source())
        Assert.contains(u'i kliknij link aktywacyjny, aby ukończyć rejestrację.', registeration_page.get_page_source())

    def test_withdraw_consignment_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        profile_page = home_page.header.open_profile_page()
        settings = profile_page.withdraw_consignment()
        sleep(3)

        Assert.contains(u"Ogłoszenie zostało wycofane", profile_page.get_page_source())

    def test_report_violation_to_offer_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        submit_offer = view_consignments_page.check_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        account_page = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.report_violation_to_offer()

        Assert.contains(u"Zgłoszenie zostało odnotowane.", consignment.get_page_source())

    def test_report_violation_to_question_to_offer_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        submit_offer = view_consignments_page.check_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.add_question_to_offer()
        consignment.report_violation_to_question_to_offer()

        Assert.contains(u"Zgłoszenie zostało odnotowane.", consignment.get_page_source())

    def test_withdraw_offer_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        submit_offer = view_consignments_page.check_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        profile = home_page.header.open_profile_page()
        profile.withdraw_offer()

        Assert.contains(u"Oferta została wycofana.", profile.get_page_source())

    def test_watch_auction_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        consignment = view_consignments_page.check_added_consignment()
        consignment.watch_consignment()

        Assert.contains(u"Ogłoszenie obserwowane", consignment.get_page_source())

    def test_reject_offer_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        submit_offer = view_consignments_page.check_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.reject_offer()
        sleep(3)

        Assert.contains(u"Oferta została odrzucona.", consignment.get_page_source())

    def test_user_reply_to_question_to_consignment_from_provider_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        consignment = view_consignments_page.check_added_consignment()
        consignment.provider_add_question_to_consignment()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.user_open_first_message()
        consignment.reply_to_provider_question_to_consignment()

        Assert.contains(u"Twoja odpowiedź została dodana.", consignment.get_page_source())
        Assert.contains(u"This is my reply", consignment.get_page_source())

    def test_user_send_commentary_from_ended_transactions_menu_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        submit_offer = view_consignments_page.check_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.accept_offer()
        profile = home_page.header.open_profile_page()
        profile.user_send_commentary_from_ended_transactions_menu()

        Assert.contains(u"Komentarz został wystawiony.", consignment.get_page_source())

    def test_user_send_commentary_from_commentaries_menu_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        submit_offer = view_consignments_page.check_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.accept_offer()
        profile = home_page.header.open_profile_page()
        profile.user_send_commentary_from_commentaries_menu()

        Assert.contains(u"Komentarz został wystawiony.", consignment.get_page_source())

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
        add_consignment_page.get_consignment_title_from_result_page_after_payment()

        Assert.contains(u"Twoja przesyłka", add_consignment_page.get_page_source())
        Assert.equal(add_consignment_page.consignment_title_result_page_after_payment, add_consignment_page._title_uuid)
        Assert.contains(u"została wystawiona! Wyróżnienie ogłoszenia będzie widoczne od razu po zaksięgowaniu wpłaty w systemie PayU.", add_consignment_page.get_page_source())

    def test_user_add_new_consignment_urgent_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.add_consignment_parcel()
        add_consignment_page.set_urgent()
        add_consignment_page.save_transport()

        Assert.contains(u"Twoje ogłoszenie zostało zapisane i będzie opublikowane po dokonaniu wpłaty.", add_consignment_page.get_page_source())

        add_consignment_page.pay_with_test_payment()
        add_consignment_page.get_consignment_title_from_result_page_after_payment()

        Assert.contains(u"Twoja przesyłka", add_consignment_page.get_page_source())
        Assert.equal(add_consignment_page.consignment_title_result_page_after_payment, add_consignment_page._title_uuid)
        Assert.contains(u"została wystawiona! Wyróżnienie ogłoszenia będzie widoczne od razu po zaksięgowaniu wpłaty w systemie PayU.", add_consignment_page.get_page_source())

    def test_user_add_new_consignment_highlited_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.add_consignment_parcel()
        add_consignment_page.set_highlited()
        add_consignment_page.save_transport()

        Assert.contains(u"Twoje ogłoszenie zostało zapisane i będzie opublikowane po dokonaniu wpłaty.", add_consignment_page.get_page_source())

        add_consignment_page.pay_with_test_payment()
        add_consignment_page.get_consignment_title_from_result_page_after_payment()

        Assert.contains(u"Twoja przesyłka", add_consignment_page.get_page_source())
        Assert.equal(add_consignment_page.consignment_title_result_page_after_payment, add_consignment_page._title_uuid)
        Assert.contains(u"została wystawiona! Wyróżnienie ogłoszenia będzie widoczne od razu po zaksięgowaniu wpłaty w systemie PayU.", add_consignment_page.get_page_source())

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
        add_consignment_page.get_consignment_title_from_result_page_after_payment()

        Assert.contains(u"Twoja przesyłka", add_consignment_page.get_page_source())
        Assert.equal(add_consignment_page.consignment_title_result_page_after_payment, add_consignment_page._title_uuid)
        Assert.contains(u"została wystawiona! Wyróżnienie ogłoszenia będzie widoczne od razu po zaksięgowaniu wpłaty w systemie PayU.", add_consignment_page.get_page_source())

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
        add_consignment_page.get_consignment_title_from_result_page_after_payment()

        Assert.contains(u"Twoja przesyłka", add_consignment_page.get_page_source())
        Assert.equal(add_consignment_page.consignment_title_result_page_after_payment, add_consignment_page._title_uuid)
        Assert.contains(u"została wystawiona! Wyróżnienie ogłoszenia będzie widoczne od razu po zaksięgowaniu wpłaty w systemie PayU.", add_consignment_page.get_page_source())

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
        add_consignment_page.get_consignment_title_from_result_page_after_payment()

        Assert.contains(u"Twoja przesyłka", add_consignment_page.get_page_source())
        Assert.equal(add_consignment_page.consignment_title_result_page_after_payment, add_consignment_page._title_uuid)
        Assert.contains(u"została wystawiona! Wyróżnienie ogłoszenia będzie widoczne od razu po zaksięgowaniu wpłaty w systemie PayU.", add_consignment_page.get_page_source())

    def setUp(self):
        self.timeout = 30

        if run_locally:
            self.driver = webdriver.Firefox()
            self.driver.implicitly_wait(self.timeout)
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
            self.driver.quit()
        else:
            print("Link to your job: https://saucelabs.com/jobs/%s" % self.driver.session_id)
            try:
                if sys.exc_info() == (None, None, None):
                    sauce.jobs.update_job(self.driver.session_id, passed=True)
                else:
                    sauce.jobs.update_job(self.driver.session_id, passed=False)
            finally:
                self.driver.quit()


if __name__ == '__main__':
    unittest.main()
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

    def test_add_new_consignment_logged_in_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        add_consignment_page.get_consignment_title_from_result_page()

        Assert.contains(u"Twoja przesyłka", add_consignment_page.get_page_source())
        Assert.contains(u"została wystawiona!", add_consignment_page.get_page_source())
        Assert.equal(add_consignment_page.consignment_title_result_page, add_consignment_page._title_uuid)

    def test_new_consignment_should_appear_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid))
        view_consignments_page.open_added_consignment()

        Assert.contains(add_consignment_page._title_uuid, view_consignments_page.get_page_source())
        Assert.contains(u"Polska, Dolno\u015bl\u0105skie, Wroclaw, 54-612\xa0 Kasztanowa 23", view_consignments_page.get_page_source())
        Assert.contains(u'Polska, Podlaskie, Warszawa, 02-796\xa0 Chmielna 85', view_consignments_page.get_page_source())
        Assert.contains(u'379.50 km', view_consignments_page.get_page_source())
        Assert.contains(u'Tylko transport', view_consignments_page.get_page_source())
        Assert.contains(u'This is my additional info', view_consignments_page.get_page_source())

    def test_add_new_consignment_not_logged_in_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        Assert.contains(u"Jeszcze tylko chwila...", add_consignment_page.get_page_source())
        Assert.contains(u"Twoje og\u0142oszenie o przesy\u0142ce \xa0zosta\u0142o zapisane, ale musisz si\u0119 <strong>zalogowa\u0107,</strong> aby by\u0142o widoczne dla Przewo\u017anik\xf3w.", add_consignment_page.get_page_source())
        Assert.contains(u"Nie masz konta? <strong>Zarejestruj się </strong><strong>w 1 minutę (za darmo)</strong>. Twoje dane są <strong>chronione</strong> i nie będą upublicznione.", add_consignment_page.get_page_source())
        home_page.header.login(USER, PASSWORD)

        Assert.contains(u"Twoja przesyłka", add_consignment_page.get_page_source())
        Assert.contains(u"została wystawiona!", add_consignment_page.get_page_source())

    def test_add_new_consignment_not_activated_user_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        registeration_page = home_page.header.continue_to_registration_page()
        registeration_page.add_new_consignment_unactivated_fill_username_field()
        registeration_page.add_new_consignment_unactivated_fill_email_field()
        registeration_page.new_user_fill_data()

        Assert.contains(u"Odbierz pocztę", registeration_page.get_page_source())
        Assert.contains(registeration_page._email_user_add_new_consignment, registeration_page.get_page_source())
        Assert.contains(u'Na Twój adres', registeration_page.get_page_source())
        Assert.contains(u'wys\u0142ali\u015bmy e-mail aktywacyjny.\xa0Po aktywacji konta Twoja przesy\u0142ka\xa0zostanie wystawiona.', registeration_page.get_page_source())
        Assert.contains(u'Je\u017celi Tw\xf3j email jest na wp.pl, o2.pl, tlen.pl to sprawd\u017a zak\u0142adk\u0119 <em>Oferty</em>\xa0oraz <em>Spam </em>swojej skrzynki odbiorczej.', registeration_page.get_page_source())

    def test_add_new_consignment_not_logged_in_provider_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        Assert.contains(u"Jeszcze tylko chwila...", add_consignment_page.get_page_source())
        Assert.contains(u"Twoje og\u0142oszenie o przesy\u0142ce \xa0zosta\u0142o zapisane, ale musisz si\u0119 <strong>zalogowa\u0107,</strong> aby by\u0142o widoczne dla Przewo\u017anik\xf3w.", add_consignment_page.get_page_source())
        Assert.contains(u"Nie masz konta? <strong>Zarejestruj się </strong><strong>w 1 minutę (za darmo)</strong>. Twoje dane są <strong>chronione</strong> i nie będą upublicznione.", add_consignment_page.get_page_source())
        home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)

        Assert.contains(u"Twoja przesyłka", add_consignment_page.get_page_source())
        Assert.contains(u"została wystawiona!", add_consignment_page.get_page_source())

    def test_register_user_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        registeration_page = home_page.header.open_registration_page()
        registeration_page.new_user_click_register()
        registeration_page.register_user_fill_username_field()
        registeration_page.register_user_fill_email_field()
        registeration_page.new_user_fill_data()

        Assert.contains(u"Odbierz pocztę", registeration_page.get_page_source())
        Assert.contains(registeration_page._email_user_register, registeration_page.get_page_source())
        Assert.contains(u'i kliknij link aktywacyjny, aby ukończyć rejestrację.', registeration_page.get_page_source())

    def test_login_unactivated_user_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        registeration_page = home_page.header.open_registration_page()
        registeration_page.new_user_click_register()
        registeration_page.login_unactivated_user_fill_username_field()
        registeration_page.login_unactivated_user_fill_email_field()
        registeration_page.new_user_fill_data()
        account_page = home_page.header.login(registeration_page._username_user_login_unactivated, registeration_page._password)

        Assert.contains(u"Twoja rejestracja nie została ukończona", registeration_page.get_page_source())
        Assert.contains(u"Odbierz pocztę i kliknij link aktywacyjny, aby ukończyć rejestrację.", registeration_page.get_page_source())

    def test_logout_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        home_page.header.login(USER, PASSWORD)
        home_page.header.logout()
        sleep(3)
        Assert.contains(u"Wylogowałeś się", home_page.get_page_source())

    def test_register_new_transport_provider_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        registeration_page = home_page.header.open_registration_page()
        registeration_page.new_transport_provider()

        Assert.contains(u"Odbierz pocztę", registeration_page.get_page_source())
        Assert.contains(registeration_page._email, registeration_page.get_page_source())
        Assert.contains(u'i kliknij link aktywacyjny, aby ukończyć rejestrację.', registeration_page.get_page_source())

    def test_edit_user_profile_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        profile_page = home_page.header.open_profile_page()
        profile_page.edit_user_profile()

        Assert.contains(u"Zmiany zostały zapisane.", profile_page.get_page_source())

    def test_edit_consignment_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        profile_page = home_page.header.open_profile_page()
        settings = profile_page.edit_consignment()
        settings.edit_consignment_move_house()

        Assert.contains(u"Zmiany w Twojej przesyłce", settings.get_page_source())
        Assert.contains(settings._title_uuid, profile_page.get_page_source())
        Assert.contains(u"zostały pomyślnie zapisane.", settings.get_page_source())

    def test_withdraw_consignment_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        profile_page = home_page.header.open_profile_page()
        settings = profile_page.withdraw_consignment()
        sleep(3)

        Assert.contains(u"Ogłoszenie zostało wycofane", profile_page.get_page_source())

    def test_report_violation_to_consignment_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.report_violation_to_consignmeent()

        Assert.contains(u"Zgłoszenie zostało odnotowane.", consignment.get_page_source())

    def test_report_violation_to_offer_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid))
        submit_offer = view_consignments_page.open_added_consignment()
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
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid))
        submit_offer = view_consignments_page.open_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.add_question_to_offer()
        consignment.report_violation_to_question_to_offer()

        Assert.contains(u"Zgłoszenie zostało odnotowane.", consignment.get_page_source())

    def test_report_violation_to_question_to_consignment_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid))
        consignment = view_consignments_page.open_added_consignment()
        consignment.provider_add_question_to_consignment()
        consignment.report_violation_to_question_to_consignment()

        Assert.contains(u"Zgłoszenie zostało odnotowane.", consignment.get_page_source())

    def test_check_categories_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.add_consignment_parcel()
        add_consignment_page.save_transport()
        view_consignment_page = home_page.header.view_consignments_page()
        view_consignment_page.check_categories()
        sleep(10)
        view_consignment_page.click_first_result()
        Assert.contains("Podlaskie", view_consignment_page.get_page_source())
        Assert.contains('Paczki', view_consignment_page.get_page_source())

    def test_submit_offer_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid))
        submit_offer = view_consignments_page.open_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()

        Assert.contains(u"Oferta została złożona", submit_offer.get_page_source())

    def test_withdraw_offer_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid))
        submit_offer = view_consignments_page.open_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        profile = home_page.header.open_profile_page()
        profile.withdraw_offer()

        Assert.contains(u"Oferta może zostać wycofana najwcześniej 3 godziny od jej złożenia.", profile.get_page_source())

    def test_submit_offer_with_expiration_date_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid))
        consignment = view_consignments_page.open_added_consignment()
        consignment.submit_offer()
        consignment.enter_expiration_date()
        consignment.confirm_submit_offer()

        Assert.contains(u"Oferta została złożona", consignment.get_page_source())

    def test_issue_consignment_again_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        profile_page = home_page.header.open_profile_page()
        settings = profile_page.withdraw_consignment()
        profile = home_page.header.open_profile_page()
        edit_settings = profile.issue_consignment_again()
        edit_settings.edit_consignment_cars()

        Assert.contains(u"Twoja przesyłka", edit_settings.get_page_source())
        Assert.contains(u"została wystawiona!", edit_settings.get_page_source())

    def test_watch_auction_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid))
        consignment = view_consignments_page.open_added_consignment()
        consignment.watch_consignment()

        sleep(2)
        Assert.contains(u"Ogłoszenie obserwowane", consignment.get_page_source())

    def test_commission_payback_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid))
        submit_offer = view_consignments_page.open_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.accept_offer()
        home_page = HomePage(self.driver).open_home_page()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        profile = home_page.header.open_profile_page()
        profile.payback_commission()

        Assert.contains(u"Wniosek został wysłany do rozpatrzenia. O wyniku zostaniesz poinformowany mailem.", profile.get_page_source())

    def test_edit_provider_profile_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        profile_page = home_page.header.open_profile_page()
        profile_page.edit_provider_profile()

        Assert.contains(u"Profil został zaktualizowany", profile_page.get_page_source())

    def test_edit_provider_data_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(PROVIDER_USER2, PROVIDER_PASSWORD2)
        profile_page = home_page.header.open_profile_page()
        profile_page.edit_provider_data()

        Assert.contains(u"Zmiany zostały zapisane.", profile_page.get_page_source())

    def test_edit_provider_notifications_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        profile_page = home_page.header.open_profile_page()
        profile_page.edit_provider_notifications()

        Assert.contains(u"Zmiany zostały zapisane.", profile_page.get_page_source())

    def test_change_password_should_succeed(self):

        home_page = HomePage(self.driver).open_home_page()
        _saved_password = get_password("change_pass1.txt")
        account_page = home_page.header.login(CHANGE_PASSWORD_USER, _saved_password)
        profile_page = home_page.header.open_profile_page()
        profile_page.change_password()

        Assert.contains(u"Hasło zostało zmienione.", profile_page.get_page_source())

    def test_reject_offer_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid))
        submit_offer = view_consignments_page.open_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.reject_offer()
        sleep(3)

        Assert.contains(u"Oferta została odrzucona.", consignment.get_page_source())

    def test_add_question_to_offer_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid))
        submit_offer = view_consignments_page.open_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.add_question_to_offer()
        sleep(3)

        Assert.contains(u"Twoja wiadomość została dodana.", consignment.get_page_source())
        Assert.contains(u"This is my question", consignment.get_page_source())

    def test_provider_reply_to_question_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid))
        submit_offer = view_consignments_page.open_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.add_question_to_offer()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_message()
        consignment.reply_to_question()

        Assert.contains(u"Twoja wiadomość została dodana.", consignment.get_page_source())
        Assert.contains(u"This is my answer", consignment.get_page_source())

    def test_provider_add_question_to_consignment_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid))
        consignment = view_consignments_page.open_added_consignment()
        consignment.provider_add_question_to_consignment()

        Assert.contains(u"Twoje pytanie zostało dodane.", consignment.get_page_source())
        Assert.contains(u"This is my question", consignment.get_page_source())

    def test_user_reply_to_question_to_consignment_from_provider_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid))
        consignment = view_consignments_page.open_added_consignment()
        consignment.provider_add_question_to_consignment()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.user_open_first_message()
        consignment.reply_to_provider_question_to_consignment()

        Assert.contains(u"Twoja odpowiedź została dodana.", consignment.get_page_source())
        Assert.contains(u"This is my reply", consignment.get_page_source())

    def test_accept_offer_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        store = home_page.header.open_profile_page()
        store.store_provider_data()
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid))
        submit_offer = view_consignments_page.open_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.accept_offer()
        sleep(3)

        Assert.contains("Gratulacje!", consignment.get_page_source())
        Assert.contains(u"Wybrałeś ofertę Przewoźnika <strong>"+PROVIDER_USER, consignment.get_page_source())
        Assert.contains(u"Skontaktuj się z Przewoźnikiem <strong>"+PROVIDER_USER+u"</strong> w celu realizacji usługi transportowej", consignment.get_page_source())
        Assert.contains(u"Imię i nazwisko: <strong>"+store.name1, consignment.get_page_source())
        Assert.contains("tel.: <strong>"+store.tel, consignment.get_page_source())
        Assert.contains("tel. kom.: <strong>"+store.kom, consignment.get_page_source())
        Assert.contains("e-mail: <strong>"+store.mail, consignment.get_page_source())
        Assert.contains(store.address_table[0], consignment.get_page_source())
        Assert.contains(store.address_table[1], consignment.get_page_source())
        Assert.contains(store.address_table[2], consignment.get_page_source())
        Assert.contains(u"Pobierz list przewozowy, który będzie potwierdzeniem nadania Twojej przesyłki", consignment.get_page_source())
        Assert.contains(u"(Ogłoszenie nieaktualne. Użytkownik wybrał już ofertę)", consignment.get_page_source())

    def test_make_offer_executed_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid))
        submit_offer = view_consignments_page.open_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.accept_offer()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        profile = home_page.header.open_profile_page()
        profile.make_offer_executed()
        profile.make_offer_executed_submit_yes()
        sleep(2)

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(profile._executed_result_field, u"Oferta ma status zrealizowana."))
        # Assert.contains(u"Oferta ma status zrealizowana.", profile.get_page_source())

    def test_provider_send_commentary_from_my_offers_menu_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid))
        submit_offer = view_consignments_page.open_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.accept_offer()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        profile = home_page.header.open_profile_page()
        profile.provider_send_commentary_from_my_offers_menu()

        Assert.contains(u"Komentarz został wystawiony.", consignment.get_page_source())

    def test_reply_to_question_to_consignment_from_panel_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid))
        consignment = view_consignments_page.open_added_consignment()
        consignment.provider_add_question_to_consignment()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        profile.user_click_reply_to_question()

        Assert.contains(u"Napisz wiadomość i ustal z Przewoźnikiem niezbędne szczegóły. Aby transakcja była bezpieczna musisz jeszcze zaakceptować ofertę Przewoźnika.", profile.get_page_source())

        consignment.reply_to_provider_question_to_consignment()

        Assert.contains(u"Twoja odpowiedź została dodana.", profile.get_page_source())
        Assert.contains(u"This is my reply", profile.get_page_source())

    def test_user_send_commentary_from_ended_transactions_menu_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid))
        submit_offer = view_consignments_page.open_added_consignment()
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
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid))
        submit_offer = view_consignments_page.open_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.accept_offer()
        profile = home_page.header.open_profile_page()
        profile.user_send_commentary_from_commentaries_menu()

        Assert.contains(u"Komentarz został wystawiony.", consignment.get_page_source())

    def test_provider_reply_to_negative_commentary_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid))
        submit_offer = view_consignments_page.open_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.accept_offer()
        profile = home_page.header.open_profile_page()
        profile.user_send_negative_commentary()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        profile = home_page.header.open_profile_page()
        profile.provider_reply_to_negative_commentary()

        Assert.contains(u"This is my commentary", profile.get_page_source())
        Assert.contains(u"This is my reply", profile.get_page_source())

    def test_provider_send_commentary_from_commentaries_menu_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid))
        submit_offer = view_consignments_page.open_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.accept_offer()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        profile = home_page.header.open_profile_page()
        profile.provider_send_commentary_from_commentaries_menu()

        Assert.contains(u"Komentarz został wystawiony.", consignment.get_page_source())

    def test_ask_for_offer_on_provider_page_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider_page = home_page.header.view_provider_JLMTranspol_page()
        provider_page.ask_for_offer_on_provider_page()

        Assert.contains(u"Twoja prośba o ofertę została wysłana do Przewoźnika.", provider_page.get_page_source())

    def test_ask_for_offer_while_adding_consignment_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        add_consignment_page.ask_for_offer_while_adding_consignment()
        sleep(2)

        Assert.contains(u"Prośba wysłana", add_consignment_page.get_page_source())

    def test_ask_for_offer_for_added_consignment_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        profile = home_page.header.open_profile_page()
        profile.ask_for_offer_for_added_consignment()
        sleep(4)
        Assert.contains(u"Prośba wysłana", profile.get_page_source())

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

    def test_provider_add_new_consignment_urgent_and_highlited_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.add_consignment_parcel()
        add_consignment_page.set_urgent()
        add_consignment_page.set_highlited()
        add_consignment_page.save_transport()

        Assert.contains(u"Twoja przesy\u0142ka zosta\u0142a wystawiona! Op\u0142ata za wyr\xf3\u017cnienie og\u0142oszenia zosta\u0142a doliczona do Twojego salda (zak\u0142adka Moje konto &gt; Rozliczenia).", add_consignment_page.get_page_source())

    def test_provider_add_new_consignment_highlited_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.add_consignment_parcel()
        add_consignment_page.set_highlited()
        add_consignment_page.save_transport()

        Assert.contains(u"Twoja przesy\u0142ka zosta\u0142a wystawiona! Op\u0142ata za wyr\xf3\u017cnienie og\u0142oszenia zosta\u0142a doliczona do Twojego salda (zak\u0142adka Moje konto &gt; Rozliczenia).", add_consignment_page.get_page_source())

    def test_provider_add_new_consignment_urgent_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.add_consignment_parcel()
        add_consignment_page.set_urgent()
        add_consignment_page.save_transport()

        Assert.contains(u"Twoja przesy\u0142ka zosta\u0142a wystawiona! Op\u0142ata za wyr\xf3\u017cnienie og\u0142oszenia zosta\u0142a doliczona do Twojego salda (zak\u0142adka Moje konto &gt; Rozliczenia).", add_consignment_page.get_page_source())

    def test_provider_login_while_adding_new_consignment_set_highlited_and_urgent_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.add_consignment_parcel()
        add_consignment_page.set_urgent()
        add_consignment_page.set_highlited()
        add_consignment_page.save_transport()
        account_page = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)

        Assert.contains(u"Twoja przesy\u0142ka zosta\u0142a wystawiona! Op\u0142ata za wyr\xf3\u017cnienie og\u0142oszenia zosta\u0142a doliczona do Twojego salda (zak\u0142adka Moje konto &gt; Rozliczenia).", add_consignment_page.get_page_source())
        Assert.contains(u"Zalogowałeś się", add_consignment_page.get_page_source())

    def test_provider_login_while_adding_new_consignment_set_highlited_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.add_consignment_parcel()
        add_consignment_page.set_highlited()
        add_consignment_page.save_transport()
        account_page = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)

        Assert.contains(u"Twoja przesy\u0142ka zosta\u0142a wystawiona! Op\u0142ata za wyr\xf3\u017cnienie og\u0142oszenia zosta\u0142a doliczona do Twojego salda (zak\u0142adka Moje konto &gt; Rozliczenia).", add_consignment_page.get_page_source())
        Assert.contains(u"Zalogowałeś się", add_consignment_page.get_page_source())

    def test_provider_login_while_adding_new_consignment_set_urgent_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.add_consignment_parcel()
        add_consignment_page.set_urgent()
        add_consignment_page.save_transport()
        account_page = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)

        Assert.contains(u"Twoja przesy\u0142ka zosta\u0142a wystawiona! Op\u0142ata za wyr\xf3\u017cnienie og\u0142oszenia zosta\u0142a doliczona do Twojego salda (zak\u0142adka Moje konto &gt; Rozliczenia).", add_consignment_page.get_page_source())
        Assert.contains(u"Zalogowałeś się", add_consignment_page.get_page_source())

    def test_provider_after_adding_consignment_set_highlited_and_urgent_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        profile_page = home_page.header.open_profile_page()
        profile_page.provider_open_my_consignments_menu()
        profile_page.provider_click_first_consignment_distinguish_button()
        profile_page.set_consignment_highlited_and_urgent()

        Assert.contains(u"Operacja przebiegła pomyślnie.", add_consignment_page.get_page_source())

    def test_provider_after_adding_consignment_set_highlited_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        profile_page = home_page.header.open_profile_page()
        profile_page.provider_open_my_consignments_menu()
        profile_page.provider_click_first_consignment_distinguish_button()
        profile_page.set_consignment_highlited()

        Assert.contains(u"Operacja przebiegła pomyślnie.", add_consignment_page.get_page_source())

    def test_provider_after_adding_consignment_set_urgent_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        profile_page = home_page.header.open_profile_page()
        profile_page.provider_open_my_consignments_menu()
        profile_page.provider_click_first_consignment_distinguish_button()
        profile_page.set_consignment_urgent()

        Assert.contains(u"Operacja przebiegła pomyślnie.", add_consignment_page.get_page_source())

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
                          To=["sergii.demianchuk@clicktrans.pl", "michal.brzezinski@clicktrans.pl"])
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

     # htmltestrunner.main()
     # unittest.main()
     # import xmlrunner
     # unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
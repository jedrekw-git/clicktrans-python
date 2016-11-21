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
        Assert.contains(u"Jeszcze tylko chwila...", add_consignment_page.get_page_source(), "The text <Jeszcze tylko chwila> didn't appear on confirmation page after entering congigment details consignment, probably the consignment details were wrongly entered")
        Assert.contains(u"Twoje ogłoszenie o przesyłce  zostało zapisane, ale musisz się zalogować, aby było widoczne dla Przewoźników.", add_consignment_page.get_page_source(), "The text <Twoje ogłoszenie o przesyłce  zostało zapisane, ale musisz się zalogować, aby było widoczne dla Przewoźników> didn't appear on confirmation page after adding consignment, probably the consignment details were wrongly entered")
        Assert.contains(u"Nie masz konta? <b>Zarejestruj si\u0119 w 1 minut\u0119 (za darmo).</b> Twoje dane s\u0105 chronione i nie b\u0119d\u0105 upublicznione.", add_consignment_page.get_page_source(), "The text <Nie masz konta? <b>Zarejestruj si\u0119 w 1 minut\u0119 (za darmo).</b> Twoje dane s\u0105 chronione i nie b\u0119d\u0105 upublicznione.> didn't appear on confirmation page after adding consignment, probably the consignment details were wrongly entered")
        home_page.header.login_after_adding_consignment(USER, PASSWORD)

        Assert.contains(u"Twoja przesyłka", add_consignment_page.get_page_source(), "The text <Twoja przesyłka> didn't appear on confirmation page after adding consignment and logging")
        Assert.contains(add_consignment_page._title_uuid, add_consignment_page.get_page_source(), "The consignment title didn't appear on confirmation page after adding consignment and logging")
        Assert.contains(u"została wystawiona!", add_consignment_page.get_page_source(), "The text <została wystawiona!> didn't appear on confirmation page after adding consignment and logging")

    def test_add_new_consignment_not_activated_user_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        registeration_page = home_page.header.continue_to_registration_page()
        registeration_page.add_new_consignment_unactivated_fill_username_field()
        registeration_page.add_new_consignment_unactivated_fill_email_field()
        registeration_page.new_user_fill_data()

        Assert.contains(u"Odbierz pocztę", registeration_page.get_page_source(), "The text <Odbierz pocztę> wasn't found on confirmastion page after entering new user data")
        Assert.contains(registeration_page._email_user_add_new_consignment, registeration_page.get_page_source(), "The user email wasn't found on confirmastion page after entering new user data")
        Assert.contains(u'i kliknij link aktywacyjny, aby ukończyć rejestrację.', registeration_page.get_page_source(), "The text <i kliknij link aktywacyjny, aby ukończyć rejestrację> wasn't found on confirmastion page after entering new user data")

    def test_add_new_consignment_not_logged_in_provider_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        Assert.contains(u"Jeszcze tylko chwila...", add_consignment_page.get_page_source(), "The text <Jeszcze tylko chwila> didn't appear on confirmation page after entering congigment details consignment, probably the consignment details were wrongly entered")
        Assert.contains(u"Twoje ogłoszenie o przesyłce  zostało zapisane, ale musisz się zalogować, aby było widoczne dla Przewoźników.", add_consignment_page.get_page_source(), "The text <Twoje ogłoszenie o przesyłce  zostało zapisane, ale musisz się zalogować, aby było widoczne dla Przewoźników> didn't appear on confirmation page after adding consignment, probably the consignment details were wrongly entered")
        Assert.contains(u"Nie masz konta? <b>Zarejestruj si\u0119 w 1 minut\u0119 (za darmo).</b> Twoje dane s\u0105 chronione i nie b\u0119d\u0105 upublicznione.", add_consignment_page.get_page_source(), "The text <Nie masz konta? <b>Zarejestruj si\u0119 w 1 minut\u0119 (za darmo).</b> Twoje dane s\u0105 chronione i nie b\u0119d\u0105 upublicznione> didn't appear on confirmation page after adding consignment, probably the consignment details were wrongly entered")
        home_page.header.login_after_adding_consignment(PROVIDER_USER2, PROVIDER_PASSWORD2)

        Assert.contains(u"Twoja przesyłka", add_consignment_page.get_page_source(), "The text <Twoja przesyłka> didn't appear on confirmation page after adding consignment and logging")
        Assert.contains(add_consignment_page._title_uuid, add_consignment_page.get_page_source(), "The consignment title didn't appear on confirmation page after adding consignment and logging")
        Assert.contains(u"została wystawiona!", add_consignment_page.get_page_source(), "The text <została wystawiona!> didn't appear on confirmation page after adding consignment and logging")

    def test_add_new_consignment_logged_in_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        add_consignment_page.get_consignment_title_from_result_page()

        Assert.contains(u"Twoja przesyłka", add_consignment_page.get_page_source(), "The text <Twoja przesyłka> didn't appear on confirmation page after adding consignment")
        Assert.contains(u"została wystawiona!", add_consignment_page.get_page_source(), "The text <została wystawiona!> didn't appear on confirmation page after adding consignment")
        Assert.equal(add_consignment_page.consignment_title_result_page, add_consignment_page._title_uuid, "The consignment title didn't appear on confirmation page after adding consignment")

    def test_new_consignment_should_appear_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), "The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
        view_consignments_page.open_added_consignment()

        Assert.contains(add_consignment_page._title_uuid, view_consignments_page.get_page_source(), "THe consignment title didn't appear on added consignment page")
        Assert.contains(u"Wrocław, Polska", view_consignments_page.get_page_source(), "The text <Wrocław, Polska> didn't appear on added consignment page")
        Assert.contains(u'Warszawa, Polska', view_consignments_page.get_page_source(), "The text <Warszawa, Polska> didn't appear on added consignment page")
        Assert.contains(u'347.00  km', view_consignments_page.get_page_source(), "The text <347.00  km> didn't appear on added consignment page, probably the distance between cities has changed")
        Assert.contains(u'Kompleksowa usługa: transport, załadunek i rozładunek', view_consignments_page.get_page_source(), "The text <Kompleksowa usługa: transport, załadunek i rozładunek> didn't appear on added consignment page")
        Assert.contains(u'This is my additional info', view_consignments_page.get_page_source(), "The text <This is my additional info> didn't appear on added consignment page")

    def test_register_user_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        registeration_page = home_page.header.open_registration_page()
        registeration_page.new_user_click_register()
        registeration_page.register_user_fill_username_field()
        registeration_page.register_user_fill_email_field()
        registeration_page.new_user_fill_data()

        Assert.contains(u"Odbierz pocztę", registeration_page.get_page_source(), "The text <Odbierz pocztę> didn't appear on confirmation page after registering user, probably the registration didn't work")
        Assert.contains(registeration_page._email_user_register, registeration_page.get_page_source(), "The registered user email didn't appear on confirmation page after registering user")
        Assert.contains(u'i kliknij link aktywacyjny, aby ukończyć rejestrację.', registeration_page.get_page_source(), "The text <i kliknij link aktywacyjny, aby ukończyć rejestrację.> didn't appear on confirmation page after registering user")

    def test_login_unactivated_user_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        registeration_page = home_page.header.open_registration_page()
        registeration_page.new_user_click_register()
        registeration_page.login_unactivated_user_fill_username_field()
        registeration_page.login_unactivated_user_fill_email_field()
        registeration_page.new_user_fill_data()
        account_page = home_page.header.login(registeration_page._username_user_login_unactivated, registeration_page._password)

        Assert.contains(u"Twoja rejestracja nie została ukończona", registeration_page.get_page_source(), "The text <Twoja rejestracja nie została ukończona> didn't appear on page after logging unactivated user")
        Assert.contains(u"Odbierz pocztę i kliknij link aktywacyjny, aby ukończyć rejestrację.", registeration_page.get_page_source(), "The text <Odbierz pocztę i kliknij link aktywacyjny, aby ukończyć rejestrację.> didn't appear on page after logging unactivated user")

    def test_logout_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        home_page.header.login(USER, PASSWORD)
        home_page.header.logout()
        sleep(3)
        Assert.contains(u"Prześlesz wszystko i wszędzie!", home_page.get_page_source(), "The text <Prześlesz wszystko i wszędzie!> didn't appear on home page")
        Assert.contains(u"Masz pytania? Kontakt:", home_page.get_page_source(), "The text <Masz pytania? Kontakt:> didn't appear on home page")

    def test_register_new_transport_provider_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        registeration_page = home_page.header.open_registration_page()
        registeration_page.new_transport_provider()

        Assert.contains(u"Odbierz pocztę", registeration_page.get_page_source(), "The text <Odbierz pocztę> didn't appear on confirmation page after registering provider, probably the registration didn't work")
        Assert.contains(registeration_page._email, registeration_page.get_page_source(), "The registered provider email didn't appear on confirmation page after registering provider")
        Assert.contains(u'i kliknij link aktywacyjny, aby ukończyć rejestrację.', registeration_page.get_page_source(), "The text <i kliknij link aktywacyjny, aby ukończyć rejestrację.> didn't appear on confirmation page after registering provider")

    def test_edit_user_profile_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        profile_page = home_page.header.open_profile_page()
        profile_page.edit_user_profile()

        Assert.contains(u"Twoje dane zostały zaktualizowane", profile_page.get_page_source(), "The text <Twoje dane zostały zaktualizowane> didn't appear on confirmation page after editing user profile")
        Assert.contains(u"Sprawdź pocztę. Na Twój nowy adres e-mail wysłaliśmy wiadomość z instrukcją jak ukończyć zmianę adresu e-mail.", profile_page.get_page_source(), "The text <Sprawdź pocztę. Na Twój nowy adres e-mail wysłaliśmy wiadomość z instrukcją jak ukończyć zmianę adresu e-mail.> didn't appear on confirmation page after editing user profile")

    def test_edit_consignment_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        profile_page = home_page.header.open_profile_page()
        settings = profile_page.edit_consignment()
        settings.edit_consignment_parcel()

        Assert.contains(u"Zmiany w Twojej przesyłce", settings.get_page_source(), "The text <Zmiany w Twojej przesyłce> didn't appear on confirmation page after editing consignment, probably the edit didn't work well")
        Assert.contains(settings._title_uuid, profile_page.get_page_source(), "The edited consignment title didn't appear on confirmation page after editing consignment, probably the edit didn't work well")
        Assert.contains(u"zostały pomyślnie zapisane.", settings.get_page_source(), "The text <zostały pomyślnie zapisane.> didn't appear on confirmation page after editing consignment, probably the edit didn't work well")

        settings.view_added_consignment()

        Assert.contains(add_consignment_page._title_uuid, settings.get_page_source(), "The edited consignment title didn't appear on consignment page after editing consignment")
        Assert.contains(u"Katowice, Polska", settings.get_page_source(), "The text <Katowice, Polska> didn't appear on consignment page after editing consignment")
        Assert.contains(u'Poznań, Polska', settings.get_page_source(), "The text <Poznań, Polska> didn't appear on consignment page after editing consignment")
        Assert.contains(u'409.00  km', settings.get_page_source(), "The text <409.00  km> didn't appear on consignment page after editing consignment, probably the distance between cities has changed")
        Assert.contains(u'Kompleksowa usługa: transport, załadunek i rozładunek', settings.get_page_source(), "The text <Kompleksowa usługa: transport, załadunek i rozładunek> didn't appear on consignment page after editing consignment")
        Assert.contains(u'This is my additional info after edit', settings.get_page_source(), "The text <This is my additional info after edit> didn't appear on consignment page after editing consignment")

    # PRZEPRASZAMY STRONA NIE ZNALEZIONA, zgłoszone





    def test_withdraw_consignment_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        profile_page = home_page.header.open_profile_page()
        settings = profile_page.withdraw_consignment()
        sleep(3)

        Assert.contains(u"Ogłoszenie zostało wycofane", profile_page.get_page_source(), "The text <Ogłoszenie zostało wycofane> didn't appear on profile page after withdrawing consignment")

    def test_report_violation_to_consignment_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        consignment = add_consignment_page.view_added_consignment()
        consignment.report_violation_to_consignmeent()

        Assert.contains(u"Zgłoszenie zostało odnotowane", consignment.get_page_source(), "The text <Zgłoszenie zostało odnotowane> didn't appear on consignment page after reporting violation")

    def test_report_violation_to_offer_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), "The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
        submit_offer = view_consignments_page.open_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        home_page.header.logout()
        account_page = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.report_violation_to_offer()

        Assert.contains(u"Zgłoszenie zostało odnotowane", consignment.get_page_source(), "The text <Zgłoszenie zostało odnotowane> didn't appear on consignment page after reporting violation to offer")

    def test_report_violation_to_question_to_offer_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), "The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
        submit_offer = view_consignments_page.open_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        home_page.header.logout()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.add_question_to_offer()
        consignment.report_violation_to_question_to_offer()

        Assert.contains(u"Zgłoszenie zostało odnotowane", consignment.get_page_source(), "The text <Zgłoszenie zostało odnotowane> didn't appear on consignment page after reporting violation to question to offer")

    def test_report_violation_to_question_to_consignment_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), "The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
        consignment = view_consignments_page.open_added_consignment()
        consignment.provider_add_question_to_consignment()
        consignment.report_violation_to_question_to_consignment()

        Assert.contains(u"Zgłoszenie zostało odnotowane", consignment.get_page_source(), "The text <Zgłoszenie zostało odnotowane> didn't appear on consignment page after reporting violation to question to consignment")

    def test_check_categories_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.add_consignment_parcel()
        view_consignment_page = home_page.header.view_consignments_page()
        view_consignment_page.check_categories()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(view_consignment_page._first_result_posting_province, "mazowieckie"), "The first result on view consignments page posting province didn't match posting province entered into search field")
        view_consignment_page.click_first_result()
        Assert.contains('Paczki', view_consignment_page.get_page_source(), "The text <Paczki> didn't appear on consignment page, probably the category on view consignments page wasn't chosen")

    def test_submit_offer_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), "The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
        submit_offer = view_consignments_page.open_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()

        Assert.contains(u"Oferta została złożona", submit_offer.get_page_source(), "The text <Oferta została złożona> didn't appear on consignment page after submitting offer, probably offer wasn't submitted")

    def test_withdraw_offer_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), "The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
        submit_offer = view_consignments_page.open_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        profile = home_page.header.open_profile_page()
        profile.withdraw_offer()

        Assert.contains(u"Oferta może zostać wycofana najwcześniej 3 godziny od jej złożenia.", profile.get_page_source(), "The text <Oferta może zostać wycofana najwcześniej 3 godziny od jej złożenia.> didn't appear on consignment page after trying to withdraw offer")

    # def test_issue_consignment_again_should_succeed(self):
    #     home_page = HomePage(self.driver).open_home_page()
    #     account_page = home_page.header.login(USER, PASSWORD)
    #     add_consignment_page = home_page.header.add_consignment_page()
    #     add_consignment_page.new_furniture_consignment()
    #     profile_page = home_page.header.open_profile_page()
    #     settings = profile_page.withdraw_consignment()
    #     profile = home_page.header.open_profile_page()
    #     edit_settings = profile.issue_consignment_again()
    #     edit_settings.edit_consignment_cars()
    #
    #     Assert.contains(u"Twoja przesyłka", edit_settings.get_page_source())
    #     Assert.contains(u"została wystawiona!", edit_settings.get_page_source())
    #
# EDIT CONSIGNMENT

    def test_watch_auction_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), "The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
        consignment = view_consignments_page.open_added_consignment()
        consignment.watch_consignment()

        sleep(2)
        Assert.contains(u"Ogłoszenie obserwowane", consignment.get_page_source(), "The text <Ogłoszenie obserwowane> didn't appear on consignment page after watching consignment")

    def test_commission_payback_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), "The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
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

        Assert.contains(u"Wniosek został wysłany do rozpatrzenia. O wyniku zostaniesz poinformowany mailem.", profile.get_page_source(), "The text <Wniosek został wysłany do rozpatrzenia. O wyniku zostaniesz poinformowany mailem.> didn't appear on profile page after making payback commission")

    def test_edit_provider_profile_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        profile_page = home_page.header.open_profile_page()
        profile_page.edit_provider_profile()

        Assert.contains(u"Zmiany zostały zapisane.", profile_page.get_page_source(), "The text <Zmiany zostały zapisane.> didn't appear on profile page after editing provider profile")
        Assert.equal(profile_page._route_from_value, profile_page.get_value(profile_page._route_from_field), "The edited route <From> value didn't appear on profile page after editing provider profile")
        Assert.equal(profile_page._route_to_value, profile_page.get_value(profile_page._route_to_field), "The edited route <To> value didn't appear on profile page after editing provider profile")


    def test_edit_provider_data_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(PROVIDER_USER2, PROVIDER_PASSWORD2)
        profile_page = home_page.header.open_profile_page()
        profile_page.edit_provider_data()

        Assert.contains(u"Sprawdź pocztę. Na Twój nowy adres e-mail wysłaliśmy wiadomość z instrukcją jak ukończyć zmianę adresu e-mail.", profile_page.get_page_source(), "The text <Sprawdź pocztę. Na Twój nowy adres e-mail wysłaliśmy wiadomość z instrukcją jak ukończyć zmianę adresu e-mail> didn't appear on profile page after editing provider data")
        Assert.contains(u"Twoje dane zostały zaktualizowane", profile_page.get_page_source(), "The text <Twoje dane zostały zaktualizowane> didn't appear on profile page after editing provider data")

    def test_edit_provider_company_data_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(PROVIDER_USER3, PROVIDER_PASSWORD3)
        profile_page = home_page.header.open_profile_page()
        profile_page.edit_provider_company_data()

        Assert.contains(u"Zmiany zostały zapisane.", profile_page.get_page_source(), "The text <Zmiany zostały zapisane.> didn't appear on profile page after editing provider company data")
        Assert.contains(u"Dane na Twoim koncie oczekują na sprawdzenie przez pracownika Clicktrans.pl. Do weryfikacji danych może być potrzebne nadesłanie dokumentów potwierdzających. Powiadomimy Cię o tym e-mailem.", profile_page.get_page_source(), "The text <Dane na Twoim koncie oczekują na sprawdzenie przez pracownika Clicktrans.pl. Do weryfikacji danych może być potrzebne nadesłanie dokumentów potwierdzających. Powiadomimy Cię o tym e-mailem> disn't appear on profile page after editing provider company data")

    def test_edit_provider_notifications_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(PROVIDER_USER2, PROVIDER_PASSWORD2)
        profile_page = home_page.header.open_profile_page()
        profile_page.edit_provider_notifications()

        Assert.contains(u"Zmiany zostały zapisane.", profile_page.get_page_source(), "The text <Zmiany zostały zapisane.> didn't appear on profile page after editing provider notifications")

    def test_change_password_should_succeed(self):

        home_page = HomePage(self.driver).open_home_page()
        _saved_password = get_password("change_pass1.txt")
        account_page = home_page.header.login(CHANGE_PASSWORD_USER, _saved_password)
        profile_page = home_page.header.open_profile_page()
        profile_page.change_password("change_pass1.txt")

        Assert.contains(u"Hasło zostało zmienione.", profile_page.get_page_source(), "The text <Hasło zostało zmienione> didn't appear or profile page after changing password")

    def test_reject_offer_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), "The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
        submit_offer = view_consignments_page.open_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.reject_offer()
        sleep(3)

        Assert.contains(u"Oferta została odrzucona.", consignment.get_page_source(), "The text <Oferta została odrzucona.> didn't appear on consignment page after rejecting offer")

    def test_add_question_to_offer_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), "The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
        submit_offer = view_consignments_page.open_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.add_question_to_offer()
        consignment.show_offer_details()

        Assert.contains(u"Twoja wiadomość została dodana.", consignment.get_page_source(), "The text <Twoja wiadomość została dodana.> didn't appear on consignment page after adding question to offer")
        Assert.contains(u"This is my question", consignment.get_page_source(), "The text <This is my question> didn't appear on consignment page after adding question to offer")

    def test_provider_reply_to_question_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), "The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
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
        consignment.show_offer_details()

        Assert.contains(u"Twoja wiadomość została dodana.", consignment.get_page_source(), "The text <Twoja wiadomość została dodana.> didn't appear on consignment page after replying to question to offer")
        Assert.contains(u"This is my answer", consignment.get_page_source(), "The text <This is my answer> didn't appear on consignment page after replying to question to offer")

    def test_provider_add_question_to_consignment_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), "The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
        consignment = view_consignments_page.open_added_consignment()
        consignment.provider_add_question_to_consignment()

        Assert.contains(u"Twoje pytanie zostało dodane.", consignment.get_page_source(), "The text <Twoje pytanie zostało dodane.> didn't appear on consignment page after adding question to consignment")
        Assert.contains(u"This is my question", consignment.get_page_source(), "The text <This is my question> didn't appear on consignment page after adding question to consignment")

    def test_user_reply_to_question_to_consignment_from_provider_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), "The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
        consignment = view_consignments_page.open_added_consignment()
        consignment.provider_add_question_to_consignment()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.user_open_first_message()
        consignment.reply_to_provider_question_to_consignment()

        Assert.contains(u"Twoja odpowiedź została dodana.", consignment.get_page_source(), "The text <Twoja odpowiedź została dodana.> didn't appear on consignment page after replying to question to consignment")
        Assert.contains(u"This is my reply", consignment.get_page_source(), "The text <This is my reply> didn't appear on consignment page after replying to question to consignment")

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
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), "The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
        submit_offer = view_consignments_page.open_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.accept_offer()
        sleep(3)

        Assert.contains("Gratulacje", consignment.get_page_source(), "The text <Gratulacje> didn't appear on consignment page after accepting offer")
        Assert.contains(u"Wybrałeś ofertę Przewoźnika <b>"+PROVIDER_USER, consignment.get_page_source(), "The text <Wybrałeś ofertę Przewoźnika <b>PROVIDER_USER_NAME> didn't appear on consignment page after accepting offer")
        Assert.contains(u"Co dalej? Skontaktuj si\u0119 z Przewo\u017anikiem <b>"+PROVIDER_USER+u"</b> w celu realizacji us\u0142ugi transportowej:", consignment.get_page_source(), "The text <Co dalej? Skontaktuj si\u0119 z Przewo\u017anikiem <b>PROVIDER_USER_NAME</b> w celu realizacji us\u0142ugi transportowej:> didn't appear on consignment page after accepting offer")
        Assert.contains(u"Imi\u0119 i nazwisko:</b> "+store.name1, consignment.get_page_source(), "The text <Imi\u0119 i nazwisko:</b> STORED_NAME_FROM_PROFILE> didn't appear on consignment page after accepting offer")
        Assert.contains(u"tel.:</b> "+store.tel, consignment.get_page_source(), "The text <tel.:</b> STORED_PHONE_FORM_PROFILE> didn't appear on consignment page after accepting offer")
        Assert.contains(u"e-mail:</b> "+store.mail, consignment.get_page_source(), "The text <e-mail:</b> STORED_EMAIL_FROM_PROFILE> didn't appear on consignment page after accepting offer")
        Assert.contains(store.www, consignment.get_page_source(), "The text <STORED_WWW_FROM_PROFILE> didn't appear on consignment page after accepting offer")
        Assert.contains(store.address_table_0_splitted[0]+"  "+store.address_table_0_splitted[1], consignment.get_page_source(), "The text <STORED_PROVIDER_ADDRESS_LINE_!> didn't appear on consignment page after accepting offer")
        Assert.contains(store.address_table[1], consignment.get_page_source(), "The text <STORED_PROVIDER_ADDRESS_LINE_2> didn't appear on consignment page after accepting offer")
        Assert.contains(store.address_table[2], consignment.get_page_source(), "The text <STORED_PROVIDER_ADDRESS_LINE_3> didn't appear on consignment page after accepting offer")
        Assert.contains(u"Pobierz list przewozowy, który będzie potwierdzeniem nadania Twojej przesyłki", consignment.get_page_source(), "The text <Pobierz list przewozowy, który będzie potwierdzeniem nadania Twojej przesyłki> didn't appear on consignment page after accepting offer")
        Assert.contains(u"(Ogłoszenie nieaktualne. Użytkownik wybrał już ofertę)", consignment.get_page_source(), "The text <(Ogłoszenie nieaktualne. Użytkownik wybrał już ofertę)> didn't appear on consignment page after accepting offer")

#  PROVIDER ADDRESS TABLE[0] IS SHOWN WITH 2 SPACES, zgłoszone, ale poprawione splittem

    def test_make_offer_executed_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), "The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
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

        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(profile._executed_result_field, u"Oferta ma status zrealizowana"), "The text <Oferta ma status zrealizowana> didn't match the text in Offer executed result field in provider profile after making offer executed")

    def test_provider_send_commentary_from_my_offers_menu_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), "The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
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

        Assert.contains(u"Komentarz został wystawiony.", consignment.get_page_source(), "The text <Komentarz został wystawiony.> didn't appear on provider profile page after sending commentary form my offers menu")

    def test_reply_to_question_to_consignment_from_panel_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), "The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
        consignment = view_consignments_page.open_added_consignment()
        consignment.provider_add_question_to_consignment()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        profile.user_click_reply_to_question()

        Assert.contains(u"Napisz wiadomość i ustal z Przewoźnikiem niezbędne szczegóły. Aby transakcja była bezpieczna musisz jeszcze zaakceptować ofertę Przewoźnika.", profile.get_page_source(), "The text <Napisz wiadomość i ustal z Przewoźnikiem niezbędne szczegóły. Aby transakcja była bezpieczna musisz jeszcze zaakceptować ofertę Przewoźnika> didn't appear on user profile page ofter clicking <reply to question>")

        consignment.reply_to_provider_question_to_consignment()

        Assert.contains(u"Twoja odpowiedź została dodana.", profile.get_page_source(), "The text <Twoja odpowiedź została dodana> didn't appear on consignment page after replying to provider question to consignment")
        Assert.contains(u"This is my reply", profile.get_page_source(), "The text <This is my reply> didn't appear on consignment page after replying to provider question to consignment")

    def test_user_send_commetary_from_ended_transactions_menu_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), "The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
        submit_offer = view_consignments_page.open_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.accept_offer()
        profile = home_page.header.open_profile_page()
        profile.user_send_commentary_from_ended_transactions_menu()

        Assert.contains(u"Komentarz został wystawiony.", consignment.get_page_source(), "The text <Komentarz został wystawiony.> didn't appear on user profile page after sending commentary from ended transactions menu")

    def test_user_send_commentary_from_commentaries_menu_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), "The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
        submit_offer = view_consignments_page.open_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.accept_offer()
        profile = home_page.header.open_profile_page()
        profile.user_send_commentary_from_commentaries_menu()

        Assert.contains(u"Komentarz został wystawiony.", consignment.get_page_source(), "The text <Komentarz został wystawiony.> didn't appear on user profile page after sending commentary from commentaries menu")

    def test_provider_reply_to_negative_commentary_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), "The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
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

        Assert.contains(u"This is my negative commentary", profile.get_page_source(), "The text <This is my negative commentary> didn't appear on provider profile page after replying to negative commentary")
        Assert.contains(u"This is my reply", profile.get_page_source(), "The text <This is my reply> didn't appear on provider profile page after replying to negative commentary")

# There's no possibility to reply to negative commentary as provider, zgłoszone




    def test_provider_send_commentary_from_commentaries_menu_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), "The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
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

        Assert.contains(u"Komentarz został wystawiony.", consignment.get_page_source(), "The text <Komentarz został wystawiony.> didn't appear on provider profile page after sending commentary from commentaries menu")

        profile.enter_provider_sent_commentaries_tab()

        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(profile._provider_first_sent_commentary_field, "This is my commentary"), "The text in provider first sent commentary field in provider sent commentaries tab didn't match text <This is my commentary>")
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(profile._provider_first_sent_commentary_consignment_uuid, view_consignments_page._title_uuid), "The text in provider first sent commentary consignment title field in provider sent commentaries tab didn't match <CONSIGNMENT_TITLE>")

    def test_ask_for_offer_on_provider_page_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider_page = home_page.header.view_provider_damian_wiklina_page()
        provider_page.ask_for_offer_on_provider_page()

        Assert.contains(u"Twoja prośba o ofertę została wysłana do Przewoźnika", provider_page.get_page_source(), "THe text <Twoja prośba o ofertę została wysłana do Przewoźnika> didn't appear on provider <damian wilkina> page after asking for offer on this page")

    def test_ask_for_offer_while_adding_consignment_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        add_consignment_page.ask_for_offer_while_adding_consignment()
        sleep(2)

        Assert.contains(u"Prośba wysłana", add_consignment_page.get_page_source(), "The text <Prośba wysłana> didn't appear on add consignment page after asking for offer while adding consignment")

    def test_ask_for_offer_for_added_consignment_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        profile = home_page.header.open_profile_page()
        profile.ask_for_offer_for_added_consignment()
        sleep(4)
        Assert.contains(u"Prośba wysłana", profile.get_page_source(), "The text <Prośba wysłana> didn't appear on user profile page after asking for offer for added consignment")

    # def test_user_add_new_consignment_urgent_and_highlited_should_succeed(self):
    #     home_page = HomePage(self.driver).open_home_page()
    #     account_page = home_page.header.login(USER, PASSWORD)
    #     add_consignment_page = home_page.header.add_consignment_page()
    #     add_consignment_page.add_consignment_parcel()
    #     add_consignment_page.set_urgent()
    #     add_consignment_page.set_highlited()
    #     add_consignment_page.save_transport()
    #
    #     Assert.contains(u"Twoje ogłoszenie zostało zapisane i będzie opublikowane po dokonaniu wpłaty.", add_consignment_page.get_page_source())
    #
    #     add_consignment_page.pay_with_test_payment()
    #     # Assert.contains(strftime("%d.%m.%Y", gmtime()), add_consignment_page.get_first_payment_date())
    #
    #     add_consignment_page.get_consignment_title_from_result_page_after_payment()
    #
    #     if u"Twoja przesy\u0142ka" in add_consignment_page.get_page_source():
    #         Assert.equal(add_consignment_page.consignment_title_result_page_after_payment, add_consignment_page._title_uuid)
    #         Assert.contains(u"zosta\u0142a wystawiona! Wyr\xf3\u017cnienie og\u0142oszenia b\u0119dzie widoczne od razu po zaksi\u0119gowaniu wp\u0142aty w systemie PayU.", add_consignment_page.get_page_source())
    #     else:
    #         Assert.contains(u"Operacja przebiegła pomyślnie. Wyróżnienie Twojego ogłoszenia będzie widoczne od razu po zaksięgowaniu wpłaty w systemie PayU. Zobacz swoje ogłoszenie:", add_consignment_page.get_page_source())
    #         Assert.equal(add_consignment_page.consignment_title_result_page_after_payment, add_consignment_page._title_uuid)
    #
    # def test_user_add_new_consignment_urgent_should_succeed(self):
    #     home_page = HomePage(self.driver).open_home_page()
    #     account_page = home_page.header.login(USER, PASSWORD)
    #     add_consignment_page = home_page.header.add_consignment_page()
    #     add_consignment_page.add_consignment_parcel()
    #     add_consignment_page.set_urgent()
    #     add_consignment_page.save_transport()
    #
    #     Assert.contains(u"Twoje ogłoszenie zostało zapisane i będzie opublikowane po dokonaniu wpłaty.", add_consignment_page.get_page_source())
    #
    #     add_consignment_page.pay_with_test_payment()
    #     # Assert.contains(strftime("%d.%m.%Y", gmtime()), add_consignment_page.get_first_payment_date())
    #
    #     add_consignment_page.get_consignment_title_from_result_page_after_payment()
    #
    #     if u"Twoja przesy\u0142ka" in add_consignment_page.get_page_source():
    #         Assert.equal(add_consignment_page.consignment_title_result_page_after_payment, add_consignment_page._title_uuid)
    #         Assert.contains(u"zosta\u0142a wystawiona! Wyr\xf3\u017cnienie og\u0142oszenia b\u0119dzie widoczne od razu po zaksi\u0119gowaniu wp\u0142aty w systemie PayU.", add_consignment_page.get_page_source())
    #     else:
    #         Assert.contains(u"Operacja przebiegła pomyślnie. Wyróżnienie Twojego ogłoszenia będzie widoczne od razu po zaksięgowaniu wpłaty w systemie PayU. Zobacz swoje ogłoszenie:", add_consignment_page.get_page_source())
    #         Assert.equal(add_consignment_page.consignment_title_result_page_after_payment, add_consignment_page._title_uuid)
    #
    # def test_user_add_new_consignment_highlited_should_succeed(self):
    #     home_page = HomePage(self.driver).open_home_page()
    #     account_page = home_page.header.login(USER, PASSWORD)
    #     add_consignment_page = home_page.header.add_consignment_page()
    #     add_consignment_page.add_consignment_parcel()
    #     add_consignment_page.set_highlited()
    #     add_consignment_page.save_transport()
    #
    #     Assert.contains(u"Twoje ogłoszenie zostało zapisane i będzie opublikowane po dokonaniu wpłaty.", add_consignment_page.get_page_source())
    #
    #     add_consignment_page.pay_with_test_payment()
    #     # Assert.contains(strftime("%d.%m.%Y", gmtime()), add_consignment_page.get_first_payment_date())
    #
    #     add_consignment_page.get_consignment_title_from_result_page_after_payment()
    #
    #     if u"Twoja przesy\u0142ka" in add_consignment_page.get_page_source():
    #         Assert.equal(add_consignment_page.consignment_title_result_page_after_payment, add_consignment_page._title_uuid)
    #         Assert.contains(u"zosta\u0142a wystawiona! Wyr\xf3\u017cnienie og\u0142oszenia b\u0119dzie widoczne od razu po zaksi\u0119gowaniu wp\u0142aty w systemie PayU.", add_consignment_page.get_page_source())
    #     else:
    #         Assert.contains(u"Operacja przebiegła pomyślnie. Wyróżnienie Twojego ogłoszenia będzie widoczne od razu po zaksięgowaniu wpłaty w systemie PayU. Zobacz swoje ogłoszenie:", add_consignment_page.get_page_source())
    #         Assert.equal(add_consignment_page.consignment_title_result_page_after_payment, add_consignment_page._title_uuid)
    #
    # def test_user_login_while_adding_new_consignment_set_highlited_and_urgent_should_succeed(self):
    #     home_page = HomePage(self.driver).open_home_page()
    #     add_consignment_page = home_page.header.add_consignment_page()
    #     add_consignment_page.add_consignment_parcel()
    #     add_consignment_page.set_urgent()
    #     add_consignment_page.set_highlited()
    #     add_consignment_page.save_transport()
    #     account_page = home_page.header.login(USER, PASSWORD)
    #
    #     Assert.contains(u"Twoje ogłoszenie zostało zapisane i będzie opublikowane po dokonaniu wpłaty.", add_consignment_page.get_page_source())
    #     Assert.contains(u"Zalogowałeś się", add_consignment_page.get_page_source())
    #
    #     add_consignment_page.pay_with_test_payment()
    #     # Assert.contains(strftime("%d.%m.%Y", gmtime()), add_consignment_page.get_first_payment_date())
    #
    #     add_consignment_page.get_consignment_title_from_result_page_after_payment()
    #
    #     if u"Twoja przesy\u0142ka" in add_consignment_page.get_page_source():
    #         Assert.equal(add_consignment_page.consignment_title_result_page_after_payment, add_consignment_page._title_uuid)
    #         Assert.contains(u"zosta\u0142a wystawiona! Wyr\xf3\u017cnienie og\u0142oszenia b\u0119dzie widoczne od razu po zaksi\u0119gowaniu wp\u0142aty w systemie PayU.", add_consignment_page.get_page_source())
    #     else:
    #         Assert.contains(u"Operacja przebiegła pomyślnie. Wyróżnienie Twojego ogłoszenia będzie widoczne od razu po zaksięgowaniu wpłaty w systemie PayU. Zobacz swoje ogłoszenie:", add_consignment_page.get_page_source())
    #         Assert.equal(add_consignment_page.consignment_title_result_page_after_payment, add_consignment_page._title_uuid)
    #
    # def test_user_login_while_adding_new_consignment_set_highlited_should_succeed(self):
    #     home_page = HomePage(self.driver).open_home_page()
    #     add_consignment_page = home_page.header.add_consignment_page()
    #     add_consignment_page.add_consignment_parcel()
    #     add_consignment_page.set_highlited()
    #     add_consignment_page.save_transport()
    #     account_page = home_page.header.login(USER, PASSWORD)
    #
    #     Assert.contains(u"Twoje ogłoszenie zostało zapisane i będzie opublikowane po dokonaniu wpłaty.", add_consignment_page.get_page_source())
    #     Assert.contains(u"Zalogowałeś się", add_consignment_page.get_page_source())
    #
    #     add_consignment_page.pay_with_test_payment()
    #     # Assert.contains(strftime("%d.%m.%Y", gmtime()), add_consignment_page.get_first_payment_date())
    #
    #     add_consignment_page.get_consignment_title_from_result_page_after_payment()
    #
    #     if u"Twoja przesy\u0142ka" in add_consignment_page.get_page_source():
    #         Assert.equal(add_consignment_page.consignment_title_result_page_after_payment, add_consignment_page._title_uuid)
    #         Assert.contains(u"zosta\u0142a wystawiona! Wyr\xf3\u017cnienie og\u0142oszenia b\u0119dzie widoczne od razu po zaksi\u0119gowaniu wp\u0142aty w systemie PayU.", add_consignment_page.get_page_source())
    #     else:
    #         Assert.contains(u"Operacja przebiegła pomyślnie. Wyróżnienie Twojego ogłoszenia będzie widoczne od razu po zaksięgowaniu wpłaty w systemie PayU. Zobacz swoje ogłoszenie:", add_consignment_page.get_page_source())
    #         Assert.equal(add_consignment_page.consignment_title_result_page_after_payment, add_consignment_page._title_uuid)
    #
    # def test_user_login_while_adding_new_consignment_set_urgent_should_succeed(self):
    #     home_page = HomePage(self.driver).open_home_page()
    #     add_consignment_page = home_page.header.add_consignment_page()
    #     add_consignment_page.add_consignment_parcel()
    #     add_consignment_page.set_urgent()
    #     add_consignment_page.save_transport()
    #     account_page = home_page.header.login(USER, PASSWORD)
    #
    #     Assert.contains(u"Twoje ogłoszenie zostało zapisane i będzie opublikowane po dokonaniu wpłaty.", add_consignment_page.get_page_source())
    #     Assert.contains(u"Zalogowałeś się", add_consignment_page.get_page_source())
    #
    #     add_consignment_page.pay_with_test_payment()
    #     # Assert.contains(strftime("%d.%m.%Y", gmtime()), add_consignment_page.get_first_payment_date())
    #
    #     add_consignment_page.get_consignment_title_from_result_page_after_payment()
    #
    #     if u"Twoja przesy\u0142ka" in add_consignment_page.get_page_source():
    #         Assert.equal(add_consignment_page.consignment_title_result_page_after_payment, add_consignment_page._title_uuid)
    #         Assert.contains(u"zosta\u0142a wystawiona! Wyr\xf3\u017cnienie og\u0142oszenia b\u0119dzie widoczne od razu po zaksi\u0119gowaniu wp\u0142aty w systemie PayU.", add_consignment_page.get_page_source())
    #     else:
    #         Assert.contains(u"Operacja przebiegła pomyślnie. Wyróżnienie Twojego ogłoszenia będzie widoczne od razu po zaksięgowaniu wpłaty w systemie PayU. Zobacz swoje ogłoszenie:", add_consignment_page.get_page_source())
    #         Assert.equal(add_consignment_page.consignment_title_result_page_after_payment, add_consignment_page._title_uuid)
    #
    # def test_user_after_adding_consignment_set_highlited_and_urgent_should_succeed(self):
    #     home_page = HomePage(self.driver).open_home_page()
    #     account_page = home_page.header.login(USER, PASSWORD)
    #     add_consignment_page = home_page.header.add_consignment_page()
    #     add_consignment_page.new_furniture_consignment()
    #     profile_page = home_page.header.open_profile_page()
    #     profile_page.user_open_my_consignments_menu()
    #     profile_page.user_click_first_consignment_distinguish_button()
    #     profile_page.set_consignment_highlited_and_urgent()
    #     add_consignment_page.pay_with_test_payment()
    #
    #     add_consignment_page.get_consignment_title_from_result_page_after_payment()
    #
    #     if u"Twoja przesy\u0142ka" in add_consignment_page.get_page_source():
    #         Assert.equal(add_consignment_page.consignment_title_result_page_after_payment, add_consignment_page._title_uuid)
    #         Assert.contains(u"zosta\u0142a wystawiona! Wyr\xf3\u017cnienie og\u0142oszenia b\u0119dzie widoczne od razu po zaksi\u0119gowaniu wp\u0142aty w systemie PayU.", add_consignment_page.get_page_source())
    #     else:
    #         Assert.contains(u"Operacja przebiegła pomyślnie. Wyróżnienie Twojego ogłoszenia będzie widoczne od razu po zaksięgowaniu wpłaty w systemie PayU. Zobacz swoje ogłoszenie:", add_consignment_page.get_page_source())
    #         Assert.equal(add_consignment_page.consignment_title_result_page_after_payment, add_consignment_page._title_uuid)
    #
    # def test_user_after_adding_consignment_set_highlited_should_succeed(self):
    #     home_page = HomePage(self.driver).open_home_page()
    #     account_page = home_page.header.login(USER, PASSWORD)
    #     add_consignment_page = home_page.header.add_consignment_page()
    #     add_consignment_page.new_furniture_consignment()
    #     profile_page = home_page.header.open_profile_page()
    #     profile_page.user_open_my_consignments_menu()
    #     profile_page.user_click_first_consignment_distinguish_button()
    #     profile_page.set_consignment_highlited()
    #     add_consignment_page.pay_with_test_payment()
    #
    #     add_consignment_page.get_consignment_title_from_result_page_after_payment()
    #
    #     if u"Twoja przesy\u0142ka" in add_consignment_page.get_page_source():
    #         Assert.equal(add_consignment_page.consignment_title_result_page_after_payment, add_consignment_page._title_uuid)
    #         Assert.contains(u"zosta\u0142a wystawiona! Wyr\xf3\u017cnienie og\u0142oszenia b\u0119dzie widoczne od razu po zaksi\u0119gowaniu wp\u0142aty w systemie PayU.", add_consignment_page.get_page_source())
    #     else:
    #         Assert.contains(u"Operacja przebiegła pomyślnie. Wyróżnienie Twojego ogłoszenia będzie widoczne od razu po zaksięgowaniu wpłaty w systemie PayU. Zobacz swoje ogłoszenie:", add_consignment_page.get_page_source())
    #         Assert.equal(add_consignment_page.consignment_title_result_page_after_payment, add_consignment_page._title_uuid)
    #
    # def test_user_after_adding_consignment_set_urgent_should_succeed(self):
    #     home_page = HomePage(self.driver).open_home_page()
    #     account_page = home_page.header.login(USER, PASSWORD)
    #     add_consignment_page = home_page.header.add_consignment_page()
    #     add_consignment_page.new_furniture_consignment()
    #     profile_page = home_page.header.open_profile_page()
    #     profile_page.user_open_my_consignments_menu()
    #     profile_page.user_click_first_consignment_distinguish_button()
    #     profile_page.set_consignment_urgent()
    #     add_consignment_page.pay_with_test_payment()
    #
    #     add_consignment_page.get_consignment_title_from_result_page_after_payment()
    #
    #     if u"Twoja przesy\u0142ka" in add_consignment_page.get_page_source():
    #         Assert.equal(add_consignment_page.consignment_title_result_page_after_payment, add_consignment_page._title_uuid)
    #         Assert.contains(u"zosta\u0142a wystawiona! Wyr\xf3\u017cnienie og\u0142oszenia b\u0119dzie widoczne od razu po zaksi\u0119gowaniu wp\u0142aty w systemie PayU.", add_consignment_page.get_page_source())
    #     else:
    #         Assert.contains(u"Operacja przebiegła pomyślnie. Wyróżnienie Twojego ogłoszenia będzie widoczne od razu po zaksięgowaniu wpłaty w systemie PayU. Zobacz swoje ogłoszenie:", add_consignment_page.get_page_source())
    #         Assert.equal(add_consignment_page.consignment_title_result_page_after_payment, add_consignment_page._title_uuid)
    #
    # def test_provider_add_new_consignment_urgent_and_highlited_should_succeed(self):
    #     home_page = HomePage(self.driver).open_home_page()
    #     account_page = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
    #     add_consignment_page = home_page.header.add_consignment_page()
    #     add_consignment_page.add_consignment_parcel()
    #     add_consignment_page.set_urgent()
    #     add_consignment_page.set_highlited()
    #     add_consignment_page.save_transport()
    #
    #     Assert.contains(u"Twoja przesy\u0142ka zosta\u0142a wystawiona! Op\u0142ata za wyr\xf3\u017cnienie og\u0142oszenia zosta\u0142a doliczona do Twojego salda (zak\u0142adka Moje konto &gt; Rozliczenia).", add_consignment_page.get_page_source())
    #
    # def test_provider_add_new_consignment_highlited_should_succeed(self):
    #     home_page = HomePage(self.driver).open_home_page()
    #     account_page = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
    #     add_consignment_page = home_page.header.add_consignment_page()
    #     add_consignment_page.add_consignment_parcel()
    #     add_consignment_page.set_highlited()
    #     add_consignment_page.save_transport()
    #
    #     Assert.contains(u"Twoja przesy\u0142ka zosta\u0142a wystawiona! Op\u0142ata za wyr\xf3\u017cnienie og\u0142oszenia zosta\u0142a doliczona do Twojego salda (zak\u0142adka Moje konto &gt; Rozliczenia).", add_consignment_page.get_page_source())
    #
    # def test_provider_add_new_consignment_urgent_should_succeed(self):
    #     home_page = HomePage(self.driver).open_home_page()
    #     account_page = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
    #     add_consignment_page = home_page.header.add_consignment_page()
    #     add_consignment_page.add_consignment_parcel()
    #     add_consignment_page.set_urgent()
    #     add_consignment_page.save_transport()
    #
    #     Assert.contains(u"Twoja przesy\u0142ka zosta\u0142a wystawiona! Op\u0142ata za wyr\xf3\u017cnienie og\u0142oszenia zosta\u0142a doliczona do Twojego salda (zak\u0142adka Moje konto &gt; Rozliczenia).", add_consignment_page.get_page_source())
    #
    # def test_provider_login_while_adding_new_consignment_set_highlited_and_urgent_should_succeed(self):
    #     home_page = HomePage(self.driver).open_home_page()
    #     add_consignment_page = home_page.header.add_consignment_page()
    #     add_consignment_page.add_consignment_parcel()
    #     add_consignment_page.set_urgent()
    #     add_consignment_page.set_highlited()
    #     add_consignment_page.save_transport()
    #     account_page = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
    #
    #     Assert.contains(u"Twoja przesy\u0142ka zosta\u0142a wystawiona! Op\u0142ata za wyr\xf3\u017cnienie og\u0142oszenia zosta\u0142a doliczona do Twojego salda (zak\u0142adka Moje konto &gt; Rozliczenia).", add_consignment_page.get_page_source())
    #     Assert.contains(u"Zalogowałeś się", add_consignment_page.get_page_source())
    #
    # def test_provider_login_while_adding_new_consignment_set_highlited_should_succeed(self):
    #     home_page = HomePage(self.driver).open_home_page()
    #     add_consignment_page = home_page.header.add_consignment_page()
    #     add_consignment_page.add_consignment_parcel()
    #     add_consignment_page.set_highlited()
    #     add_consignment_page.save_transport()
    #     account_page = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
    #
    #     Assert.contains(u"Twoja przesy\u0142ka zosta\u0142a wystawiona! Op\u0142ata za wyr\xf3\u017cnienie og\u0142oszenia zosta\u0142a doliczona do Twojego salda (zak\u0142adka Moje konto &gt; Rozliczenia).", add_consignment_page.get_page_source())
    #     Assert.contains(u"Zalogowałeś się", add_consignment_page.get_page_source())
    #
    # def test_provider_login_while_adding_new_consignment_set_urgent_should_succeed(self):
    #     home_page = HomePage(self.driver).open_home_page()
    #     add_consignment_page = home_page.header.add_consignment_page()
    #     add_consignment_page.add_consignment_parcel()
    #     add_consignment_page.set_urgent()
    #     add_consignment_page.save_transport()
    #     account_page = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
    #
    #     Assert.contains(u"Twoja przesy\u0142ka zosta\u0142a wystawiona! Op\u0142ata za wyr\xf3\u017cnienie og\u0142oszenia zosta\u0142a doliczona do Twojego salda (zak\u0142adka Moje konto &gt; Rozliczenia).", add_consignment_page.get_page_source())
    #     Assert.contains(u"Zalogowałeś się", add_consignment_page.get_page_source())
    #
    # def test_provider_after_adding_consignment_set_highlited_and_urgent_should_succeed(self):
    #     home_page = HomePage(self.driver).open_home_page()
    #     account_page = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
    #     add_consignment_page = home_page.header.add_consignment_page()
    #     add_consignment_page.new_furniture_consignment()
    #     profile_page = home_page.header.open_profile_page()
    #     profile_page.provider_open_my_consignments_menu()
    #     profile_page.provider_click_first_consignment_distinguish_button()
    #     profile_page.set_consignment_highlited_and_urgent()
    #
    #     Assert.contains(u"Operacja przebiegła pomyślnie.", add_consignment_page.get_page_source())
    #
    # def test_provider_after_adding_consignment_set_highlited_should_succeed(self):
    #     home_page = HomePage(self.driver).open_home_page()
    #     account_page = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
    #     add_consignment_page = home_page.header.add_consignment_page()
    #     add_consignment_page.new_furniture_consignment()
    #     profile_page = home_page.header.open_profile_page()
    #     profile_page.provider_open_my_consignments_menu()
    #     profile_page.provider_click_first_consignment_distinguish_button()
    #     profile_page.set_consignment_highlited()
    #
    #     Assert.contains(u"Operacja przebiegła pomyślnie.", add_consignment_page.get_page_source())
    #
    # def test_provider_after_adding_consignment_set_urgent_should_succeed(self):
    #     home_page = HomePage(self.driver).open_home_page()
    #     account_page = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
    #     add_consignment_page = home_page.header.add_consignment_page()
    #     add_consignment_page.new_furniture_consignment()
    #     profile_page = home_page.header.open_profile_page()
    #     profile_page.provider_open_my_consignments_menu()
    #     profile_page.provider_click_first_consignment_distinguish_button()
    #     profile_page.set_consignment_urgent()
    #
    #     Assert.contains(u"Operacja przebiegła pomyślnie.", add_consignment_page.get_page_source())

    # def test_zz_generate_plot_and_send_email(self):
    #     self._save_plot()
    #     self._convert_to_html()
    #     self._send_email()

    def tally(self):
        return len(self._resultForDoCleanups.errors) + len(self._resultForDoCleanups.failures)

    def setUp(self):
        self.timeout = 30
        if run_locally:
            self.driver = webdriver.Firefox()
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
    #     sender = Mailer('smtp.gmail.com', use_tls=True, usr='jedrzej.wojcieszczyk@testuj.pl', pwd='paluch88')
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

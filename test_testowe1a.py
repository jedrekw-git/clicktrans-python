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

    def test_add_new_consignment_not_activated_user_should_succeed(self):
        home_page = HomePage(self.driver).open_page_testowe()
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        registeration_page = home_page.header.continue_to_registration_page()
        registeration_page.add_new_consignment_unactivated_fill_username_field()
        registeration_page.add_new_consignment_unactivated_fill_email_field()
        registeration_page.new_user_fill_data()

        Assert.contains(u"Odbierz pocztę", registeration_page.get_page_source(), u"The text <Odbierz pocztę> wasn't found on confirmastion page after entering new user data")
        Assert.contains(registeration_page._email_user_add_new_consignment, registeration_page.get_page_source(), u"The user email wasn't found on confirmastion page after entering new user data")
        Assert.contains(u'i kliknij link aktywacyjny, aby ukończyć rejestrację.', registeration_page.get_page_source(), u"The text <i kliknij link aktywacyjny, aby ukończyć rejestrację> wasn't found on confirmastion page after entering new user data")

    # def test_withdraw_consignment_should_succeed(self):
    #     home_page = HomePage(self.driver).open_page_testowe()
    #     account_page = home_page.header.login(USER, PASSWORD)
    #     add_consignment_page = home_page.header.add_consignment_page()
    #     add_consignment_page.new_furniture_consignment()
    #     WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(add_consignment_page._after_adding_consignment_text_field, u"została wystawiona!"), u"The text <została wystawiona> didn't appear on page after adding consignment, probably the consignment wasn't added")
    #     profile_page = home_page.header.open_profile_page()
    #     settings = profile_page.withdraw_consignment()
    #     sleep(3)
    #
    #     Assert.contains(u"Ogłoszenie zostało wycofane", profile_page.get_page_source(), u"The text <Ogłoszenie zostało wycofane> didn't appear on profile page after withdrawing consignment")

#CHROME

    def test_report_violation_to_question_to_offer_should_succeed(self):
        home_page = HomePage(self.driver).open_page_testowe()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(add_consignment_page._after_adding_consignment_text_field, u"została wystawiona!"), u"The text <została wystawiona> didn't appear on page after adding consignment, probably the consignment wasn't added")
        home_page.header.logout()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), u"The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
        submit_offer = view_consignments_page.open_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        home_page.header.logout()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.add_question_to_offer()
        consignment.report_violation_to_question_to_offer()

        Assert.contains(u"Zgłoszenie zostało odnotowane", consignment.get_page_source(), u"The text <Zgłoszenie zostało odnotowane> didn't appear on consignment page after reporting violation to question to offer")

# no possibility to add question to consignment

    def test_check_categories_should_succeed(self):
        home_page = HomePage(self.driver).open_page_testowe()
        account_page = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.add_consignment_parcel()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(add_consignment_page._after_adding_consignment_text_field, u"została wystawiona!"), u"The text <została wystawiona> didn't appear on page after adding consignment, probably the consignment wasn't added")
        view_consignment_page = home_page.header.view_consignments_page()
        view_consignment_page.check_categories()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(view_consignment_page._first_result_posting_province, "azowieckie"), u"The first result on view consignments page posting province didn't match posting province entered into search field")
        view_consignment_page.click_first_result()
        Assert.contains('Paczki', view_consignment_page.get_page_source(), u"The text <Paczki> didn't appear on consignment page, probably the category on view consignments page wasn't chosen")

    def test_submit_offer_should_succeed(self):
        home_page = HomePage(self.driver).open_page_testowe()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(add_consignment_page._after_adding_consignment_text_field, u"została wystawiona!"), u"The text <została wystawiona> didn't appear on page after adding consignment, probably the consignment wasn't added")
        home_page.header.logout()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), u"The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
        submit_offer = view_consignments_page.open_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()

        Assert.contains(u"Oferta została złożona", submit_offer.get_page_source(), u"The text <Oferta została złożona> didn't appear on consignment page after submitting offer, probably offer wasn't submitted")

    # def test_issue_consignment_again_should_succeed(self):
    #     home_page = HomePage(self.driver).open_page_testowe()
    #     account_page = home_page.header.login(USER, PASSWORD)
    #     add_consignment_page = home_page.header.add_consignment_page()
    #     add_consignment_page.new_furniture_consignment()
    #     WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(add_consignment_page._after_adding_consignment_text_field, u"została wystawiona!"), u"The text <została wystawiona> didn't appear on page after adding consignment, probably the consignment wasn't added")
    #     profile_page = home_page.header.open_profile_page()
    #     settings = profile_page.withdraw_consignment()
    #     profile = home_page.header.open_profile_page()
    #     edit_settings = profile.issue_consignment_again()
    #     edit_settings.edit_consignment_cars()
    #
    #     WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element(edit_settings._edit_consignment_result_field, u"Twoja przesyłka"), u"The text <Twoja przesyłka> didn't appear on confirmation page after editing consignment, probably the edit didn't work well")
    #     # Assert.contains(u"Twoja przesyłka", edit_settings.get_page_source(), u"The text <Twoja przesyłka> didn't appear on confirmation page after editing consignment, probably the edit didn't work well")
    #     Assert.contains(edit_settings._title_uuid, profile_page.get_page_source(), u"The edited consignment title didn't appear on confirmation page after editing consignment, probably the edit didn't work well")
    #     Assert.contains(u"została wystawiona!", edit_settings.get_page_source(), u"The text <została wystawiona!> didn't appear on confirmation page after editing consignment, probably the edit didn't work well")
    #
    #     edit_settings.view_added_consignment()
    #
    #     Assert.contains(edit_settings._title_uuid, edit_settings.get_page_source(), u"The edited consignment title didn't appear on consignment page after editing consignment")
    #     Assert.contains(u"Katowice, Polska", edit_settings.get_page_source(), u"The text <Katowice, Polska> didn't appear on consignment page after editing consignment")
    #     Assert.contains(u'Poznań, Polska', edit_settings.get_page_source(), u"The text <Poznań, Polska> didn't appear on consignment page after editing consignment")
    #     Assert.contains(u'409.00  km', edit_settings.get_page_source(), u"The text <409.00  km> didn't appear on consignment page after editing consignment, probably the distance between cities has changed")
    #     Assert.contains(u'This is my additional info after edit', edit_settings.get_page_source(), u"The text <This is my additional info after edit> didn't appear on consignment page after editing consignment")

    # CHROME, WITHDRAW NIE DZIAŁA

    def test_commission_payback_should_succeed(self):
        home_page = HomePage(self.driver).open_page_testowe()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(add_consignment_page._after_adding_consignment_text_field, u"została wystawiona!"), u"The text <została wystawiona> didn't appear on page after adding consignment, probably the consignment wasn't added")
        home_page.header.logout()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), u"The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
        submit_offer = view_consignments_page.open_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        home_page.header.logout()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.accept_offer()
        home_page.header.logout()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        profile = home_page.header.open_profile_page()
        profile.payback_commission()

        Assert.contains(u"Wniosek został wysłany do rozpatrzenia. O wyniku zostaniesz poinformowany mailem.", profile.get_page_source(), u"The text <Wniosek został wysłany do rozpatrzenia. O wyniku zostaniesz poinformowany mailem.> didn't appear on profile page after making payback commission")

    def test_edit_provider_profile_should_succeed(self):
        home_page = HomePage(self.driver).open_page_testowe()
        account_page = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        profile_page = home_page.header.open_profile_page()
        profile_page.edit_provider_profile()
        sleep(2)

        Assert.contains(u"Zmiany zostały zapisane.", profile_page.get_page_source(), u"The text <Zmiany zostały zapisane.> didn't appear on profile page after editing provider profile")
        Assert.equal(profile_page._route_from_value, profile_page.get_value(profile_page._route_from_field), u"The edited route <From> value didn't appear on profile page after editing provider profile")
        Assert.equal(profile_page._route_to_value, profile_page.get_value(profile_page._route_to_field), u"The edited route <To> value didn't appear on profile page after editing provider profile")

    def test_edit_provider_company_data_should_succeed(self):
        home_page = HomePage(self.driver).open_page_testowe()
        account_page = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        profile_page = home_page.header.open_profile_page()
        profile_page.edit_provider_company_data()

        Assert.contains(u"Zmiany zostały zapisane.", profile_page.get_page_source(), u"The text <Zmiany zostały zapisane.> didn't appear on profile page after editing provider company data")
        # WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(profile_page._changes_saved_field, u"Zmiany zostały zapisane."), u"The text <Zmiany zostały zapisane.> didn't appear on profile page after editing provider company data")
        Assert.contains(u"Dane na Twoim koncie oczekują na sprawdzenie przez pracownika Clicktrans.pl. Do weryfikacji danych może być potrzebne nadesłanie dokumentów potwierdzających. Powiadomimy Cię o tym e-mailem.", profile_page.get_page_source(), u"The text <Dane na Twoim koncie oczekują na sprawdzenie przez pracownika Clicktrans.pl. Do weryfikacji danych może być potrzebne nadesłanie dokumentów potwierdzających. Powiadomimy Cię o tym e-mailem> disn't appear on profile page after editing provider company data")

    def test_provider_reply_to_question_should_succeed(self):
        home_page = HomePage(self.driver).open_page_testowe()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(add_consignment_page._after_adding_consignment_text_field, u"została wystawiona!"), u"The text <została wystawiona> didn't appear on page after adding consignment, probably the consignment wasn't added")
        home_page.header.logout()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), u"The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
        submit_offer = view_consignments_page.open_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        home_page.header.logout()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.add_question_to_offer()
        home_page.header.logout()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_message()
        consignment.reply_to_question()
        consignment.show_offer_details()

        Assert.contains(u"Twoja wiadomość została dodana.", consignment.get_page_source(), u"The text <Twoja wiadomość została dodana.> didn't appear on consignment page after replying to question to offer")
        Assert.contains(u"This is my answer", consignment.get_page_source(), u"The text <This is my answer> didn't appear on consignment page after replying to question to offer")

    def test_provider_add_question_to_consignment_should_succeed(self):
        home_page = HomePage(self.driver).open_page_testowe()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(add_consignment_page._after_adding_consignment_text_field, u"została wystawiona!"), u"The text <została wystawiona> didn't appear on page after adding consignment, probably the consignment wasn't added")
        home_page.header.logout()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), u"The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
        consignment = view_consignments_page.open_added_consignment()
        consignment.provider_add_question_to_consignment()

        Assert.contains(u"Twoje pytanie zostało dodane.", consignment.get_page_source(), u"The text <Twoje pytanie zostało dodane.> didn't appear on consignment page after adding question to consignment")
        Assert.contains(u"This is my question", consignment.get_page_source(), u"The text <This is my question> didn't appear on consignment page after adding question to consignment")

#brak mozliwosci dodania pytania do przesyłki

    def test_accept_offer_should_succeed(self):
        home_page = HomePage(self.driver).open_page_testowe()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(add_consignment_page._after_adding_consignment_text_field, u"została wystawiona!"), u"The text <została wystawiona> didn't appear on page after adding consignment, probably the consignment wasn't added")
        home_page.header.logout()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        store = home_page.header.open_profile_page()
        store.store_provider_data()
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), u"The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
        submit_offer = view_consignments_page.open_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        home_page.header.logout()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.accept_offer()
        sleep(3)

        Assert.contains("Gratulacje", consignment.get_page_source(), u"The text <Gratulacje> didn't appear on consignment page after accepting offer")
        Assert.contains(u"Wybrałeś ofertę Przewoźnika <b>"+PROVIDER_USER, consignment.get_page_source(), u"The text <Wybrałeś ofertę Przewoźnika <b>PROVIDER_USER_NAME> didn't appear on consignment page after accepting offer")
        Assert.contains(u"Co dalej? Skontaktuj si\u0119 z Przewo\u017anikiem <b>"+PROVIDER_USER+u"</b> w celu realizacji us\u0142ugi transportowej:", consignment.get_page_source(), u"The text <Co dalej? Skontaktuj si\u0119 z Przewo\u017anikiem <b>PROVIDER_USER_NAME</b> w celu realizacji us\u0142ugi transportowej:> didn't appear on consignment page after accepting offer")
        Assert.contains(u"Imi\u0119 i nazwisko:</b> "+store.name1, consignment.get_page_source(), u"The text <Imi\u0119 i nazwisko:</b> STORED_NAME_FROM_PROFILE> didn't appear on consignment page after accepting offer")
        Assert.contains(u"tel.:</b> "+store.tel, consignment.get_page_source(), u"The text <tel.:</b> STORED_PHONE_FORM_PROFILE> didn't appear on consignment page after accepting offer")
        Assert.contains(u"e-mail:</b> "+store.mail, consignment.get_page_source(), u"The text <e-mail:</b> STORED_EMAIL_FROM_PROFILE> didn't appear on consignment page after accepting offer")
        Assert.contains(store.www, consignment.get_page_source(), u"The text <STORED_WWW_FROM_PROFILE> didn't appear on consignment page after accepting offer")
        # Assert.contains(store.address_table_0_splitted[0]+" "+store.address_table_0_splitted[1], consignment.get_page_source(), u"The text <STORED_PROVIDER_ADDRESS_LINE_!> didn't appear on consignment page after accepting offer")
        Assert.contains(store.address_table[0], consignment.get_page_source(), u"The text <STORED_PROVIDER_ADDRESS_LINE_!> didn't appear on consignment page after accepting offer")
        Assert.contains(store.address_table[1], consignment.get_page_source(), u"The text <STORED_PROVIDER_ADDRESS_LINE_2> didn't appear on consignment page after accepting offer")
        Assert.contains(store.address_table[2], consignment.get_page_source(), u"The text <STORED_PROVIDER_ADDRESS_LINE_3> didn't appear on consignment page after accepting offer")
        Assert.contains(u"Pobierz list przewozowy, który będzie potwierdzeniem nadania Twojej przesyłki", consignment.get_page_source(), u"The text <Pobierz list przewozowy, który będzie potwierdzeniem nadania Twojej przesyłki> didn't appear on consignment page after accepting offer")
        Assert.contains(u"(Ogłoszenie nieaktualne. Użytkownik wybrał już ofertę)", consignment.get_page_source(), u"The text <(Ogłoszenie nieaktualne. Użytkownik wybrał już ofertę)> didn't appear on consignment page after accepting offer")

#  PROVIDER ADDRESS TABLE[0] IS SHOWN WITH 2 SPACES, zgłoszone, ale poprawione splittem

    def test_make_offer_executed_should_succeed(self):
        home_page = HomePage(self.driver).open_page_testowe()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(add_consignment_page._after_adding_consignment_text_field, u"została wystawiona!"), u"The text <została wystawiona> didn't appear on page after adding consignment, probably the consignment wasn't added")
        home_page.header.logout()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), u"The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
        submit_offer = view_consignments_page.open_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        home_page.header.logout()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.accept_offer()
        home_page.header.logout()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        profile = home_page.header.open_profile_page()
        profile.make_offer_executed()

        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(profile._executed_result_field, u"Oferta ma status zrealizowana"), u"The text <Oferta ma status zrealizowana> didn't match the text in Offer executed result field in provider profile after making offer executed")

    # def test_provider_send_commentary_from_my_offers_menu_should_succeed(self):
    #     home_page = HomePage(self.driver).open_page_testowe()
    #     user = home_page.header.login(USER, PASSWORD)
    #     add_consignment_page = home_page.header.add_consignment_page()
    #     add_consignment_page.new_furniture_consignment()
    #     WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(add_consignment_page._after_adding_consignment_text_field, u"została wystawiona!"), u"The text <została wystawiona> didn't appear on page after adding consignment, probably the consignment wasn't added")
    #     home_page.header.logout()
    #     provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
    #     view_consignments_page = home_page.header.view_consignments_page()
    #     view_consignments_page.search_for_added_consignment()
    #     WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), u"The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
    #     submit_offer = view_consignments_page.open_added_consignment()
    #     submit_offer.submit_offer()
    #     submit_offer.confirm_submit_offer()
    #     home_page.header.logout()
    #     user = home_page.header.login(USER, PASSWORD)
    #     profile = home_page.header.open_profile_page()
    #     consignment = profile.open_first_auction()
    #     consignment.accept_offer()
    #     home_page.header.logout()
    #     provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
    #     profile = home_page.header.open_profile_page()
    #     profile.provider_send_commentary_from_my_offers_menu()
    #
    #     Assert.contains(u"Komentarz został wystawiony.", consignment.get_page_source(), u"The text <Komentarz został wystawiony.> didn't appear on provider profile page after sending commentary form my offers menu")

# chrome

    # def test_user_send_commentary_from_ended_transactions_menu_should_succeed(self):
    #     home_page = HomePage(self.driver).open_page_testowe()
    #     user = home_page.header.login(USER, PASSWORD)
    #     add_consignment_page = home_page.header.add_consignment_page()
    #     add_consignment_page.new_furniture_consignment()
    #     WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(add_consignment_page._after_adding_consignment_text_field, u"została wystawiona!"), u"The text <została wystawiona> didn't appear on page after adding consignment, probably the consignment wasn't added")
    #     home_page.header.logout()
    #     provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
    #     view_consignments_page = home_page.header.view_consignments_page()
    #     view_consignments_page.search_for_added_consignment()
    #     WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), u"The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
    #     submit_offer = view_consignments_page.open_added_consignment()
    #     submit_offer.submit_offer()
    #     submit_offer.confirm_submit_offer()
    #     home_page.header.logout()
    #     user = home_page.header.login(USER, PASSWORD)
    #     profile = home_page.header.open_profile_page()
    #     consignment = profile.open_first_auction()
    #     consignment.accept_offer()
    #     profile = home_page.header.open_profile_page()
    #     profile.user_send_commentary_from_ended_transactions_menu()
    #
    #     Assert.contains(u"Komentarz został wystawiony.", consignment.get_page_source(), u"The text <Komentarz został wystawiony.> didn't appear on user profile page after sending commentary from ended transactions menu")

# chrome


    # def test_user_send_commentary_from_commentaries_menu_should_succeed(self):
    #     home_page = HomePage(self.driver).open_page_testowe()
    #     user = home_page.header.login(USER, PASSWORD)
    #     add_consignment_page = home_page.header.add_consignment_page()
    #     add_consignment_page.new_furniture_consignment()
    #     WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(add_consignment_page._after_adding_consignment_text_field, u"została wystawiona!"), u"The text <została wystawiona> didn't appear on page after adding consignment, probably the consignment wasn't added")
    #     home_page.header.logout()
    #     provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
    #     view_consignments_page = home_page.header.view_consignments_page()
    #     view_consignments_page.search_for_added_consignment()
    #     WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), u"The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
    #     submit_offer = view_consignments_page.open_added_consignment()
    #     submit_offer.submit_offer()
    #     submit_offer.confirm_submit_offer()
    #     home_page.header.logout()
    #     user = home_page.header.login(USER, PASSWORD)
    #     profile = home_page.header.open_profile_page()
    #     consignment = profile.open_first_auction()
    #     consignment.accept_offer()
    #     profile = home_page.header.open_profile_page()
    #     profile.user_send_commentary_from_commentaries_menu()
    #
    #     Assert.contains(u"Komentarz został wystawiony.", consignment.get_page_source(), u"The text <Komentarz został wystawiony.> didn't appear on user profile page after sending commentary from commentaries menu")

# chrome


    # def test_provider_reply_to_negative_commentary_should_succeed(self):
    #     home_page = HomePage(self.driver).open_page_testowe()
    #     user = home_page.header.login(USER, PASSWORD)
    #     add_consignment_page = home_page.header.add_consignment_page()
    #     add_consignment_page.new_furniture_consignment()
    #     WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(add_consignment_page._after_adding_consignment_text_field, u"została wystawiona!"), u"The text <została wystawiona> didn't appear on page after adding consignment, probably the consignment wasn't added")
    #     home_page.header.logout()
    #     provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
    #     view_consignments_page = home_page.header.view_consignments_page()
    #     view_consignments_page.search_for_added_consignment()
    #     WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), u"The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
    #     submit_offer = view_consignments_page.open_added_consignment()
    #     submit_offer.submit_offer()
    #     submit_offer.confirm_submit_offer()
    #     home_page.header.logout()
    #     user = home_page.header.login(USER, PASSWORD)
    #     profile = home_page.header.open_profile_page()
    #     consignment = profile.open_first_auction()
    #     consignment.accept_offer()
    #     profile = home_page.header.open_profile_page()
    #     profile.user_send_negative_commentary()
    #     home_page.header.logout()
    #     provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
    #     profile = home_page.header.open_profile_page()
    #     profile.provider_reply_to_negative_commentary()
    #
    #     Assert.contains(u"This is my negative commentary", profile.get_page_source(), u"The text <This is my negative commentary> didn't appear on provider profile page after replying to negative commentary")
    #     Assert.contains(u"This is my reply", profile.get_page_source(), u"The text <This is my reply> didn't appear on provider profile page after replying to negative commentary")

# There's no possibility to reply to negative commentary as provider, zgłoszone
#chrome



    # def test_provider_send_commentary_from_commentaries_menu_should_succeed(self):
    #     home_page = HomePage(self.driver).open_page_testowe()
    #     user = home_page.header.login(USER, PASSWORD)
    #     add_consignment_page = home_page.header.add_consignment_page()
    #     add_consignment_page.new_furniture_consignment()
    #     WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(add_consignment_page._after_adding_consignment_text_field, u"została wystawiona!"), u"The text <została wystawiona> didn't appear on page after adding consignment, probably the consignment wasn't added")
    #     home_page.header.logout()
    #     provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
    #     view_consignments_page = home_page.header.view_consignments_page()
    #     view_consignments_page.search_for_added_consignment()
    #     WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), u"The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
    #     submit_offer = view_consignments_page.open_added_consignment()
    #     submit_offer.submit_offer()
    #     submit_offer.confirm_submit_offer()
    #     home_page.header.logout()
    #     user = home_page.header.login(USER, PASSWORD)
    #     profile = home_page.header.open_profile_page()
    #     consignment = profile.open_first_auction()
    #     consignment.accept_offer()
    #     home_page.header.logout()
    #     provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
    #     profile = home_page.header.open_profile_page()
    #     profile.provider_send_commentary_from_commentaries_menu()
    #
    #     Assert.contains(u"Komentarz został wystawiony.", consignment.get_page_source(), u"The text <Komentarz został wystawiony.> didn't appear on provider profile page after sending commentary from commentaries menu")
    #
    #     profile.enter_provider_sent_commentaries_tab()
    #
    #     WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(profile._provider_first_sent_commentary_field, "This is my commentary"), u"The text in provider first sent commentary field in provider sent commentaries tab didn't match text <This is my commentary>")
    #     WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(profile._provider_first_sent_commentary_consignment_uuid, view_consignments_page._title_uuid), u"The text in provider first sent commentary consignment title field in provider sent commentaries tab didn't match <CONSIGNMENT_TITLE>")

# chrome


    def test_ask_for_offer_while_adding_consignment_should_succeed(self):
        home_page = HomePage(self.driver).open_page_testowe()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(add_consignment_page._after_adding_consignment_text_field, u"została wystawiona!"), u"The text <została wystawiona> didn't appear on page after adding consignment, probably the consignment wasn't added")
        add_consignment_page.ask_for_offer_while_adding_consignment()
        sleep(2)

        Assert.contains(u"Prośba wysłana", add_consignment_page.get_page_source(), u"The text <Prośba wysłana> didn't appear on add consignment page after asking for offer while adding consignment")

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
        text_file.write("<br><br>Wykres statystyczny: <img src=""http://ci.testuj.pl/job/Clicktrans3testowe/ws/screendumps/"+self._saved_filename_plot+".png>")
        text_file.close()

    def take_screenshot(self):
        filename = self._get_filename() + ".png"
        print "\n{method} Screenshot and HTML:\n".format(
            method=self._testMethodName)
        print 'screenshot:', filename
        self.driver.get_screenshot_as_file(filename)
        text_file = open("Clicktrans3RaportScreeny.txt", "a")
        text_file.write("<br><br>{method} Screenshot and HTML:<br>".format(
            method=self._testMethodName)+"<br>Screenshot: <a href=""http://ci.testuj.pl/job/Clicktrans3testowe/ws/screendumps/"+self._saved_filename+".png>"+self._saved_filename+"</a>")
        text_file.close()

    def dump_html(self):
        filename = self._get_filename() + '.html'
        print 'page HTML:', filename
        with open(filename, 'w') as f:
            f.write(self.driver.page_source.encode('utf-8'))
        text_file = open("Clicktrans3RaportScreeny.txt", "a")
        text_file.write("<br>Html: <a href=""http://ci.testuj.pl/job/Clicktrans3testowe/ws/screendumps/"+self._saved_filename+".html>"+self._saved_filename+"</a>")
        text_file.close()

    def _send_email(self):
        from mailer import Mailer
        from mailer import Message

        message = Message(From="jedrzej.wojcieszczyk@testuj.pl",
                          To=["jedrzej.wojcieszczyk@testuj.pl"])
        message.Subject = "Raport Clicktrans3 Testowe Testy Automatyczne Jenkins"
        message.Html = """<head><meta http-equiv="Content-Type" content="text/html;charset=UTF-8"></head><p>Cześć!<br>
           Oto wygenerowany automatycznie raport z testów Clicktrans 3 Testowe<br><br>
           Tabela raportowa z logami wykonanych testów, a pod nią linki do screenshotów i kodu html testów które nie przeszły oraz wykres statystyczny:  <a href="http://ci.testuj.pl/job/Clicktrans3testowe/ws/Clicktrans3testoweReportLogi.html">Tabela z logami, screenshoty i wykres</a></p>"""

        sender = Mailer('smtp.gmail.com', use_tls=True, usr='maildoklientow@gmail.com', pwd='useme1988')
        sender.send(message)

open("Clicktrans3RaportScreeny.txt", 'w').close()
suite = unittest.TestLoader().loadTestsFromTestCase(SmokeTest)
outfile = open("Clicktrans3testoweReportLogi.html", "wb")
runner = HTMLTestRunner(stream=outfile, title='Test Report', description='Clicktrans3 Testowe', verbosity=2)
runner.run(suite)

     # htmltestrunner.main()
     # unittest.main()
     # import xmlrunner
     # unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
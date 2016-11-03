# coding=utf-8
import re
from change_password import *
from pages.add_consignment import AddConsignmentPage
from pages.base import BasePage
from pages.consignment_page import ConsignmentPage
from selenium.webdriver.common.by import By
from time import sleep
from utils.config import *
from utils.utils import *
from selenium.common.exceptions import TimeoutException



class ProfilePage(BasePage):
    _title = "Profile"

    _edit_profile_button = (By.XPATH, "//a[6]/h4")
    _name_field = (By.ID, "user_edit_name")
    _change_name = get_random_string(8)
    _email_field = (By.ID, "user_edit_email")
    _change_email = "jedrek"+get_random_integer(4)+"@migmail.pl"
    _repeat_email_field = (By.ID, "repeat_guest_user_email")
    _language_dropdown = (By.CSS_SELECTOR, "input.search")
    _language_polish = (By.XPATH, "//div[4]/div/div[2]/div")
    _country_dropdown = (By.XPATH, "//div[6]/div/input")
    _random_country_button = (By.XPATH, "//div[%s]" %randint(10,253))
    _city_field = (By.ID, "user_edit_address_city")
    _change_city = get_random_string(7)
    _postal_code_field = (By.ID, "user_edit_address_postalCode")
    _change_postal_code = get_random_integer(2)+"-"+get_random_integer(3)
    _street_field = (By.ID, "user_edit_address_street")
    _change_street = get_random_string(8)
    _building_number_field = (By.ID, "user_edit_address_buildingNr")
    _change_building_number = get_random_integer(2)
    _phone_field = (By.ID, "user_edit_phone")
    _change_phone = get_random_integer(9)
    _save_button = (By.ID, "user_edit_submit")
    _company_data_save_button = (By.ID, "company_details_submit")
    _my_data_tab = (By.XPATH, "//div[2]/div/a[2]")
    _company_data_tab = (By.XPATH, "//div[2]/div/a[3]")
    _notification_settings_tab = (By.LINK_TEXT, "Ustawienia powiadomień")
    _change_password_tab = (By.LINK_TEXT, "Zmiana hasła")
    _company_mobile = (By.ID, "company_details_phone")
    _company_name = (By.ID, "company_details_name")
    _company_krs = (By.ID, "company_details_companyNumber")
    _company_nip = (By.ID, "company_details_taxNumber")
    _company_regon = (By.ID, "company_regon")
    _company_country_dropdown = (By.XPATH, "//div[6]/div/input")
    _random_company_country_button = (By.XPATH, "//div[%s]"%randint(10,253))
    _company_city = (By.ID, "company_details_address_city")
    _company_postal = (By.ID, "company_details_address_postalCode")
    _company_street = (By.ID, "company_details_address_street")
    _company_building = (By.ID, "company_details_address_buildingNr")
    _company_www = (By.ID, "company_details_website")
    _company_description = (By.ID, "company_description")
    _random_notification_period_radio = (By.XPATH, "//div[%s]/div/label"%randint(2,6))
    _notification_category_custom_radio = (By.XPATH, "//div[2]/div/div/div/label")
    _notification_category_dropdown = (By.XPATH, "//div/div/div[2]/div[2]/div/div")
    _remove_first_notification_category_button = (By.XPATH, "//div[2]/div/div/a/i")
    _random_notification_category = (By.XPATH, "//div[2]/div[%s]"%randint(3,9))
    _notifications_countries_custom_radio = (By.XPATH, "//div[3]/div/div/div/label")
    _remove_first_country_button = (By.XPATH, "//div[3]/div[2]/div/div/a/i")
    _notifications_countries_custom_dropdown = (By.XPATH, "//div[3]/div[2]/div/div")
    _random_notifications_countries_custom_button = (By.XPATH, "//div[%s]"%randint(12,234))
    _save_notifications_button = (By.XPATH, "//button")
    _change_password_old_field = (By.ID, "guest_user_oldpassword")
    _change_password_new_field = (By.ID, "guest_user_password")
    _change_password_new2_field = (By.ID, "repeat_guest_user_password")
    _change_password_submit = (By.XPATH, "//input[@value='Zapisz zmiany']")
    _my_consignments_menu = (By.XPATH, "//a[3]/h4")
    _ended_transactions_tab = (By.LINK_TEXT, "Zakończone transakcją")
    _first_ended_transaction_send_commentary_button = (By.XPATH, "/html/body/div[1]/div[3]/div[4]/div[4]/div[1]/div[2]/div[1]/table/tbody/tr[2]/td[4]/a[2]")
    _first_ended_transaction_commentary_content = (By.XPATH, "//textarea[@id='content_mess']")
    _first_ended_transaction_submit_commentary_button = (By.XPATH, "(//input[@value='OK'])[2]")
    _commentaries_menu = (By.XPATH, "/html/body/div[1]/div[3]/div[4]/div[1]/div/ul/li[5]/a")
    _first_transaction_send_commentary_button = (By.XPATH, "//td[4]/a")
    _first_transaction_commentary_content = (By.XPATH, "//textarea[@id='content_mess']")
    _first_transaction_submit_commentary_button = (By.XPATH, "(//input[@value='OK'])[3]")
    _first_transaction_commentary_mark_dropdown = (By.NAME, "mark")
    _provider_commentaries_menu = (By.XPATH, "//li[7]/a")
    _provider_received_commentaries_tab = (By.LINK_TEXT, "Otrzymane")
    _provider_reply_to_negative_commentary_button = (By.XPATH, "//td[5]/a")
    _provider_reply_to_negative_commentary_content = (By.XPATH, "//textarea[@id='content']")
    _provider_reply_to_negative_commentary_submit_button = (By.XPATH, "(//input[@value='OK'])[3]")
    _provider_send_commentary_button = (By.XPATH, "//td[4]/a")
    _provider_send_commentary_content = (By.XPATH, "//textarea[@id='content_mess']")
    _provider_send_commentary_submit_button = (By.XPATH, "(//input[@value='OK'])[3]")
    _first_consignment_edit = (By.XPATH, "/html/body/div[8]/div[5]/div[2]/div[2]/table/tbody/tr[1]/td[5]/div/div[2]/a")
    _first_consignment_withdraw = (By.XPATH, "//div[3]/a")
    _random_withdraw_cause = (By.XPATH, "//div[%s]/div/label"%randint(2,5))
    _withdraw_consignment_submit = (By.ID, "RejectAuction_reject")
    _first_consignment_enter = (By.XPATH, "//td/a")
    _withdraw_first_offer = (By.XPATH, "//div[3]/a")
    _withdraw_first_offer_confirm = (By.XPATH, "//div[2]/div/div[2]/a")
    _unactual_tab = (By.PARTIAL_LINK_TEXT, u"Nieaktualne")
    _my_offers_menu = (By.PARTIAL_LINK_TEXT, "Moje oferty")
    _first_consignment_issue_again = (By.XPATH, "//td[4]/div/div[2]/a")
    _accepted_tab = (By.PARTIAL_LINK_TEXT, "Zaakceptowane")
    _my_offers_send_commentary_button = (By.PARTIAL_LINK_TEXT, u"Wystaw komentarz")
    _my_offers_commentary_content = (By.ID, "user_opinion_content")
    _my_offers_commentary_submit_button = (By.XPATH, "//div[3]/div[2]")
    _random_commentary_type_button = (By.XPATH, "//form/div/div/div[2]/div[%s]"%randint(1,3))
    _set_executed_link = (By.PARTIAL_LINK_TEXT, "Ustaw jako ZREALIZOWANA")
    _set_executed_submit = (By.XPATH, "//div[2]/div/div[2]/a")
    _commission_payback_tab = (By.PARTIAL_LINK_TEXT, u"Zwroty prowizji")
    _commission_payback_request_link = (By.XPATH, "//td[6]/div/div[2]/a")
    _commission_reason_field = (By.ID, "AddRefund_descriptionCompany")
    _commission_confirmation_button = (By.XPATH, "//div[2]/div[3]/div")
    # _messages_menu = (By.XPATH, "//div[6]/div/div/ul/li[2]/a")
    _messages_menu = (By.PARTIAL_LINK_TEXT, u"Wiadomości")
    _first_message = (By.XPATH, "//td[2]/a")
    _provider_profile_button = (By.XPATH, "//a[8]/h4")
    _remove_first_category_button = (By.XPATH, "//div[2]/div/div/a/i")
    _random_category_button = (By.XPATH, "//div[2]/div[%s]" %randint(3,9))
    _category_dropdown = (By.XPATH, "//form/div[2]/div/div")
    _remove_first_route_button = (By.XPATH, "//div[4]/a")
    _add_route_button = (By.LINK_TEXT, u"Dodaj trasę")
    _route_from_field = (By.XPATH, "//div[4]/div/div/div/div/input")
    _route_from_value = "Warszawa, Polska"
    _route_to_field = (By.XPATH, "//div[2]/div/input")
    _route_to_value = "Katowice, Polska"
    _add_route_both_sides_checkbox = (By.XPATH, "//label")
    _remove_first_country_button = (By.XPATH, "//div[6]/div/div/a/i")
    _country_dropdown = (By.XPATH, "//form/div[6]/div/div")
    _random_country_button = (By.XPATH, "//div[%s]" %randint(12,234))
    _remove_first_car_button = (By.XPATH, "//div[7]/div/div/div[4]/a")
    _add_car_button = (By.LINK_TEXT, "Dodaj pojazd")
    _first_car_type_dropdown = (By.XPATH, "//form/div[7]/div/div/div/div")
    _random_first_car_type_button = (By.XPATH, "//div/div/div/div/div[2]/div[%s]"%randint(2,16))
    _first_car_capacity_dropdown = (By.XPATH, "//div[7]/div/div/div[2]/div/div")
    _random_first_car_capacity_button = (By.XPATH, "//div[2]/div/div[2]/div[%s]"%randint(2,7))
    _first_car_number_field = (By.XPATH, "//div[3]/input")
    _first_car_number_value = randint(1,4)
    _second_car_type_dropdown = (By.XPATH, "//div[7]/div/div[2]/div/div")
    _random_second_car_type_button = (By.XPATH, "//div/div[2]/div/div/div[2]/div[%s]"%randint(2,16))
    _second_car_capacity_dropdown = (By.XPATH, "//div[7]/div/div[2]/div[2]/div")
    _random_second_car_capacity_button = (By.XPATH, "//div[2]/div[2]/div/div[2]/div[%s]"%randint(2,7))
    _second_car_number_field = (By.XPATH, "//div[2]/div[3]/input")
    _second_car_number_value = randint(1,4)
    _company_description_field = (By.XPATH, "//textarea")
    _company_description_value = get_random_string(10)+" "+get_random_string(7)+" "+get_random_string(9)
    _random_transport_profile = (By.XPATH, "//div[%s]/div/label"%randint(2,8))
    _company_kind_dropdown = (By.XPATH, "//form/div[9]/div[3]/div")
    _random_company_kind_button = (By.XPATH, "//div[3]/div/div[2]/div[%s]"%randint(2,9))
    _remove_first_accepted_form_of_payment_button = (By.XPATH, "//div[4]/div/a/i")
    _accepted_form_of_payment_dropodown = (By.XPATH, "//form/div[9]/div[4]/div")
    _random_accepted_form_of_payment_button = (By.XPATH, "//div[4]/div/div[2]/div[%s]"%randint(2,6))
    _issue_VAT_invoices_dropdown = (By.XPATH, "//form/div[9]/div[5]/div")
    _random_issue_VAT_invoices_button = (By.XPATH, "//div[5]/div/div[2]/div[%s]"%randint(1,2))
    _issue_VAT_NP_invoices_dropdown = (By.XPATH, "//form/div[9]/div[6]/div")
    _random_issue_VAT_NP_invoices_button = (By.XPATH, "//div[6]/div/div[2]/div[%s]"%randint(1,2))
    _employee_number_field = (By.ID, "company_profile_employees")
    _driver_number_field = (By.ID, "company_profile_drivers")
    _company_creation_year_field = (By.ID, "company_profile_establishedYear")
    _company_creation_year_value = randint(1988, 2015)
    _save_changes = (By.ID, "company_profile_submit")
    _user_messages_menu = (By.XPATH, "//a[2]/h4")
    _user_first_message = (By.XPATH, "//td[2]/a")
    _user_first_link_reply_to_question = (By.XPATH, "/html/body/div[1]/div[3]/div[4]/div[3]/div[1]/div[2]/div[1]/table/tbody/tr[2]/td[5]/a")
    _provider_data_saved_name = (By.XPATH, "//td[2]")
    _provider_data_saved_tel = (By.XPATH, "//tr[3]/td[2]")
    _provider_data_saved_kom = (By.ID, "user_edit_phone")
    _provider_data_saved_mail = (By.XPATH, "//tr[2]/td[2]")
    _provider_data_saved_www = (By.XPATH, "//tr[5]/td[2]")
    _provider_data_saved_address = (By.XPATH, "//tr[4]/td[2]")
    _ask_for_offers_button = (By.XPATH, "//a[2]")
    _first_offer = (By.XPATH, "//div[@id='recommendedusers']/div/table/tbody/tr[2]/td[7]/input")
    _first_consignment_distinguish_button = (By.XPATH, "//td[5]/a")
    _provider_first_consignment_distinguish_button = (By.XPATH, "//td[5]/a")
    _set_highlited_checkbox = (By.NAME, "auction_special")
    _set_urgent_checkbox = (By.NAME, "auction_important")
    _submit_distinguish_consignment = (By.ID, "add_auction_button")
    # _provider_my_consignments_menu = (By.XPATH, "//div[6]/div/div/ul/li[4]/a")
    _provider_my_consignments_menu = (By.PARTIAL_LINK_TEXT, u"Moje przesyłki")
    _executed_result_field = (By.XPATH, "/html/body/div[7]/div")

    def __init__(self, driver):
        super(ProfilePage, self).__init__(driver, self._title)

    def edit_user_profile(self):
        self.click(self._edit_profile_button)
        self.clear_field_and_send_keys(self._change_name, self._name_field)
        self.clear_field_and_send_keys(self._change_email, self._email_field)
        self.clear_field_and_send_keys(self._change_phone, self._phone_field)
        self.click(self._language_dropdown)
        self.click(self._language_polish)
        self.click(self._country_dropdown)
        self.click(self._random_country_button)
        self.clear_field_and_send_keys(self._change_street, self._street_field)
        self.clear_field_and_send_keys(self._change_building_number, self._building_number_field)
        self.clear_field_and_send_keys(self._change_postal_code, self._postal_code_field)
        self.clear_field_and_send_keys(self._change_city, self._city_field)
        self.click(self._save_button)

    def edit_consignment(self):
        self.click(self._my_consignments_menu)
        self.click(self._first_consignment_edit)
        return AddConsignmentPage(self.get_driver())

    def withdraw_consignment(self):
        self.click(self._my_consignments_menu)
        self.click(self._first_consignment_withdraw)
        self.click(self._random_withdraw_cause)
        self.click(self._withdraw_consignment_submit)

    def open_first_auction(self):
        self.condition_click(self._my_consignments_menu)
        self.click(self._first_consignment_enter)
        return ConsignmentPage(self.get_driver())

    def withdraw_offer(self):
        self.click(self._my_offers_menu)
        self.click(self._withdraw_first_offer)
        self.click(self._withdraw_first_offer_confirm)
        sleep(2)

    def issue_consignment_again(self):
        self.click(self._my_consignments_menu)
        self.click(self._unactual_tab)
        self.click(self._first_consignment_issue_again)
        return AddConsignmentPage(self.get_driver())

    def payback_commission(self):
        self.click(self._my_offers_menu)
        self.click(self._commission_payback_tab)
        self.click(self._commission_payback_request_link)
        self.clear_field_and_send_keys(get_random_string(10), self._commission_reason_field)
        self.click(self._commission_confirmation_button)

    def edit_provider_profile(self):
        self.click(self._provider_profile_button)
        while True:
            try:
                self.click(self._remove_first_category_button, "remove first category button is not clickable", 2)
            except TimeoutException:
                break
        self.click(self._category_dropdown)
        self.click(self._random_category_button)
        while True:
            try:
                self.click(self._remove_first_country_button, "remove first country button is not clickable", 2)
            except TimeoutException:
                break
        self.click(self._country_dropdown)
        self.click(self._random_country_button)
        while True:
            try:
                self.click(self._remove_first_route_button, "remove first route button is not clickable", 2)
            except TimeoutException:
                break
        self.click(self._add_route_button)
        self.clear_field_and_send_keys(self._route_from_value, self._route_from_field)
        self.click(self._route_from_field)
        self.clear_field_and_send_keys(self._route_to_value, self._route_to_field)
        self.click(self._route_to_field)
        self.click(self._add_route_both_sides_checkbox)
        while True:
            try:
                self.click(self._remove_first_accepted_form_of_payment_button, "remove first accepted form of payment button is not clickable", 2)
            except TimeoutException:
                break
        self.click(self._accepted_form_of_payment_dropodown)
        self.click(self._random_accepted_form_of_payment_button)
        sleep(2)
        while True:
            try:
                self.click(self._remove_first_car_button, "remove first car button is not clickable", 2)
            except TimeoutException:
                break
        self.click(self._add_car_button)
        self.click(self._first_car_type_dropdown)
        self.click(self._random_first_car_type_button)
        self.click(self._first_car_capacity_dropdown)
        self.click(self._random_first_car_capacity_button)
        self.clear_field_and_send_keys(self._first_car_number_value, self._first_car_number_field)
        sleep(2)
        self.click(self._add_car_button)
        self.click(self._second_car_type_dropdown)
        self.click(self._random_second_car_type_button)
        self.click(self._second_car_capacity_dropdown)
        self.click(self._random_second_car_capacity_button)
        self.clear_field_and_send_keys(self._second_car_number_value, self._second_car_number_field)
        self.clear_field_and_send_keys(self._company_description_value, self._company_description_field)
        self.click(self._random_transport_profile)
        self.click(self._company_kind_dropdown)
        self.click(self._random_company_kind_button)
        sleep(2)
        self.click(self._issue_VAT_NP_invoices_dropdown)
        self.click(self._random_issue_VAT_NP_invoices_button)
        self.click(self._issue_VAT_invoices_dropdown)
        self.click(self._random_issue_VAT_invoices_button)
        self.clear_field_and_send_keys(get_random_integer(1), self._employee_number_field)
        self.clear_field_and_send_keys(get_random_integer(1), self._driver_number_field)
        self.clear_field_and_send_keys(self._company_creation_year_value, self._company_creation_year_field)
        self.click(self._save_changes)

    def edit_provider_data(self):
        self.click(self._provider_profile_button)
        self.click(self._my_data_tab)
        self.clear_field_and_send_keys(self._change_name, self._name_field)
        self.clear_field_and_send_keys(self._change_email, self._email_field)
        self.clear_field_and_send_keys(self._change_phone, self._phone_field)
        self.click(self._save_button)

    def edit_provider_company_data(self):
        self.click(self._provider_profile_button)
        self.click(self._company_data_tab)
        self.clear_field_and_send_keys(get_random_string(10), self._company_name)
        self.clear_field_and_send_keys(get_random_string(10), self._company_krs)
        self.clear_field_and_send_keys(get_random_integer(10), self._company_nip)
        self.clear_field_and_send_keys(self._change_phone, self._company_mobile)
        self.click(self._company_country_dropdown)
        self.click(self._random_company_country_button)
        self.clear_field_and_send_keys(self._change_street, self._company_street)
        self.clear_field_and_send_keys(get_random_integer(2), self._company_building)
        self.clear_field_and_send_keys(get_random_string(9), self._company_city)
        self.clear_field_and_send_keys(self._change_postal_code, self._company_postal)
        self.clear_field_and_send_keys("www."+get_random_string(5)+".pl", self._company_www)
        self.click(self._company_data_save_button)

    def edit_provider_notifications(self):
        self.click(self._provider_profile_button)
        self.click(self._notification_settings_tab)
        self.click(self._random_notification_period_radio)
        self.click(self._notification_category_custom_radio)
        while True:
            try:
                self.click(self._remove_first_notification_category_button, "remove first notification category button is not clickable", 2)
            except TimeoutException:
                break
        self.click(self._notification_category_dropdown)
        self.condition_click(self._random_notification_category)
        self.click(self._notifications_countries_custom_radio)
        while True:
            try:
                self.click(self._remove_first_country_button, "remove first country button is not clickable", 2)
            except TimeoutException:
                break
        self.click(self._notifications_countries_custom_dropdown)
        self.click(self._random_notifications_countries_custom_button)
        self.click(self._save_notifications_button)

    def change_password(self):
        self.click(self._edit_profile_button)
        self.click(self._change_password_tab)
        self.clear_field_and_send_keys(get_password('change_pass1.txt'), self._change_password_old_field)
        change_password_value('change_pass1.txt')
        self.clear_field_and_send_keys(get_password('change_pass1.txt'), self._change_password_new_field)
        self.clear_field_and_send_keys(get_password('change_pass1.txt'), self._change_password_new2_field)
        self.click(self._change_password_submit)

    def open_first_message(self):
        self.click(self._messages_menu)
        self.click(self._first_message)
        return ConsignmentPage(self.get_driver())

    def user_open_first_message(self):
        self.click(self._user_messages_menu)
        self.click(self._user_first_message)
        return ConsignmentPage(self.get_driver())

    def user_click_reply_to_question(self):
        self.click(self._user_messages_menu)
        self.click(self._user_first_link_reply_to_question)
        return ConsignmentPage(self.get_driver())

    def make_offer_executed(self):
        self.click(self._my_offers_menu)
        self.click(self._accepted_tab)
        self.get_driver().execute_script("window.scrollTo(1100, 320);")
        self.click(self._set_executed_link)
        self.click(self._set_executed_submit)

    def provider_send_commentary_from_my_offers_menu(self):
        self.click(self._my_offers_menu)
        self.click(self._accepted_tab)
        self.click(self._my_offers_send_commentary_button)
        self.click(self._random_commentary_type_button)
        self.clear_field_and_send_keys("This is my commentary", self._my_offers_commentary_content)
        self.click(self._my_offers_commentary_submit_button)

    def provider_send_commentary_from_commentaries_menu(self):
        self.click(self._provider_commentaries_menu)
        self.click(self._provider_send_commentary_button)
        self.clear_field_and_send_keys("This is my commentary", self._provider_send_commentary_content)
        self.click(self._provider_send_commentary_submit_button)

    def provider_reply_to_negative_commentary(self):
        self.click(self._provider_commentaries_menu)
        self.click(self._provider_received_commentaries_tab)
        self.click(self._provider_reply_to_negative_commentary_button)
        self.clear_field_and_send_keys("This is my reply", self._provider_reply_to_negative_commentary_content)
        self.click(self._provider_reply_to_negative_commentary_submit_button)

    def user_send_commentary_from_ended_transactions_menu(self):
        self.click(self._my_consignments_menu)
        self.click(self._ended_transactions_tab)
        self.click(self._first_ended_transaction_send_commentary_button)
        self.clear_field_and_send_keys("This is my commentary", self._first_ended_transaction_commentary_content)
        self.click(self._first_ended_transaction_submit_commentary_button)

    def user_send_commentary_from_commentaries_menu(self):
        self.click(self._commentaries_menu)
        self.click(self._first_transaction_send_commentary_button)
        self.clear_field_and_send_keys("This is my commentary", self._first_transaction_commentary_content)
        self.click(self._first_transaction_submit_commentary_button)

    def user_send_negative_commentary(self):
        self.click(self._commentaries_menu)
        self.click(self._first_transaction_send_commentary_button)
        self.select_index_from_dropdown(2, self._first_transaction_commentary_mark_dropdown)
        self.clear_field_and_send_keys("This is my commentary", self._first_transaction_commentary_content)
        self.click(self._first_transaction_submit_commentary_button)

    def store_provider_data(self):
        self.click(self._provider_profile_button)
        self.click(self._my_data_tab)
        self.name1 = self.get_text(self._provider_data_saved_name)
        self.tel = self.get_text(self._provider_data_saved_tel)
        self.mail = self.get_text(self._provider_data_saved_mail)
        # self.kom = self.get_text(self._provider_data_saved_kom)
        self.click(self._company_data_tab)
        self.www = self.get_text(self._provider_data_saved_www)
        self.address = self.get_text(self._provider_data_saved_address)
        self.address_without_html = re.sub("<.*?>", "", self.address)
        self.address_table = self.address_without_html.splitlines()

    def ask_for_offer_for_added_consignment(self):
        self.click(self._my_consignments_menu)
        self.click(self._ask_for_offers_button)
        self.click(self._first_offer)

    def set_consignment_highlited_and_urgent(self):
        self.check(self._set_urgent_checkbox)
        sleep(2)
        self.check(self._set_highlited_checkbox)
        sleep(2)
        self.click(self._submit_distinguish_consignment)

    def set_consignment_highlited(self):
        self.check(self._set_highlited_checkbox)
        sleep(1)
        self.click(self._submit_distinguish_consignment)

    def set_consignment_urgent(self):
        self.check(self._set_urgent_checkbox)
        sleep(1)
        self.click(self._submit_distinguish_consignment)

    def user_open_my_consignments_menu(self):
        self.click(self._my_consignments_menu)

    def provider_open_my_consignments_menu(self):
        self.click(self._provider_my_consignments_menu)

    def user_click_first_consignment_distinguish_button(self):
        self.click(self._first_consignment_distinguish_button)

    def provider_click_first_consignment_distinguish_button(self):
        self.click(self._provider_first_consignment_distinguish_button)

# coding=utf-8
from pages.base import BasePage
from selenium.webdriver.common.by import By
from utils.utils import *



class RegistrationPage(BasePage):
    _title = "Register"

    _register_user = (By.XPATH, "//button")
    _register_transport_provider = (By.XPATH, "//div[2]/a/div/button")
    _username_field = (By.ID, "user_register_login")
    _password_field = (By.ID, "user_register_plainPassword")
    _password = get_random_uuid(9)
    _email_field = (By.ID, "user_register_email")
    _email = "jedrek"+get_random_integer(4)+"@migmail.pl"
    _name_field = (By.ID, "user_register_name")
    _name = get_random_string(7)+" "+get_random_string(5)
    _phone_field = (By.ID, "user_register_phone")
    _phone = get_random_integer(9)
    _mobile_field = (By.ID, "guest_user_mobile")
    _mobile = get_random_integer(9)
    _rules_acceptance_checkbox = (By.XPATH, "//label")
    _guest_user_acceptance_checkbox = (By.XPATH, "//div[2]/div/label")
    _guest_user_accept_info_checkbox = (By.XPATH, "//div[3]/div/label")
    _register_button = (By.ID, "user_register_submit")
    _company_name_field = (By.ID, "company_name")
    _company_name = get_random_string(7)
    _NIP_field = (By.ID, "company_nip")
    _NIP_value = get_random_integer(10)
    _regon_field = (By.ID, "company_regon")
    _regon_value = get_random_integer(9)
    _country_list = (By.ID, "company_country")
    _city_field = (By.ID, "company_city")
    _city_value = get_random_string(8)
    _postal_code_field = (By.ID, "company_postal")
    _postal_code_value = get_random_integer(2)+"-"+get_random_integer(3)
    _street_field = (By.ID, "company_street")
    _street_value = get_random_string(8)
    _building_number_field = (By.ID, "company_building")
    _building_number_value = get_random_integer(2)
    _www_field = (By.ID, "company_www")
    _www_value = "www."+get_random_string(8)+".pl"
    _description_field = (By.ID, "company_description")
    _description_value = get_random_string(10)

    def __init__(self, driver):
        super(RegistrationPage, self).__init__(driver, self._title)
        self._username_user_register = get_random_uuid(9)
        self._username_user_login_unactivated = get_random_uuid(9)
        self._username_provider = get_random_uuid(9)
        self._username_user_add_new_consignment = get_random_uuid(9)
        self._email_user_register = "jedrek"+get_random_integer(5)+"@migmail.pl"
        self._email_user_login_unactivated = "jedrek"+get_random_integer(5)+"@migmail.pl"
        self._email_user_add_new_consignment = "jedrek"+get_random_integer(5)+"@migmail.pl"

    def new_user_click_register(self):
        self.click(self._register_user)

    def register_user_fill_username_field(self):
        self.clear_field_and_send_keys(self._username_user_register, self._username_field)

    def register_user_fill_email_field(self):
        self.clear_field_and_send_keys(self._email_user_register, self._email_field)

    def login_unactivated_user_fill_username_field(self):
        self.clear_field_and_send_keys(self._username_user_login_unactivated, self._username_field)

    def login_unactivated_user_fill_email_field(self):
        self.clear_field_and_send_keys(self._email_user_login_unactivated, self._email_field)

    def add_new_consignment_unactivated_fill_username_field(self):
        self.clear_field_and_send_keys(self._username_user_add_new_consignment, self._username_field)

    def add_new_consignment_unactivated_fill_email_field(self):
        self.clear_field_and_send_keys(self._email_user_add_new_consignment, self._email_field)

    def new_user_fill_data(self):
        self.clear_field_and_send_keys(self._name, self._name_field)
        self.clear_field_and_send_keys(self._phone, self._phone_field)
        self.clear_field_and_send_keys(self._password, self._password_field)
        self.check(self._rules_acceptance_checkbox)
        self.check(self._guest_user_acceptance_checkbox)
        self.check(self._guest_user_accept_info_checkbox)
        self.click(self._register_button)

    def new_transport_provider(self):
        self.click(self._register_transport_provider)
        self.clear_field_and_send_keys(self._username_provider, self._username_field)
        self.clear_field_and_send_keys(self._password, self._password_field)
        self.clear_field_and_send_keys(self._email, self._email_field)
        self.clear_field_and_send_keys(self._name, self._name_field)
        self.clear_field_and_send_keys(self._phone, self._phone_field)
        # self.clear_field_and_send_keys(self._mobile, self._mobile_field)
        # self.clear_field_and_send_keys(self._company_name, self._company_name_field)
        # self.clear_field_and_send_keys(self._NIP_value, self._NIP_field)
        # self.clear_field_and_send_keys(self._regon_value, self._regon_field)
        # self.select_index_from_dropdown(get_random_integer(2), self._country_list)
        # self.clear_field_and_send_keys(self._city_value, self._city_field)
        # self.clear_field_and_send_keys(self._postal_code_value, self._postal_code_field)
        # self.clear_field_and_send_keys(self._street_value, self._street_field)
        # self.clear_field_and_send_keys(self._building_number_value, self._building_number_field)
        # self.clear_field_and_send_keys(self._www_value, self._www_field)
        # self.clear_field_and_send_keys(self._description_value, self._description_field)
        self.check(self._rules_acceptance_checkbox)
        self.check(self._guest_user_acceptance_checkbox)
        self.check(self._guest_user_accept_info_checkbox)
        self.click(self._register_button)
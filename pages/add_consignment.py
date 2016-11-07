# coding=utf-8
import datetime
from pages.base import BasePage
from pages.page import *
from pages.view_consignments import ViewConsignmentsPage
from selenium.webdriver.common.by import By
from time import sleep
from utils.utils import *
from pages.consignment_page import ConsignmentPage



class AddConsignmentPage(BasePage):

    _title = "Add consignment"
    _url = "http://clickuser:Click4Test@test.clicktrans.pl/"
    _url_old = "http://clicktrans_test:click!82@test.clicktrans.pl/"

    _category_dropdown = (By.XPATH, "//div[@id='categories']/form/div/div/div/div/div/div/div")
    _category_furniture = (By.LINK_TEXT, "Meble")
    _category_parcels = (By.XPATH, "//div[7]/a/span")
    _consignment_title_field = (By.ID, "EditAuction_title")
    _send_city_field = (By.ID, "sendLocation")
    _receive_city_field = (By.ID, "receiveLocation")
    _placeholder_results = (By.LINK_TEXT, "Warszawa, Polska")
    _date_fixed_checkbox = (By.CSS_SELECTOR, "label.bolded.bigger-font")
    _send_date_field = (By.ID, "EditAuction_sendDate")
    _send_date_value = str(datetime.date.today().year)+"-"+str(datetime.date.today().month)+"-"+str(datetime.date.today().day)+" - "+str(datetime.date.today().year)+"-"+str(datetime.date.today().month)+"-"+str(datetime.date.today().day+1)
    _send_date_value_next_month = str(datetime.date.today().year)+"-"+str(datetime.date.today().month)+"-"+str(datetime.date.today().day)+" - "+str(datetime.date.today().year)+"-"+str(datetime.date.today().month+1)+"-1"
    _receive_date_field = (By.ID, "EditAuction_receiveDate")
    _receive_date_value = str(datetime.date.today().year)+"-"+str(datetime.date.today().month)+"-"+str(datetime.date.today().day+1)+" - "+str(datetime.date.today().year)+"-"+str(datetime.date.today().month)+"-"+str(datetime.date.today().day+2)
    _receive_date_value_next_month = str(datetime.date.today().year)+"-"+str(datetime.date.today().month+1)+"-1 - "+str(datetime.date.today().year)+"-"+str(datetime.date.today().month+1)+"-2"
    _additional_info_button = (By.XPATH, "//div[3]/div/label")
    _submit_consignment_button = (By.NAME, "EditAuction[submit]")
    _consignment_length = (By.ID, "EditAuction_item_length")
    _consignment_width = (By.ID, "EditAuction_item_width")
    _consignment_height = (By.ID, "EditAuction_item_height")
    _consignment_weight = (By.ID, "EditAuction_item_weight")
    _quantity = (By.ID, "EditAuction_item_itemsNumber")
    _type_of_service_dropdown = (By.XPATH, "//div[@id='form']/div[4]/div/div")
    _type_of_service_complex_service_option = (By.XPATH, "//div[4]/div/div[2]/div[2]")
    _budget = (By.ID, "EditAuction_budget")
    _additional_info = (By.ID, "EditAuction_description")
    _save_edit_consignment = (By.XPATH, "//input[@value='Zapisz zmiany']")
    _view_added_consignment_button = (By.XPATH, "//div/div/div/div/div/a[2]")
    _consignment_title_result_page = (By.XPATH, "//div/div/div/div/div/div/a")
    _consignment_title_result_page_after_payment = (By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div/div[2]/strong/a")
    _first_offer = (By.XPATH, "//td[7]/button")
    _highlited_checkbox = (By.NAME, "auction_special")
    _urgent_checkbox = (By.NAME, "auction_important")
    _test_payment_radio = (By.XPATH, "//input[@value='t']")
    _invoice_company_country = (By.ID, "invoice_company_country")
    _submit_payment_button = (By.XPATH, "//input[@value='Płacę']")
    _payu_accept_button = (By.XPATH, "//input")
    _payu_valid_authorization = (By.XPATH, "/html/body/div/div[2]/div/div[1]/div/table/tbody/tr/td[1]/form/input[1]")
    _first_payment_date_field = (By.XPATH, "/html/body/div[1]/div[3]/div[4]/div[3]/div[1]/div[2]/div[1]/table/tbody/tr[2]/td[3]")

    def __init__(self, driver):
        super(AddConsignmentPage, self).__init__(driver, self._title)
        self._title_uuid = get_random_uuid(7)
        ViewConsignmentsPage._title_uuid = self._title_uuid

    def new_furniture_consignment(self):
        self.click(self._category_dropdown)
        self.click(self._category_furniture)
        self.send_keys(self._title_uuid, self._consignment_title_field)
        self.send_keys(u"Wrocław", self._send_city_field)
        sleep(2)
        self.click(self._receive_city_field)
        self.send_keys(u"Warszawa", self._receive_city_field)
        sleep(2)
        self.click(self._consignment_title_field)
        self.condition_click(self._date_fixed_checkbox)
        if str(datetime.date.today().day) == 30:
            self.clear_field_and_send_keys(self._send_date_value_next_month, self._send_date_field)
        elif str(datetime.date.today().day) == 31:
            self.clear_field_and_send_keys(self._send_date_value_next_month, self._send_date_field)
        elif str(datetime.date.today().month) == 2 and str(datetime.date.today().day) == 29:
            self.clear_field_and_send_keys(self._send_date_value_next_month, self._send_date_field)
        else:
            self.clear_field_and_send_keys(self._send_date_value, self._send_date_field)
        if str(datetime.date.today().day) == 29:
            self.clear_field_and_send_keys(self._receive_date_value_next_month, self._receive_date_field)
        elif str(datetime.date.today().day) == 30:
            self.clear_field_and_send_keys(self._receive_date_value_next_month, self._receive_date_field)
        elif str(datetime.date.today().day) == 31:
            self.clear_field_and_send_keys(self._receive_date_value_next_month, self._receive_date_field)
        elif str(datetime.date.today().month) == 2 and str(datetime.date.today().day) == 28:
            self.clear_field_and_send_keys(self._receive_date_value_next_month, self._receive_date_field)
        else:
            self.clear_field_and_send_keys(self._receive_date_value, self._receive_date_field)
        self.click(self._consignment_title_field)
        self.condition_click(self._additional_info_button)
        self.clear_field_and_send_keys("3", self._consignment_length)
        self.clear_field_and_send_keys("4", self._consignment_width)
        self.clear_field_and_send_keys("2", self._consignment_height)
        self.clear_field_and_send_keys("15", self._consignment_weight)
        self.clear_field_and_send_keys("5", self._quantity)
        self.click(self._type_of_service_dropdown)
        self.click(self._type_of_service_complex_service_option)
        self.clear_field_and_send_keys("200", self._budget)
        self.clear_field_and_send_keys("This is my additional info", self._additional_info)
        self.click(self._submit_consignment_button)
        return self._title_uuid

    def edit_consignment_parcel(self):
        self.click(self._category_dropdown)
        self.click(self._category_parcels)
        self.clear_field_and_send_keys(self._title_uuid, self._consignment_title_field)
        self.clear_field_and_send_keys(u"Katowice", self._send_city_field)
        sleep(2)
        self.click(self._receive_city_field)
        self.clear_field_and_send_keys(u"Poznań", self._receive_city_field)
        sleep(2)
        self.click(self._consignment_title_field)
        # self.condition_click(self._date_fixed_checkbox)
        if str(datetime.date.today().day) == 30:
            self.clear_field_and_send_keys(self._send_date_value_next_month, self._send_date_field)
        elif str(datetime.date.today().day) == 31:
            self.clear_field_and_send_keys(self._send_date_value_next_month, self._send_date_field)
        elif str(datetime.date.today().month) == 2 and str(datetime.date.today().day) == 29:
            self.clear_field_and_send_keys(self._send_date_value_next_month, self._send_date_field)
        else:
            self.clear_field_and_send_keys(self._send_date_value, self._send_date_field)
        if str(datetime.date.today().day) == 29:
            self.clear_field_and_send_keys(self._receive_date_value_next_month, self._receive_date_field)
        elif str(datetime.date.today().day) == 30:
            self.clear_field_and_send_keys(self._receive_date_value_next_month, self._receive_date_field)
        elif str(datetime.date.today().day) == 31:
            self.clear_field_and_send_keys(self._receive_date_value_next_month, self._receive_date_field)
        elif str(datetime.date.today().month) == 2 and str(datetime.date.today().day) == 28:
            self.clear_field_and_send_keys(self._receive_date_value_next_month, self._receive_date_field)
        else:
            self.clear_field_and_send_keys(self._receive_date_value, self._receive_date_field)
        self.click(self._consignment_title_field)
        self.condition_click(self._additional_info_button)
        self.clear_field_and_send_keys("5", self._consignment_length)
        self.clear_field_and_send_keys("3", self._consignment_width)
        self.clear_field_and_send_keys("8", self._consignment_height)
        self.clear_field_and_send_keys("12", self._consignment_weight)
        self.clear_field_and_send_keys("3", self._quantity)
        # self.click(self._type_of_service_dropdown)
        # self.click(self._type_of_service_complex_service_option)
        # self.clear_field_and_send_keys("200", self._budget)
        self.clear_field_and_send_keys("This is my additional info after edit", self._additional_info)
        self.click(self._submit_consignment_button)
        sleep(90)

    def view_added_consignment(self):
        self.click(self._view_added_consignment_button)
        return ConsignmentPage(self.get_driver())


    def get_consignment_title_from_result_page(self):
        self.consignment_title_result_page = self.get_text(self._consignment_title_result_page)

    def get_consignment_title_from_result_page_after_payment(self):
        self.consignment_title_result_page_after_payment = self.get_text(self._consignment_title_result_page_after_payment)

    def edit_consignment_cars(self):
        self.click(self._cars_link)
        sleep(4)
        self.clear_field_and_send_keys("Pontiac 100", self._car_model)
        self.clear_field_and_send_keys(get_random_integer(2), self._car_weight)
        self.clear_field_and_send_keys(get_random_integer(3), self._car_budget)
        self.clear_field_and_send_keys(get_random_string(20), self._additional_info)
        self.click(self._set_price_and_deadline)
        self.select_index_from_dropdown(4, self._send_province_dropdown)
        self.clear_field_and_send_keys("Edited", self._send_city)
        self.clear_field_and_send_keys("50-690", self._send_post_code)
        self.select_index_from_dropdown(5, self._receive_province)
        self.clear_field_and_send_keys("Also", self._receive_city)
        self.clear_field_and_send_keys("05-880", self._receive_post_code)
        self.select_index_from_dropdown(2, self._period)
        self.click(self._save_transport_button)

    def ask_for_offer_while_adding_consignment(self):
        self.click(self._first_offer)

    def add_consignment_parcel(self):
        self.click(self._category_dropdown)
        self.click(self._category_parcels)
        self.clear_field_and_send_keys(self._title_uuid, self._consignment_title_field)
        self.clear_field_and_send_keys(u"Warszawa", self._send_city_field)
        sleep(2)
        self.click(self._receive_city_field)
        self.clear_field_and_send_keys(u"Poznań", self._receive_city_field)
        sleep(2)
        self.click(self._consignment_title_field)
        self.condition_click(self._date_fixed_checkbox)
        if str(datetime.date.today().day) == 30:
            self.clear_field_and_send_keys(self._send_date_value_next_month, self._send_date_field)
        elif str(datetime.date.today().day) == 31:
            self.clear_field_and_send_keys(self._send_date_value_next_month, self._send_date_field)
        elif str(datetime.date.today().month) == 2 and str(datetime.date.today().day) == 29:
            self.clear_field_and_send_keys(self._send_date_value_next_month, self._send_date_field)
        else:
            self.clear_field_and_send_keys(self._send_date_value, self._send_date_field)
        if str(datetime.date.today().day) == 29:
            self.clear_field_and_send_keys(self._receive_date_value_next_month, self._receive_date_field)
        elif str(datetime.date.today().day) == 30:
            self.clear_field_and_send_keys(self._receive_date_value_next_month, self._receive_date_field)
        elif str(datetime.date.today().day) == 31:
            self.clear_field_and_send_keys(self._receive_date_value_next_month, self._receive_date_field)
        elif str(datetime.date.today().month) == 2 and str(datetime.date.today().day) == 28:
            self.clear_field_and_send_keys(self._receive_date_value_next_month, self._receive_date_field)
        else:
            self.clear_field_and_send_keys(self._receive_date_value, self._receive_date_field)
        self.click(self._consignment_title_field)
        self.condition_click(self._additional_info_button)
        self.clear_field_and_send_keys("5", self._consignment_length)
        self.clear_field_and_send_keys("3", self._consignment_width)
        self.clear_field_and_send_keys("8", self._consignment_height)
        self.clear_field_and_send_keys("12", self._consignment_weight)
        self.clear_field_and_send_keys("3", self._quantity)
        # self.click(self._type_of_service_dropdown)
        # self.click(self._type_of_service_complex_service_option)
        # self.clear_field_and_send_keys("200", self._budget)
        self.clear_field_and_send_keys("This is my additional info", self._additional_info)
        self.click(self._submit_consignment_button)

    def set_highlited(self):
        self.check(self._highlited_checkbox)
        self.click(self._receive_city)

    def set_urgent(self):
        self.click(self._urgent_checkbox)
        self.click(self._receive_city)

    def pay_with_test_payment(self):
        self.click(self._test_payment_radio)
        self.select_index_from_dropdown(get_random_integer(2), self._invoice_company_country)
        self.click(self._submit_payment_button)
        sleep(2)
        self.click(self._payu_accept_button)
        # self.click(self._payu_valid_authorization)

    def get_first_payment_date(self):
        return self.get_text(self._first_payment_date_field)

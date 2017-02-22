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
    _category_cars = (By.XPATH, "//div[3]/a/span")
    _consignment_title_field = (By.ID, "EditAuction_title")
    _send_city_field = (By.ID, "sendLocation")
    _receive_city_field = (By.ID, "receiveLocation")
    _placeholder_results = (By.LINK_TEXT, "Warszawa, Polska")
    _date_fixed_checkbox = (By.XPATH, "//label")
    _send_date_field = (By.NAME, "EditAuction[sendDate]")
    _send_date_value = str(datetime.date.today().year)+"-"+str(datetime.date.today().month)+"-"+str(datetime.date.today().day)+" - "+str(datetime.date.today().year)+"-"+str(datetime.date.today().month)+"-"+str(datetime.date.today().day+1)
    _send_date_value_next_month = str(datetime.date.today().year)+"-"+str(datetime.date.today().month)+"-"+str(datetime.date.today().day)+" - "+str(datetime.date.today().year)+"-"+str(datetime.date.today().month+1)+"-1"
    _today = datetime.date.today()
    _tomorrow = datetime.date.today()+ datetime.timedelta(1)
    _2_days_ahead = datetime.date.today()+ datetime.timedelta(2)
    _send_date_from_field = (By.NAME, "daterangepicker_start")
    _send_date_from_value = _today.strftime('%Y-%m-%d')
    _send_date_to_field = (By.NAME, "daterangepicker_end")
    _send_date_to_value = _tomorrow.strftime('%Y-%m-%d')
    _receive_date_from_field = (By.XPATH, "(//input[@name='daterangepicker_start'])[2]")
    _receive_date_from_value = _tomorrow.strftime('%Y-%m-%d')
    _receive_date_to_field = (By.XPATH, "(//input[@name='daterangepicker_end'])[2]")
    _receive_date_to_value = _2_days_ahead.strftime('%Y-%m-%d')
    _receive_date_field = (By.ID, "EditAuction_receiveDate")
    _receive_date_value = str(datetime.date.today().year)+"-"+str(datetime.date.today().month)+"-"+str(datetime.date.today().day+1)+" - "+str(datetime.date.today().year)+"-"+str(datetime.date.today().month)+"-"+str(datetime.date.today().day+2)
    _receive_date_value_next_month = str(datetime.date.today().year)+"-"+str(datetime.date.today().month+1)+"-1 - "+str(datetime.date.today().year)+"-"+str(datetime.date.today().month+1)+"-2"
    _additional_info_button = (By.XPATH, "//div[3]/div/label")
    _submit_consignment_button = (By.NAME, "EditAuction[submit]")
    _consignment_length = (By.ID, "EditAuction_item_length")
    _consignment_width = (By.ID, "EditAuction_item_width")
    _consignment_height = (By.ID, "EditAuction_item_height")
    _consignment_weight = (By.ID, "EditAuction_item_weight")
    _consignment_cars_brand_field = (By.ID, "EditAuction_item_model")
    _consignment_cars_brand_value = get_random_string(8)
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
    _edit_consignment_result_field = (By.CSS_SELECTOR, "div.header")

    def __init__(self, driver):
        super(AddConsignmentPage, self).__init__(driver, self._title)
        self._title_uuid = get_random_uuid(7)
        ViewConsignmentsPage._title_uuid = self._title_uuid

    def new_furniture_consignment(self):
        self.click(self._category_dropdown, "The category dropdown on new consignment page couldn't be clicked or wasn't visible")
        self.click(self._category_furniture, "The category <Furniture> on category dropdown on new consignment page couldn't be clicked or wasn't visible")
        self.send_keys(self._title_uuid, self._consignment_title_field, "The attempt to send random consignment title to consignment title field on add consignment page was unsuccessful")
        self.if_not_visible_click(self._send_date_field, self._date_fixed_checkbox)
        # self.condition_click(self._date_fixed_checkbox, "The date fixed checkbox on add consignment page couldn't be clicked or wasn't visible")
        sleep(1)
        self.click(self._send_date_field)
        self.clear_field_and_send_keys(self._send_date_from_value, self._send_date_from_field)
        self.clear_field_and_send_keys(self._send_date_to_value, self._send_date_to_field)
        self.click(self._receive_date_field)
        self.clear_field_and_send_keys(self._receive_date_from_value, self._receive_date_from_field)
        self.clear_field_and_send_keys(self._receive_date_to_value, self._receive_date_to_field)
        self.click(self._consignment_title_field, "The consignment title field on add consignment page couldn't be clicked or wasn't visible")
        self.condition_click(self._additional_info_button, "The additional info button on add consignment page couldn't be clicked or wasn't visible")
        self.clear_field_and_send_keys("3", self._consignment_length, "The attempt to enter <3> to consignment length field on add consignment page was unsuccessful")
        self.clear_field_and_send_keys("4", self._consignment_width, "The attempt to enter <4> to consignment width field on add consignment page was unsuccessful")
        self.clear_field_and_send_keys("2", self._consignment_height, "The attempt to enter <2> to consignment height field on add consignment page was unsuccessful")
        self.clear_field_and_send_keys("15", self._consignment_weight, "The attempt to enter <15> to consignment weight field on add consignment page was unsuccessful")
        self.clear_field_and_send_keys("5", self._quantity, "The attempt to enter <5> to consignment quantity field on add consignment page was unsuccessful")
        self.get_driver().execute_script("window.scrollTo(1100, 800);")
        self.click(self._type_of_service_dropdown, "The type of service dropdown on add consignment page couldn't be clicked or wasn't visible")
        self.click(self._type_of_service_complex_service_option, "The complex service option in type of service dropdown on add consignment page couldn't be clicked or wasn't visible")
        self.clear_field_and_send_keys("200", self._budget, "The attempt to enter <200> to consignment budget field on add consignment page was unsuccessful")
        self.clear_field_and_send_keys("This is my additional info", self._additional_info, "The attempt to enter <This is my additional info> to consignment additional info field on add consignment page was unsuccessful")
        self.send_keys(u"Wrocław", self._send_city_field, "The attempt to enter <Wrocław> into send city field on add consignment page was unsuccessful")
        sleep(2)
        self.click(self._receive_city_field, "The receive city field on add consignment page couldn't be clicked or wasn't visible")
        self.send_keys(u"Warszawa", self._receive_city_field, "The attempt to enter <Warszawa> into receive city field on add consignment page was unsuccessful")
        sleep(2)
        self.click(self._consignment_title_field, "The consignment title field on add consignment page couldn't be clicked or wasn't visible")

        # if str(datetime.date.today().day) == 30:
        #     self.clear_field_and_send_keys(self._send_date_value_next_month, self._send_date_field, "The attempt to send date to send date field on add consignment page was unsuccessful")
        # elif str(datetime.date.today().day) == 31:
        #     self.clear_field_and_send_keys(self._send_date_value_next_month, self._send_date_field, "The attempt to send date to send date field on add consignment page was unsuccessful")
        # elif str(datetime.date.today().month) == 2 and str(datetime.date.today().day) == 29:
        #     self.clear_field_and_send_keys(self._send_date_value_next_month, self._send_date_field, "The attempt to send date to send date field on add consignment page was unsuccessful")
        # else:
        #     self.clear_field_and_send_keys(self._send_date_value, self._send_date_field, "The attempt to send date to send date field on add consignment page was unsuccessful")
        # if str(datetime.date.today().day) == 29:
        #     self.clear_field_and_send_keys(self._receive_date_value_next_month, self._receive_date_field, "The attempt to send date to receive date field on add consignment page was unsuccessful")
        # elif str(datetime.date.today().day) == 30:
        #     self.clear_field_and_send_keys(self._receive_date_value_next_month, self._receive_date_field, "The attempt to send date to receive date field on add consignment page was unsuccessful")
        # elif str(datetime.date.today().day) == 31:
        #     self.clear_field_and_send_keys(self._receive_date_value_next_month, self._receive_date_field, "The attempt to send date to receive date field on add consignment page was unsuccessful")
        # elif str(datetime.date.today().month) == 2 and str(datetime.date.today().day) == 28:
        #     self.clear_field_and_send_keys(self._receive_date_value_next_month, self._receive_date_field, "The attempt to send date to receive date field on add consignment page was unsuccessful")
        # else:
        #     self.clear_field_and_send_keys(self._receive_date_value, self._receive_date_field, "The attempt to send date to receive date field on add consignment page was unsuccessful")
        try:
            self.click(self._submit_consignment_button, "The submit consignment button on add consignment page couldn't be clicked or wasn't visible")
            sleep(3)
        except:
            self.click(self._submit_consignment_button, "The submit consignment button on add consignment page couldn't be clicked or wasn't visible")
        return self._title_uuid

    def edit_consignment_parcel(self):
        self.click(self._category_dropdown, "The category dropdown on edit consignment page couldn't be clicked or wasn't visible")
        self.click(self._category_parcels, "The category <Parcels> on category dropdown on edit consignment page couldn't be clicked or wasn't visible")
        self.clear_field_and_send_keys(self._title_uuid, self._consignment_title_field, "The attempt to send random consignment title to consignment title field on edit consignment page was unsuccessful")
        # self.condition_click(self._date_fixed_checkbox, "The date fixed checkbox on edit consignment page couldn't be clicked or wasn't visible")
        self.if_not_visible_click(self._send_date_field, self._date_fixed_checkbox)
        self.click(self._send_date_field)
        self.clear_field_and_send_keys(self._send_date_from_value, self._send_date_from_field)
        self.clear_field_and_send_keys(self._send_date_to_value, self._send_date_to_field)
        self.click(self._receive_date_field)
        self.clear_field_and_send_keys(self._receive_date_from_value, self._receive_date_from_field)
        self.clear_field_and_send_keys(self._receive_date_to_value, self._receive_date_to_field)
        self.click(self._consignment_title_field, "The consignment title field on edit consignment page couldn't be clicked or wasn't visible")
        self.clear_field_and_send_keys(u"Katowice", self._send_city_field, "The attempt to enter <Katowice> into send city field on edit consignment page was unsuccessful")
        sleep(2)
        self.click(self._receive_city_field, "The receive city field on edit consignment page couldn't be clicked or wasn't visible")
        self.clear_field_and_send_keys(u"Poznań", self._receive_city_field, "The attempt to enter <Poznań> into receive city field on edit consignment page was unsuccessful")
        sleep(2)
        self.click(self._consignment_title_field, "The consignment title field on edit consignment page couldn't be clicked or wasn't visible")
        # if str(datetime.date.today().day) == 30:
        #     self.clear_field_and_send_keys(self._send_date_value_next_month, self._send_date_field, "The attempt to send date to send date field on edit consignment page was unsuccessful")
        # elif str(datetime.date.today().day) == 31:
        #     self.clear_field_and_send_keys(self._send_date_value_next_month, self._send_date_field, "The attempt to send date to send date field on edit consignment page was unsuccessful")
        # elif str(datetime.date.today().month) == 2 and str(datetime.date.today().day) == 29:
        #     self.clear_field_and_send_keys(self._send_date_value_next_month, self._send_date_field, "The attempt to send date to send date field on edit consignment page was unsuccessful")
        # else:
        #     self.clear_field_and_send_keys(self._send_date_value, self._send_date_field, "The attempt to send date to send date field on edit consignment page was unsuccessful")
        # if str(datetime.date.today().day) == 29:
        #     self.clear_field_and_send_keys(self._receive_date_value_next_month, self._receive_date_field, "The attempt to send date to receive date field on edit consignment page was unsuccessful")
        # elif str(datetime.date.today().day) == 30:
        #     self.clear_field_and_send_keys(self._receive_date_value_next_month, self._receive_date_field, "The attempt to send date to receive date field on edit consignment page was unsuccessful")
        # elif str(datetime.date.today().day) == 31:
        #     self.clear_field_and_send_keys(self._receive_date_value_next_month, self._receive_date_field, "The attempt to send date to receive date field on edit consignment page was unsuccessful")
        # elif str(datetime.date.today().month) == 2 and str(datetime.date.today().day) == 28:
        #     self.clear_field_and_send_keys(self._receive_date_value_next_month, self._receive_date_field, "The attempt to send date to receive date field on edit consignment page was unsuccessful")
        # else:
        #     self.clear_field_and_send_keys(self._receive_date_value, self._receive_date_field, "The attempt to send date to receive date field on edit consignment page was unsuccessful")
        self.condition_click(self._additional_info_button, "The additional info button on edit consignment page couldn't be clicked or wasn't visible")
        self.clear_field_and_send_keys("5", self._consignment_length, "The attempt to enter <5> to consignment length field on edit consignment page was unsuccessful")
        self.clear_field_and_send_keys("3", self._consignment_width, "The attempt to enter <3> to consignment width field on edit consignment page was unsuccessful")
        self.clear_field_and_send_keys("8", self._consignment_height, "The attempt to enter <8> to consignment height field on edit consignment page was unsuccessful")
        self.clear_field_and_send_keys("12", self._consignment_weight, "The attempt to enter <12> to consignment weight field on edit consignment page was unsuccessful")
        self.clear_field_and_send_keys("3", self._quantity, "The attempt to enter <3> to consignment quantity field on edit consignment page was unsuccessful")
        # self.click(self._type_of_service_dropdown, "The type of service dropdown on edit consignment page couldn't be clicked or wasn't visible")
        # self.click(self._type_of_service_complex_service_option, "The complex service option in type of service dropdown on edit consignment page couldn't be clicked or wasn't visible")
        # self.clear_field_and_send_keys("200", self._budget, "The attempt to enter <200> to consignment budget field on edit consignment page was unsuccessful")
        self.clear_field_and_send_keys("This is my additional info after edit", self._additional_info, "The attempt to enter <This is my additional info after edit> to consignment additional info field on edit consignment page was unsuccessful")
        self.click(self._submit_consignment_button, "The submit consignment button on edit consignment page couldn't be clicked or wasn't visible")

    def edit_consignment_cars(self):
        self.click(self._category_dropdown, "The category dropdown on edit consignment page couldn't be clicked or wasn't visible")
        self.click(self._category_cars, "The category <Parcels> on category dropdown on edit consignment page couldn't be clicked or wasn't visible")
        self.clear_field_and_send_keys(self._title_uuid, self._consignment_title_field, "The attempt to send random consignment title to consignment title field on edit consignment page was unsuccessful")
        # self.condition_click(self._date_fixed_checkbox, "The date fixed checkbox on edit consignment page couldn't be clicked or wasn't visible")
        self.if_not_visible_click(self._send_date_field, self._date_fixed_checkbox)
        self.click(self._send_date_field)
        self.clear_field_and_send_keys(self._send_date_from_value, self._send_date_from_field)
        self.clear_field_and_send_keys(self._send_date_to_value, self._send_date_to_field)
        self.click(self._receive_date_field)
        self.clear_field_and_send_keys(self._receive_date_from_value, self._receive_date_from_field)
        self.clear_field_and_send_keys(self._receive_date_to_value, self._receive_date_to_field)
        self.click(self._consignment_title_field, "The consignment title field on edit consignment page couldn't be clicked or wasn't visible")
        self.clear_field_and_send_keys(u"Katowice", self._send_city_field, "The attempt to enter <Katowice> into send city field on edit consignment page was unsuccessful")
        sleep(2)
        self.click(self._receive_city_field, "The receive city field on edit consignment page couldn't be clicked or wasn't visible")
        self.clear_field_and_send_keys(u"Poznań", self._receive_city_field, "The attempt to enter <Poznań> into receive city field on edit consignment page was unsuccessful")
        sleep(2)
        self.click(self._consignment_title_field, "The consignment title field on edit consignment page couldn't be clicked or wasn't visible")
        # if str(datetime.date.today().day) == 30:
        #     self.clear_field_and_send_keys(self._send_date_value_next_month, self._send_date_field, "The attempt to send date to send date field on edit consignment page was unsuccessful")
        # elif str(datetime.date.today().day) == 31:
        #     self.clear_field_and_send_keys(self._send_date_value_next_month, self._send_date_field, "The attempt to send date to send date field on edit consignment page was unsuccessful")
        # elif str(datetime.date.today().month) == 2 and str(datetime.date.today().day) == 29:
        #     self.clear_field_and_send_keys(self._send_date_value_next_month, self._send_date_field, "The attempt to send date to send date field on edit consignment page was unsuccessful")
        # else:
        #     self.clear_field_and_send_keys(self._send_date_value, self._send_date_field, "The attempt to send date to send date field on edit consignment page was unsuccessful")
        # if str(datetime.date.today().day) == 29:
        #     self.clear_field_and_send_keys(self._receive_date_value_next_month, self._receive_date_field, "The attempt to send date to receive date field on edit consignment page was unsuccessful")
        # elif str(datetime.date.today().day) == 30:
        #     self.clear_field_and_send_keys(self._receive_date_value_next_month, self._receive_date_field, "The attempt to send date to receive date field on edit consignment page was unsuccessful")
        # elif str(datetime.date.today().day) == 31:
        #     self.clear_field_and_send_keys(self._receive_date_value_next_month, self._receive_date_field, "The attempt to send date to receive date field on edit consignment page was unsuccessful")
        # elif str(datetime.date.today().month) == 2 and str(datetime.date.today().day) == 28:
        #     self.clear_field_and_send_keys(self._receive_date_value_next_month, self._receive_date_field, "The attempt to send date to receive date field on edit consignment page was unsuccessful")
        # else:
        #     self.clear_field_and_send_keys(self._receive_date_value, self._receive_date_field, "The attempt to send date to receive date field on edit consignment page was unsuccessful")
        self.condition_click(self._additional_info_button, "The additional info button on edit consignment page couldn't be clicked or wasn't visible")
        self.clear_field_and_send_keys(self._consignment_cars_brand_value, self._consignment_cars_brand_field, "The attempt to enter random text to consignment cars brand and model field on edit consignment page was unsuccessful")
        self.clear_field_and_send_keys("12", self._consignment_weight, "The attempt to enter <12> to consignment weight field on edit consignment page was unsuccessful")
        self.clear_field_and_send_keys("200", self._budget, "The attempt to enter <200> to consignment budget field on edit consignment page was unsuccessful")
        self.clear_field_and_send_keys("This is my additional info after edit", self._additional_info, "The attempt to enter <This is my additional info after edit> to consignment additional info field on edit consignment page was unsuccessful")
        self.click(self._submit_consignment_button, "The submit consignment button on edit consignment page couldn't be clicked or wasn't visible")


    def view_added_consignment(self):
        self.click(self._view_added_consignment_button, "The view added consignment button on confirmation page after adding consignment couldn't be clicked or wasn't visible")
        return ConsignmentPage(self.get_driver())


    def get_consignment_title_from_result_page(self):
        self.consignment_title_result_page = self.get_text(self._consignment_title_result_page)

    def get_consignment_title_from_result_page_after_payment(self):
        self.consignment_title_result_page_after_payment = self.get_text(self._consignment_title_result_page_after_payment)

    def ask_for_offer_while_adding_consignment(self):
        self.click(self._first_offer, "The first offer button on ask for offer while adding consignment page couldn't be clicked or wasn't visible")

    def add_consignment_parcel(self):
        self.click(self._category_dropdown, "The category dropdown on add consignment page couldn't be clicked or wasn't visible")
        self.click(self._category_parcels, "The category <Parcels> on category dropdown on add consignment page couldn't be clicked or wasn't visible")
        self.clear_field_and_send_keys(self._title_uuid, self._consignment_title_field, "The attempt to send random consignment title to consignment title field on add consignment page was unsuccessful")
        # self.condition_click(self._date_fixed_checkbox, "The date fixed checkbox on add consignment page couldn't be clicked or wasn't visible")
        self.if_not_visible_click(self._send_date_field, self._date_fixed_checkbox)
        sleep(1)
        self.click(self._send_date_field)
        self.clear_field_and_send_keys(self._send_date_from_value, self._send_date_from_field)
        self.clear_field_and_send_keys(self._send_date_to_value, self._send_date_to_field)
        self.click(self._receive_date_field)
        self.clear_field_and_send_keys(self._receive_date_from_value, self._receive_date_from_field)
        self.clear_field_and_send_keys(self._receive_date_to_value, self._receive_date_to_field)
        self.click(self._consignment_title_field, "The consignment title field on add consignment page couldn't be clicked or wasn't visible")
        self.clear_field_and_send_keys(u"Warszawa", self._send_city_field, "The attempt to enter <Warszawa> into send city field on add consignment page was unsuccessful")
        sleep(2)
        self.click(self._receive_city_field, "The receive city field on add consignment page couldn't be clicked or wasn't visible")
        self.clear_field_and_send_keys(u"Poznań", self._receive_city_field, "The attempt to enter <Poznań> into receive city field on add consignment page was unsuccessful")
        sleep(2)
        self.click(self._consignment_title_field, "The consignment title field on add consignment page couldn't be clicked or wasn't visible")
        # if str(datetime.date.today().day) == 30:
        #     self.clear_field_and_send_keys(self._send_date_value_next_month, self._send_date_field, "The attempt to send date to send date field on add consignment page was unsuccessful")
        # elif str(datetime.date.today().day) == 31:
        #     self.clear_field_and_send_keys(self._send_date_value_next_month, self._send_date_field, "The attempt to send date to send date field on add consignment page was unsuccessful")
        # elif str(datetime.date.today().month) == 2 and str(datetime.date.today().day) == 29:
        #     self.clear_field_and_send_keys(self._send_date_value_next_month, self._send_date_field, "The attempt to send date to send date field on add consignment page was unsuccessful")
        # else:
        #     self.clear_field_and_send_keys(self._send_date_value, self._send_date_field, "The attempt to send date to send date field on add consignment page was unsuccessful")
        # if str(datetime.date.today().day) == 29:
        #     self.clear_field_and_send_keys(self._receive_date_value_next_month, self._receive_date_field, "The attempt to send date to receive date field on add consignment page was unsuccessful")
        # elif str(datetime.date.today().day) == 30:
        #     self.clear_field_and_send_keys(self._receive_date_value_next_month, self._receive_date_field, "The attempt to send date to receive date field on add consignment page was unsuccessful")
        # elif str(datetime.date.today().day) == 31:
        #     self.clear_field_and_send_keys(self._receive_date_value_next_month, self._receive_date_field, "The attempt to send date to receive date field on add consignment page was unsuccessful")
        # elif str(datetime.date.today().month) == 2 and str(datetime.date.today().day) == 28:
        #     self.clear_field_and_send_keys(self._receive_date_value_next_month, self._receive_date_field, "The attempt to send date to receive date field on add consignment page was unsuccessful")
        # else:
        #     self.clear_field_and_send_keys(self._receive_date_value, self._receive_date_field, "The attempt to send date to receive date field on add consignment page was unsuccessful")
        self.condition_click(self._additional_info_button, "The additional info button on add consignment page couldn't be clicked or wasn't visible")
        self.clear_field_and_send_keys("5", self._consignment_length, "The attempt to enter <5> to consignment length field on add consignment page was unsuccessful")
        self.clear_field_and_send_keys("3", self._consignment_width, "The attempt to enter <3> to consignment width field on add consignment page was unsuccessful")
        self.clear_field_and_send_keys("8", self._consignment_height, "The attempt to enter <8> to consignment height field on add consignment page was unsuccessful")
        self.clear_field_and_send_keys("12", self._consignment_weight, "The attempt to enter <12> to consignment weight field on add consignment page was unsuccessful")
        self.clear_field_and_send_keys("3", self._quantity, "The attempt to enter <3> to consignment quantity field on add consignment page was unsuccessful")
        # self.click(self._type_of_service_dropdown, "The type of service dropdown on add consignment page couldn't be clicked or wasn't visible")
        # self.click(self._type_of_service_complex_service_option, "The complex service option in type of service dropdown on add consignment page couldn't be clicked or wasn't visible")
        # self.clear_field_and_send_keys("200", self._budget, "The attempt to enter <200> to consignment budget field on add consignment page was unsuccessful")
        self.clear_field_and_send_keys("This is my additional info", self._additional_info, "The attempt to enter <This is my additional info> to consignment additional info field on add consignment page was unsuccessful")
        self.click(self._submit_consignment_button, "The submit consignment button on add consignment page couldn't be clicked or wasn't visible")

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

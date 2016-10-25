# coding=utf-8
import datetime
from pages.base import BasePage
from selenium.webdriver.common.by import By
from time import sleep
from utils.utils import *




class ConsignmentPage(BasePage):
    _title = "Consignment"

    _consignment_violation_flag = (By.XPATH, "//div[2]/div[3]/a/i")
    _offer_violation_flag = (By.XPATH, "//td/a/i")
    _question_to_offer_violation_flag = (By.XPATH, "//div[2]/a/i")
    _question_to_consignment_violation_flag = (By.XPATH, "//div[2]/a/i")
    _violation_content = (By.XPATH, "//div/textarea")
    _violation_submit = (By.XPATH, "//div/button")
    _violation_to_offer_content_field = (By.XPATH, "//div[8]/div[2]/form/div/textarea")
    _violation_to_offer_submit = (By.XPATH, "//div[8]/div[2]/form/div[2]/div[2]/div/button")
    _violation_to_question_to_offer_content_field = (By.XPATH, "//div[9]/div[2]/form/div/textarea")
    _violation_to_question_to_offer_submit = (By.XPATH, "//div[9]/div[2]/form/div[2]/div[2]/div/button")
    _violation_to_question_to_consignment_content_field = (By.XPATH, "//div[6]/div[2]/form/div/textarea")
    _violation_to_question_to_consignment_submit = (By.XPATH, "//div[6]/div[2]/form/div[2]/div[2]/div/button")
    _submit_offer_button = (By.XPATH, "//button")
    _price = (By.ID, "AddOffer_price")
    _minimum_price = (By.ID, "AddOffer_priceMin")
    _transport_kind_dropdown = (By.XPATH, "//form/div/div[2]/div/div/div")
    _random_transport_kind_button = (By.XPATH, "//div[2]/div/div/div[2]/div[%s]"%randint(1,4))
    _description_field = (By.ID, "AddOffer_description")
    _description_value = get_random_string(5)+" "+get_random_string(6)+" "+get_random_string(7)
    _month = (By.LINK_TEXT, str(datetime.date.today().month))
    _date_from_field = (By.ID, "AddOffer_pickUpDateStart")
    _date_from = str(datetime.date.today().year)+"-"+str(datetime.date.today().month)+"-"+str(datetime.date.today().day)
    _date_to_field = (By.ID, "AddOffer_pickUpDateEnd")
    _date_to = str(datetime.date.today().year)+"-"+str(datetime.date.today().month)+"-"+str(datetime.date.today().day)
    _date_to_next_month = str(datetime.date.today().year)+"-"+str(datetime.date.today().month+1)+"-01"
    _transport_period = (By.ID, "AddOffer_transportDuration")
    _submit_offer_confirm = (By.ID, "AddOffer_save")
    _expiration_date_field = (By.ID, "AddOffer_endDate")
    _expiration_date = str(datetime.date.today().year)+"-"+str(datetime.date.today().month)+"-"+str(datetime.date.today().day)+" 12:30"
    _watch_consignment_link = (By.PARTIAL_LINK_TEXT, u"Obserwuj ogłoszenie")
    _offer_details = (By.XPATH, "//td[6]")
    _reject_offer_button = (By.XPATH, "//div[2]/div[2]/div/div/a")
    # _reject_offer_confirm = (By.LINK_TEXT, "Odrzuć ofertę")
    _reject_offer_confirm = (By.XPATH, "//div[2]/div/div/form/input")
    _add_question_button = (By.PARTIAL_LINK_TEXT, u"Wyślij wiadomość")
    _question_content = (By.ID, "AddOfferMessage_message")
    _add_question_confirm = (By.ID, "AddOfferMessage_send")
    _add_question_to_consignment_button = (By.ID, "ask-question")
    _consignment_question_content = (By.ID, "AddAuctionMessage_message")
    _consignment_question_confirm = (By.ID, "AddAuctionMessage_send")
    _consignment_question_reply_content = (By.NAME, "content")
    _consignment_question_reply_confirm = (By.XPATH, "//input[@value='Odpowiedz']")
    _accept_offer_button = (By.XPATH, "//div[2]/div/div[2]/a")
    _accept_offer_button2 = (By.LINK_TEXT, u"Akceptuję ofertę")

    def report_violation_to_consignmeent(self):
        self.click(self._consignment_violation_flag)
        self.clear_field_and_send_keys("This is my report", self._violation_content)
        self.click(self._violation_submit)

    def report_violation_to_offer(self):
        self.click(self._offer_details)
        sleep(1)
        self.click(self._offer_violation_flag)
        self.clear_field_and_send_keys("This is my report", self._violation_to_offer_content_field)
        self.click(self._violation_to_offer_submit)

    def report_violation_to_question_to_offer(self):
        self.click(self._offer_details)
        self.click(self._question_to_offer_violation_flag)
        self.clear_field_and_send_keys("This is my report", self._violation_to_question_to_offer_content_field)
        self.click(self._violation_to_question_to_offer_submit)

    def report_violation_to_question_to_consignment(self):
        self.click(self._question_to_consignment_violation_flag)
        self.clear_field_and_send_keys("This is my report", self._violation_to_question_to_consignment_content_field)
        self.click(self._violation_to_question_to_consignment_submit)

    def submit_offer(self):
        sleep(2)
        self.click(self._submit_offer_button)
        self.send_keys("111", self._price)
        self.send_keys("22", self._minimum_price)
        self.click(self._transport_kind_dropdown)
        self.click(self._random_transport_kind_button)
        self.clear_field_and_send_keys(self._description_value, self._description_field)
        self.clear_field_and_send_keys(self._expiration_date, self._expiration_date_field)
        self.clear_field_and_send_keys(self._date_from, self._date_from_field)
        if str(datetime.date.today().day) == 29:
            self.clear_field_and_send_keys(self._date_to_next_month, self._date_to_field)
        elif str(datetime.date.today().day) == 30:
            self.clear_field_and_send_keys(self._date_to_next_month, self._date_to_field)
        elif str(datetime.date.today().day) == 31:
            self.clear_field_and_send_keys(self._date_to_next_month, self._date_to_field)
        elif str(datetime.date.today().month) == 2 and str(datetime.date.today().day) == 28:
            self.clear_field_and_send_keys(self._date_to_next_month, self._date_to_field)
        else:
            self.clear_field_and_send_keys(self._date_to, self._date_to_field)
        self.send_keys("2", self._transport_period)

    def confirm_submit_offer(self):
        self.click(self._submit_offer_confirm)

    def watch_consignment(self):
        self.click(self._watch_consignment_link)

    def reject_offer(self):
        self.click(self._offer_details)
        sleep(2)
        self.click(self._reject_offer_button)
        self.click(self._reject_offer_confirm)

    def add_question_to_offer(self):
        self.click(self._offer_details)
        sleep(2)
        self.click(self._add_question_button)
        self.send_keys("This is my question", self._question_content)
        self.click(self._add_question_confirm)

    def reply_to_question(self):
        self.click(self._add_question_button)
        self.send_keys("This is my answer", self._question_content)
        self.click(self._add_question_confirm)

    def provider_add_question_to_consignment(self):
        self.click(self._add_question_to_consignment_button)
        self.send_keys("This is my question", self._consignment_question_content)
        self.click(self._consignment_question_confirm)

    def reply_to_provider_question_to_consignment(self):
        self.clear_field_and_send_keys("This is my reply", self._consignment_question_reply_content)
        self.click(self._consignment_question_reply_confirm)

    def accept_offer(self):
        self.click(self._offer_details)
        sleep(2)
        self.condition_click(self._accept_offer_button)
        self.click(self._accept_offer_button2)

# coding=utf-8
import datetime
import time
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
    _violation_submit = (By.ID, "user_complaint_submit")
    _violation_to_offer_content_field = (By.XPATH, "//div[8]/div[2]/form/div/textarea")
    _violation_to_offer_submit = (By.XPATH, "//div[8]/div[2]/form/div[2]/div[2]/div/button")
    _violation_to_question_to_offer_content_field = (By.XPATH, "//div[9]/div[2]/form/div/textarea")
    _violation_to_question_to_offer_submit = (By.XPATH, "//div[9]/div[2]/form/div[2]/div[2]/div/button")
    _violation_to_question_to_consignment_content_field = (By.XPATH, "//div[6]/div[2]/form/div/textarea")
    _violation_to_question_to_consignment_submit = (By.XPATH, "//div[6]/div[2]/form/div[2]/div[2]/div/button")
    _submit_offer_button = (By.XPATH, "//button")
    _price = (By.ID, "AddOffer_price")
    _minimum_price = (By.ID, "AddOffer_priceMin")
    _transport_kind_dropdown = (By.XPATH, "//form/div/div[3]/div/div")
    _random_transport_kind_button = (By.XPATH, "//div[3]/div/div/div[2]/div[%s]"%randint(1,4))
    _description_field = (By.ID, "AddOffer_description")
    _description_value = get_random_string(5)+" "+get_random_string(6)+" "+get_random_string(7)
    _month = (By.LINK_TEXT, str(datetime.date.today().month))
    _date_from_field = (By.ID, "AddOffer_pickUpDateStart")
    _date_from2 = str(datetime.date.today().year)+"-"+str(datetime.date.today().month)+"-"+str(datetime.date.today().day)
    _date_from = datetime.date.today().strftime('%Y-%m-%d')
    _date_from_first_10_days = str(datetime.date.today().year)+"-"+str(datetime.date.today().month)+"-0"+str(datetime.date.today().day)
    _date_to_field = (By.ID, "AddOffer_pickUpDateEnd")
    _date_to2 = str(datetime.date.today().year)+"-"+str(datetime.date.today().month)+"-"+str(datetime.date.today().day)
    _date_to = datetime.date.today().strftime('%Y-%m-%d')
    _date_to_first_10_days = str(datetime.date.today().year)+"-"+str(datetime.date.today().month)+"-0"+str(datetime.date.today().day)
    _date_to_next_month = str(datetime.date.today().year)+"-"+str(datetime.date.today().month+1)+"-01"
    _transport_period = (By.ID, "AddOffer_transportDuration")
    _submit_offer_confirm = (By.ID, "AddOffer_save")
    _expiration_date_field = (By.ID, "AddOffer_endDate")
    _expiration_date2 = str(datetime.date.today().year)+"-"+str(datetime.date.today().month)+"-"+str(datetime.date.today().day)+" 23:59"
    _expiration_date = datetime.date.today().strftime('%Y-%m-%d 23:59')
    _expiration_date_first_10_days2 = str(datetime.date.today().year)+"-"+str(datetime.date.today().month)+"-0"+str(datetime.date.today().day)+" 23:59"
    _watch_consignment_link = (By.PARTIAL_LINK_TEXT, u"Obserwuj ogłoszenie")
    _offer_details = (By.XPATH, "//td[6]")
    _reject_offer_button = (By.PARTIAL_LINK_TEXT, u"Odrzuć ofertę")
    _reject_offer_random_reason = (By.XPATH, "//div/div/div/div[%s]/div/label"%randint(1,6))
    _reject_offer_confirm = (By.ID, "RejectOffer_reject")
    _add_question_button = (By.PARTIAL_LINK_TEXT, u"Wyślij wiadomość")
    _question_content = (By.ID, "AddOfferMessage_message")
    _add_question_confirm = (By.ID, "AddOfferMessage_send")
    _add_question_to_consignment_button = (By.ID, "ask-question")
    _consignment_question_content = (By.ID, "AddAuctionMessage_message")
    _consignment_question_confirm = (By.ID, "AddAuctionMessage_send")
    _consignment_question_reply_content = (By.ID, "AddAuctionMessage_message")
    _consignment_question_reply_confirm = (By.ID, "AddAuctionMessage_send")
    _accept_offer_button = (By.XPATH, "//div[2]/div/div/a")
    _accept_offer_button2 = (By.LINK_TEXT, u"Akceptuję ofertę")

    def report_violation_to_consignmeent(self):
        self.click(self._consignment_violation_flag, "The consignment violation flag couldn't be clicked or didn't appear on consignment page")
        self.clear_field_and_send_keys("This is my report", self._violation_content, "The attempt to enter text into violation content field while adding violation to consignment was unsuccessful")
        self.click(self._violation_submit, "The add violation to consignment submit button couldn't be clicked or didn't appear on consignment page")

    def report_violation_to_offer(self):
        self.click(self._offer_details, "The offer details button couldn't be clicked or wasn't visible on consignment page")
        sleep(1)
        self.click(self._offer_violation_flag, "The offer violation flag couldn't be clicked or wasn't visible on consignment page")
        self.clear_field_and_send_keys("This is my report", self._violation_to_offer_content_field, "The attempt to enter text into violation content field while adding violation to offer was unsuccessful")
        self.click(self._violation_to_offer_submit, "The add violation to offer submit button couldn't be clicked or wasn't visible on consignment page")

    def report_violation_to_question_to_offer(self):
        self.click(self._offer_details, "The offer details button couldn't be clicked or wasn't visible on consignment page")
        self.click(self._question_to_offer_violation_flag, "The question to offer violation flag couldn't be clicked or wasn't visible on consignment page")
        self.clear_field_and_send_keys("This is my report", self._violation_to_question_to_offer_content_field, "The attempt to enter text into violation content field while adding violation to question to offer was unsuccessful")
        self.click(self._violation_to_question_to_offer_submit, "The add violation to question to offer submit button couldn't be clicked or wasn't visible on consignment page")

    def report_violation_to_question_to_consignment(self):
        self.click(self._question_to_consignment_violation_flag, "The question to consignment violation flag couldn't be clicked or wasn't visible on consignment page")
        self.clear_field_and_send_keys("This is my report", self._violation_to_question_to_consignment_content_field, "The attempt to enter text into violation content field while adding violation to question to consignment was unsuccessful")
        self.click(self._violation_to_question_to_consignment_submit, "The add violation to oconsignment submit button couldn't be clicked or wasn't visible on consignment page")

    def submit_offer(self):
        sleep(2)
        self.click(self._submit_offer_button, "THe submit offer button couldn't be clicked or wasn't found on consignment page")
        self.send_keys("111", self._price, "The attempt to enter price of offer into price field was unsuccessful")
        self.send_keys("22", self._minimum_price, "The attempt to enter minimum price of offer into minimum price field was unsuccessful")
        self.click(self._transport_kind_dropdown, "The transport kind dropdown couldn't be clicked or wasn't found on add offer page")
        self.condition_click(self._random_transport_kind_button, "The random transport kind option on transport kind dropdown couldn't be clicked or wasn't found on add offer page")
        self.clear_field_and_send_keys(self._description_value, self._description_field, "The attempt to enter description value into description field on add offer page was unsuccessful")
        self.get_driver().execute_script("document.getElementById('AddOffer_endDate').removeAttribute('readonly',0);")
        self.clear_field_and_send_keys(self._expiration_date, self._expiration_date_field, "The attempt to enter expiration date into expiration date field on add offer page was unsuccessful")
        self.get_driver().execute_script("document.getElementById('AddOffer_pickUpDateStart').removeAttribute('readonly',0);")
        self.clear_field_and_send_keys(self._date_from, self._date_from_field, "The attempt to enter date <from> into date <from> field on add offer page was unsuccessful")
        self.get_driver().execute_script("document.getElementById('AddOffer_pickUpDateEnd').removeAttribute('readonly',0);")
        if str(datetime.date.today().day) == 29:
            self.clear_field_and_send_keys(self._date_to_next_month, self._date_to_field, "The attempt to enter date <to> into date <to> field on add offer page was unsuccessful")
        elif str(datetime.date.today().day) == 30:
            self.clear_field_and_send_keys(self._date_to_next_month, self._date_to_field, "The attempt to enter date <to> into date <to> field on add offer page was unsuccessful")
        elif str(datetime.date.today().day) == 31:
            self.clear_field_and_send_keys(self._date_to_next_month, self._date_to_field, "The attempt to enter date <to> into date <to> field on add offer page was unsuccessful")
        elif str(datetime.date.today().month) == 2 and str(datetime.date.today().day) == 28:
            self.clear_field_and_send_keys(self._date_to_next_month, self._date_to_field, "The attempt to enter date <to> into date <to> field on add offer page was unsuccessful")
        else:
            self.clear_field_and_send_keys(self._date_to, self._date_to_field, "The attempt to enter date <to> into date <to> field on add offer page was unsuccessful")
        self.send_keys("2", self._transport_period, "The attempt to enter <2> into transport period field on add offer page was unsuccessful")

    def confirm_submit_offer(self):
        self.click(self._submit_offer_confirm, "The submit offer confirm button on add offer page wasn't visible")

    def watch_consignment(self):
        self.click(self._watch_consignment_link, "The watch consignment link on consignment page wasn't visible")

    def reject_offer(self):
        self.click(self._offer_details, "The offer details button couldn't be clicked or wasn't visible on consignment page")
        sleep(2)
        self.click(self._reject_offer_button, "The reject offer button in offer details on consignment page wasn't visible")
        self.click(self._reject_offer_confirm, "The reject offer confirm button in offer details on consignment page wasn't visible")

    def add_question_to_offer(self):
        self.click(self._offer_details, "The offer details button couldn't be clicked or wasn't visible on consignment page")
        sleep(2)
        self.click(self._add_question_button, "The add question to offer button in offer details on consignment page wasn't visible")
        self.send_keys("This is my question", self._question_content, "The attempt to enter question to offer content on consignment page was unsuccessful")
        self.click(self._add_question_confirm, "The add question to offer confirm button in offer details on consignment page wasn't visible")

    def reply_to_question(self):
        self.click(self._add_question_button, "The add question to offer button in offer details on consignment page wasn't visible")
        self.send_keys("This is my answer", self._question_content, "The attempt to enter question to offer content on consignment page was unsuccessful")
        self.click(self._add_question_confirm, "The add question to offer confirm button in offer details on consignment page wasn't visible")

    def provider_add_question_to_consignment(self):
        self.click(self._add_question_to_consignment_button, "The add question to consignment button on consignment page wasn't visible")
        self.send_keys("This is my question", self._consignment_question_content, "The attempt to enter question to consignment content on consignment page was unsuccessful")
        self.click(self._consignment_question_confirm, "The add question to consignment confirm button on consignment page wasn't visible")

    def reply_to_provider_question_to_consignment(self):
        self.clear_field_and_send_keys("This is my reply", self._consignment_question_reply_content, "The attempt to enter reply to question to consignment content on consignment page was unsuccessful")
        self.click(self._consignment_question_reply_confirm, "The reply to question to consignment confirm button on consignment page wasn't visible")

    def accept_offer(self):
        self.click(self._offer_details, "The offer details button couldn't be clicked or wasn't visible on consignment page")
        sleep(2)
        self.condition_click(self._accept_offer_button, "The accept offer button on consignment page wasn't visible or couldn't be clicked")
        sleep(2)
        self.click(self._accept_offer_button2, "The accept offer confirm button on consignment page wasn't visible or couldn't be clicked")

    def show_offer_details(self):
        self.click(self._offer_details, "The offer details button couldn't be clicked or wasn't visible on consignment page")

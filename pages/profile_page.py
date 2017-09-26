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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



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
    _my_data_country_dropdown = (By.XPATH, "//div[6]/div/input")
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
    _company_data_save_button = (By.CSS_SELECTOR, "html.no-js body div.ui.container.main-container div.ui.stackable.grid div.twelve.wide.column div.ui.bottom.attached.segment.company-details form.ui.form div button#company_details_submit.ui.large.primary.button")
    _my_data_tab = (By.XPATH, "//div[2]/div/a[2]")
    _company_data_tab = (By.XPATH, "//div[2]/div/a[3]")
    _notification_settings_tab = (By.LINK_TEXT, "Ustawienia powiadomień")
    _change_password_tab = (By.PARTIAL_LINK_TEXT, "Zmiana hasła")
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
    _company_upload_file_button = (By.XPATH, '//*[@id="lcn-file-uploader-1"]/div/div[2]/input')
    _company_uploaded_file_button = (By.XPATH, '//*[@id="lcn-file-uploader-1"]/div/ul/li/div/img')
    _random_notification_period_radio = (By.XPATH, "//div[%s]/div/label"%randint(2,6))
    _notification_category_custom_radio = (By.XPATH, "//div[2]/div/div/div/label")
    _notification_category_dropdown = (By.XPATH, "//div/div/div[2]/div[2]/div/div")
    _remove_first_notification_category_button = (By.XPATH, "//div[2]/div/div/a/i")
    _random_notification_category = (By.XPATH, "//div[2]/div[%s]"%randint(3,9))
    _notifications_countries_custom_radio = (By.XPATH, "//div[3]/div/div/div/label")
    _remove_first_country_button = (By.XPATH, "//div[6]/div/div/a/i")
    _notifications_countries_custom_dropdown = (By.XPATH, "//div[3]/div[2]/div/div")
    _random_notifications_countries_custom_button = (By.XPATH, "//div[%s]"%randint(12,234))
    _save_notifications_button = (By.XPATH, "//button")
    _change_password_old_field = (By.ID, "user_change_password_oldPassword")
    _change_password_new_field = (By.ID, "user_change_password_newPassword_first")
    _change_password_new2_field = (By.ID, "user_change_password_newPassword_second")
    _change_password_submit = (By.ID, "user_change_password_submit")
    _my_consignments_menu = (By.XPATH, "//a[3]/h4")
    _ended_transactions_tab = (By.PARTIAL_LINK_TEXT, u"Zakończone transakcją")
    _first_ended_transaction_send_commentary_button = (By.PARTIAL_LINK_TEXT, "Wystaw komentarz")
    _first_ended_transaction_commentary_random_type = (By.XPATH, "//form/div/div/div[2]/div[%s]" %randint(1,3))
    _first_ended_transaction_commentary_content = (By.ID, "user_opinion_content")
    _first_ended_transaction_submit_commentary_button = (By.XPATH, "/html/body/div[10]/div[1]/div[3]/div[2]")
    _commentaries_menu = (By.XPATH, "//a[5]/h4")
    _first_transaction_send_commentary_button = (By.XPATH, "//div[3]/div/a")
    _first_transaction_random_commentary_type_button = (By.XPATH, "//form/div/div/div[2]/div[%s]"%randint(1,3))
    _first_transaction_negative_commentary_type_button = (By.XPATH, "//form/div/div/div[2]/div[2]")
    _first_transaction_commentary_content = (By.ID, "user_opinion_content")
    _first_transaction_submit_commentary_button = (By.XPATH, "/html/body/div[10]/div[1]/div[3]/div[2]")
    _first_transaction_commentary_mark_dropdown = (By.NAME, "mark")
    _provider_commentaries_menu = (By.XPATH, "//a[7]/h4")
    _provider_received_commentaries_tab = (By.PARTIAL_LINK_TEXT, u"Otrzymane komentarze")
    _provider_sent_commentaries_tab = (By.PARTIAL_LINK_TEXT, u"Wystawione komentarze")
    _provider_first_sent_commentary_field = (By.XPATH, "//div[3]/div/p")
    _provider_first_sent_commentary_consignment_uuid = (By.XPATH, "//strong")
    _provider_reply_to_negative_commentary_button = (By.XPATH, "//td[5]/a")
    _provider_reply_to_negative_commentary_content = (By.XPATH, "//textarea[@id='content']")
    _provider_reply_to_negative_commentary_submit_button = (By.XPATH, "(//input[@value='OK'])[3]")
    _provider_send_commentary_button = (By.XPATH, "//div[3]/div/a")
    _provider_send_random_commentary_type_button = (By.XPATH, "//form/div/div/div[2]/div[%s]"%randint(1,3))
    _provider_send_commentary_content = (By.ID, "user_opinion_content")
    _provider_send_commentary_submit_button = (By.XPATH, "/html/body/div[10]/div[1]/div[3]/div[2]")
    _first_consignment_edit = (By.XPATH, "//div[2]/div/div/a")
    _first_consignment_withdraw = (By.PARTIAL_LINK_TEXT, "Wycofaj ogłoszenie")
    _withdraw_frame = (By.CLASS_NAME, "ui small modal transition visible active scrolling")
    _random_withdraw_cause = (By.XPATH, "//div[%s]/div/label"%randint(2,5))
    _withdraw_consignment_submit = (By.CSS_SELECTOR, "html.no-js body.dimmable.dimmed.scrolling div.ui.dimmer.modals.page.transition.visible.active div.ui.small.modal.scrolling.transition.visible.active div.content form.ui.form div.ui.basic.segment button#RejectAuction_reject.ui.right.floated.primary.button")
    _first_consignment_enter = (By.XPATH, "//div[2]/p/a")
    _withdraw_first_offer = (By.PARTIAL_LINK_TEXT, u"Wycofaj ofertę")
    _withdraw_first_offer_confirm = (By.LINK_TEXT, u"Wycofaj")
    _unactual_tab = (By.PARTIAL_LINK_TEXT, u"Nieaktualne")
    _my_offers_menu = (By.XPATH, "//a[3]/h4")
    _first_consignment_issue_again = (By.XPATH, "//a[contains(text(),'Wystaw ponownie')]")
    _accepted_tab = (By.PARTIAL_LINK_TEXT, "Zaakceptowane")
    _my_offers_send_commentary_button = (By.XPATH, "//a[contains(text(),'Wystaw komentarz')]")
    _my_offers_commentary_content = (By.ID, "user_opinion_content")
    _my_offers_commentary_submit_button = (By.XPATH, "/html/body/div[10]/div[1]/div[3]/div[2]")
    _random_commentary_type_button = (By.XPATH, "//form/div/div/div[2]/div[%s]"%randint(1,3))
    _set_executed_link = (By.PARTIAL_LINK_TEXT, "Ustaw jako ZREALIZOWANA")
    _set_executed_submit = (By.XPATH, "//div[2]/div/div[2]/a")
    _commission_payback_tab = (By.PARTIAL_LINK_TEXT, u"Zwroty prowizji")
    _commission_payback_request_link = (By.XPATH, "//td[6]/div/div[2]/a")
    _commission_reason_field = (By.CSS_SELECTOR, "html.no-js body.dimmable.dimmed.scrolling div.ui.dimmer.modals.page.transition.visible.active div.ui.modal.transition.visible.active.scrolling div.content form.ui.form div.ui.segments div.ui.horizontal.segments.grid div.ui.segment.seven.wide.column div.field textarea#AddRefund_descriptionCompany")
    _commission_confirmation_button = (By.CSS_SELECTOR, "html.no-js body.dimmable.dimmed.scrolling div.ui.dimmer.modals.page.transition.visible.active div.ui.modal.transition.visible.active.scrolling div.actions div.ui.primary.button")
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
    _provider_remove_first_country_button = (By.XPATH, "//div[6]/div/div/a/i")
    _provider_country_dropdown = (By.XPATH, "//form/div[6]/div/div")
    _provider_random_country_button = (By.XPATH, "//div[%s]" %randint(12,234))
    _remove_first_car_button = (By.XPATH, "//div[7]/div/div/div[4]/a")
    _add_car_button = (By.LINK_TEXT, "Dodaj pojazd")
    _first_car_type_dropdown = (By.XPATH, "//form/div[7]/div/div/div/div")
    _random_first_car_type_button = (By.XPATH, "//div/div/div/div/div[2]/div[%s]"%randint(2, 16))
    _first_car_capacity_dropdown = (By.XPATH, "//div[7]/div/div/div[2]/div")
    _random_first_car_capacity_button = (By.XPATH, "//div[2]/div/div[2]/div[%s]"%randint(1, 6))
    _first_car_number_field = (By.ID, "company_profile_vehicles_0_quantity")
    _first_car_number_value = randint(1,4)
    _second_car_type_dropdown = (By.XPATH, "//div[7]/div/div[2]/div/div")
    _random_second_car_type_button = (By.XPATH, "//div/div[2]/div/div/div[2]/div[%s]"%randint(2, 16))
    _second_car_capacity_dropdown = (By.XPATH, "//div[7]/div/div[2]/div[2]/div")
    _random_second_car_capacity_button = (By.XPATH, "//div[2]/div[2]/div/div[2]/div[%s]"%randint(1, 6))
    _second_car_number_field = (By.ID, "company_profile_vehicles_1_quantity")
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
    _user_first_link_reply_to_question = (By.XPATH, "//td[2]/a")
    _provider_data_saved_name = (By.XPATH, "//td[2]")
    _provider_data_saved_tel = (By.XPATH, "//tr[3]/td[2]")
    _provider_data_saved_kom = (By.ID, "user_edit_phone")
    _provider_data_saved_mail = (By.XPATH, "//tr[2]/td[2]")
    _provider_data_saved_www = (By.XPATH, "//tr[6]/td[2]")
    _provider_data_saved_address = (By.XPATH, "//tr[5]/td[2]")
    _ask_for_offers_button = (By.XPATH, "//div[2]/div[3]/div/div/a")
    _first_offer = (By.XPATH, "//button")
    _first_consignment_distinguish_button = (By.XPATH, "//td[5]/a")
    _provider_first_consignment_distinguish_button = (By.XPATH, "//td[5]/a")
    _set_highlited_checkbox = (By.NAME, "auction_special")
    _set_urgent_checkbox = (By.NAME, "auction_important")
    _submit_distinguish_consignment = (By.ID, "add_auction_button")
    # _provider_my_consignments_menu = (By.XPATH, "//div[6]/div/div/ul/li[4]/a")
    _provider_my_consignments_menu = (By.PARTIAL_LINK_TEXT, u"Moje przesyłki")
    _executed_result_field = (By.XPATH, "//div[@class='ui success message']")
    _changes_saved_field = (By.XPATH, "//div[9]/div")

    def __init__(self, driver):
        super(ProfilePage, self).__init__(driver, self._title)

    def edit_user_profile(self):
        self.click(self._edit_profile_button, "The edit profile button couldn't be clicked or wasn't visible on user profile page")
        self.clear_field_and_send_keys(self._change_name, self._name_field, "The attempt to enter new name into name field on user edit profile page was unsuccessful")
        self.clear_field_and_send_keys(self._change_email, self._email_field, "The attempt to enter new email into email field on user edit profile page was unsuccessful")
        self.clear_field_and_send_keys(self._change_phone, self._phone_field, "The attempt to enter new phone number into phone field on user edit profile page was unsuccessful")
        self.click(self._language_dropdown, "The language dropdown couldn't be clicked or waesn't visible on user edit profile page")
        self.click(self._language_polish, "The language <Polish> on language dropdown couldn't be clicked or waesn't visible on user edit profile page")
        self.click(self._my_data_country_dropdown, "The my data country dropdown couldn't be clicked or waesn't visible on user edit profile page")
        self.get_driver().execute_script("return arguments[0].scrollIntoView();", self.find_element(self._random_country_button))
        self.condition_click(self._random_country_button, "The random country button on country dropdown couldn't be clicked or waesn't visible on user edit profile page")
        self.clear_field_and_send_keys(self._change_street, self._street_field, "The attempt to enter new street name into street field on user edit profile page was unsuccessful")
        self.clear_field_and_send_keys(self._change_building_number, self._building_number_field, "The attempt to enter new building number into building number field on user edit profile page was unsuccessful")
        self.clear_field_and_send_keys(self._change_postal_code, self._postal_code_field, "The attempt to enter new postal code into postal code field on user edit profile page was unsuccessful")
        self.clear_field_and_send_keys(self._change_city, self._city_field, "The attempt to enter new city into city field on user edit profile page was unsuccessful")
        self.condition_click(self._save_button, "The attempt to click save button on user edit profile page was unsuccessful")

    def edit_consignment(self):
        self.click(self._my_consignments_menu, "The consignments menu in user profile couldn't be clicked or wasn't visible")
        self.click(self._first_consignment_edit, "The first consignment edit button in my consignments menu in user profile couldn't be clicked or wasn't visible")
        return AddConsignmentPage(self.get_driver())

    def withdraw_consignment(self):
        self.click(self._my_consignments_menu, "The consignments menu in user profile couldn't be clicked or wasn't visible")
        self.click(self._first_consignment_withdraw, "The first consignment withdraw button in my consignments menu in user profile couldn't be clicked or wasn't visible")
        sleep(1)
        # self.get_driver().switch_to.frame(self.find_element(self._withdraw_frame))
        self.click2(self._random_withdraw_cause)
        # self.click(self._random_withdraw_cause, "Trying to click random withdraw cause button while withdrawing consignment from user profile was usnsuccessful")
        # self.get_driver().execute_script("return arguments[0].scrollIntoView(false);", self.find_element(self._withdraw_consignment_submit))
        self.click2(self._withdraw_consignment_submit)
        # self.click(self._withdraw_consignment_submit, "The withdraw consignment submit button couldn't be clicked or wasn't visible in user profile")

    def open_first_auction(self):
        self.condition_click(self._my_consignments_menu, "The consignments menu in user profile couldn't be clicked or wasn't visible")
        self.click(self._first_consignment_enter, "The first auction in my consignments menu in user profile couldn't be clicked or wasn't visible")
        return ConsignmentPage(self.get_driver())

    def withdraw_offer(self):
        self.click(self._my_offers_menu, "The my offers menu in user profile couldn't be clicked or wasn't visible")
        self.click(self._withdraw_first_offer, "The first offer withdraw button in my offers menu in user profile couldn't be clicked or wasn't visible")
        self.click(self._withdraw_first_offer_confirm, "The first offer withdraw confirm button in my offers menu in user profile couldn't be clicked or wasn't visible")
        sleep(2)

    def issue_consignment_again(self):
        self.click(self._my_consignments_menu, "The consignments menu in user profile couldn't be clicked or wasn't visible" )
        self.click(self._unactual_tab, "The unactual tab in my consignments menu in user profile couldn't be clicked or wasn't visible")
        self.click(self._first_consignment_issue_again, "The first consignment issue again button in unactual tab in my consignments menu in user profile couldn't be clicked or wasn't visible")
        return AddConsignmentPage(self.get_driver())

    def payback_commission(self):
        self.click(self._my_offers_menu, "The my offers menu in user profile couldn't be clicked or wasn't visible")
        self.click(self._commission_payback_tab, "The commission payback tab in my offers menu in user profile couldn't be clicked or wasn't visible")
        self.click(self._commission_payback_request_link, "The commission payback request link in my offers menu in user profile couldn't be clicked or wasn't visible")
        # self.get_driver().execute_script("return arguments[0].scrollIntoView(true);", self.find_element(self._commission_reason_field))
        self.send_keys_to_element(self.find_element(self._commission_reason_field), get_random_string(10))
        # self.send_keys(get_random_string(10), self._commission_reason_field, "THe attempt to enter random commission payback reason was unsuccessful")
        # self.get_driver().execute_script("return arguments[0].scrollIntoView(true);", self.find_element(self._commission_confirmation_button))
        self.condition_click(self._commission_confirmation_button, "The commission payback confirmation button in my offers menu in user profile couldn't be clicked or wasn't visible")

    def edit_provider_profile(self):
        self.click(self._provider_profile_button, "The provider edit profile button couldn't be clicked or wasn't visible in provider profile")
        while True:
            try:
                self.click(self._remove_first_category_button, "Remove first category button is not clickable on edit provider profile page", 2)
            except TimeoutException:
                break
        self.click(self._category_dropdown, "The category dropdown couldn't be clicked or wasn't visible on edit provider profile page")
        self.get_driver().execute_script("return arguments[0].scrollIntoView();", self.find_element(self._random_category_button))
        self.click(self._random_category_button, "The random category button on category dropdown couldn't be clicked or wasn't visible on edit provider profile page")
        while True:
            try:
                self.click(self._remove_first_country_button, "Remove first country button is not clickable on edit provider profile page", 2)
            except TimeoutException:
                break
        self.click(self._provider_country_dropdown, "The provider country dropdown couldn't be clicked or wasn't visible on edit provider profile page")
        self.condition_click(self._provider_random_country_button, "The random country button on provider country dropdown couldn't be clicked or wasn't visible on edit provider profile page")
        while True:
            try:
                self.click(self._remove_first_route_button, "Remove first route button is not clickable on edit provider profile page", 2)
            except TimeoutException:
                break
        self.click(self._add_route_button, "The add route button couldn't be clicked or wasn't visible on edit provider profile page")
        self.clear_field_and_send_keys(self._route_from_value, self._route_from_field, "The attempt to enter route from value into route from field on edit provider profile page was unsuccessful")
        self.click(self._route_from_field, "The route from field couldn't be clicked or wasn't visible on edit provider profile page")
        self.clear_field_and_send_keys(self._route_to_value, self._route_to_field, "The attempt to enter route to value into route to field on edit provider profile page was unsuccessful")
        self.click(self._route_to_field, "The route to field couldn't be clicked or wasn't visible on edit provider profile page")
        self.click(self._add_route_both_sides_checkbox, "The add route both sides checkbox couldn't be clicked or wasn't visible on edit provider profile page")
        while True:
            try:
                self.click(self._remove_first_accepted_form_of_payment_button, "Remove first accepted form of payment button is not clickable on edit provider profile page", 2)
            except TimeoutException:
                break
        self.click(self._accepted_form_of_payment_dropodown, "The accepted form of payment dropdown couldn't be clicked or wasn't visible on edit provider profile page")
        self.click(self._random_accepted_form_of_payment_button, "The random accepted form of payment on dropdown couldn't be clicked or wasn't visible on edit provider profile page")
        sleep(2)
        while True:
            try:
                self.click(self._remove_first_car_button, "Remove first car button is not clickable on edit provider profile page", 2)
            except TimeoutException:
                break
        self.click(self._add_car_button, "The add car button couldn't be clicked or wasn't visible on edit provider profile page")
        self.click(self._first_car_type_dropdown, "The first car type dropdown couldn't be clicked or wasn't visible on edit provider profile page")
        self.condition_click(self._random_first_car_type_button, "The random first car type button on first car type dropdown couldn't be clicked or wasn't visible on edit provider profile page")
        self.click(self._first_car_capacity_dropdown, "The first car capacity dropdown couldn't be clicked or wasn't visible on edit provider profile page")
        self.click(self._random_first_car_capacity_button, "The first car capacity button on car capacity dropdown couldn't be clicked or wasn't visible on edit provider profile page")
        self.clear_field_and_send_keys(self._first_car_number_value, self._first_car_number_field, "The attempt to enter first car number value into first car number field on edit provider profile page was unsuccessful")
        sleep(2)
        self.click(self._add_car_button, "The add car button couldn't be clicked or wasn't visible on edit provider profile page")
        self.click(self._second_car_type_dropdown, "The second car type dropdown couldn't be clicked or wasn't visible on edit provider profile page")
        self.click(self._random_second_car_type_button, "The random second car type button on second car type dropdown couldn't be clicked or wasn't visible on edit provider profile page")
        self.click(self._second_car_capacity_dropdown, "The second car capacity dropdown couldn't be clicked or wasn't visible on edit provider profile page")
        sleep(1)
        self.click(self._random_second_car_capacity_button, "The second car capacity button on car capacity dropdown couldn't be clicked or wasn't visible on edit provider profile page")
        self.clear_field_and_send_keys(self._second_car_number_value, self._second_car_number_field, "The attempt to enter second car number value into second car number field on edit provider profile page was unsuccessful")
        self.clear_field_and_send_keys(self._company_description_value, self._company_description_field, "The attempt to enter company description value into company description field on edit provider profile page was unsuccessful")
        self.click(self._random_transport_profile, "The random transport profile button couldn't be clicked or wasn't visible on edit provider profile page")
        self.click(self._company_kind_dropdown, "The company kind dropdown couldn't be clicked or wasn't visible on edit provider profile page")
        self.click(self._random_company_kind_button, "The random company kind button on company kind dropdown couldn't be clicked or wasn't visible on edit provider profile page")
        sleep(2)
        self.click(self._issue_VAT_NP_invoices_dropdown, "The issue VAT NP invoices dropdown couldn't be clicked or wasn't visible on edit provider profile page")
        self.click(self._random_issue_VAT_NP_invoices_button, "The random issue VAT NP invoices button on issue VAT NP invoices dropdown couldn't be clicked or wasn't visible on edit provider profile page")
        self.condition_click(self._issue_VAT_invoices_dropdown, "The issue VAT invoices dropdown couldn't be clicked or wasn't visible on edit provider profile page")
        self.click(self._random_issue_VAT_invoices_button, "The random issue VAT invoices button on issue VAT invoices dropdown couldn't be clicked or wasn't visible on edit provider profile page")
        self.clear_field_and_send_keys(get_random_integer(1), self._employee_number_field, "The attempt to enter random integer into employee number field on edit provider profile page was unsuccessful")
        self.clear_field_and_send_keys(get_random_integer(1), self._driver_number_field, "The attempt to enter random integer into driver number field on edit provider profile page was unsuccessful")
        self.clear_field_and_send_keys(self._company_creation_year_value, self._company_creation_year_field, "The attempt to enter company creation year value into company creation year field on edit provider profile page was unsuccessful")
        self.click(self._save_changes, "The save changes button couldn't be clicked or wasn't visible on edit provider profile page")

    def edit_provider_data(self):
        self.click(self._provider_profile_button, "The provider edit profile button couldn't be clicked or wasn't visible in provider profile")
        self.click(self._my_data_tab, "The my data tab couldn't be clicked or wasn't visible on edit provider profile page")
        self.clear_field_and_send_keys(self._change_name, self._name_field, "The attempt to enter new name into name field on provider edit data page was unsuccessful")
        self.clear_field_and_send_keys(self._change_email, self._email_field, "The attempt to enter new email into email field on provider edit data page was unsuccessful")
        self.clear_field_and_send_keys(self._change_phone, self._phone_field, "The attempt to enter new phone into phone field on provider edit data page was unsuccessful")
        self.click(self._save_button, "The save changes button couldn't be clicked or wasn't visible on edit provider data page")

    def edit_provider_company_data(self):
        self.condition_click(self._provider_profile_button, "The provider edit profile button couldn't be clicked or wasn't visible in provider profile")
        self.click(self._company_data_tab, "The company data tab couldn't be clicked or wasn't visible on edit provider profile page")
        self.clear_field_and_send_keys(get_random_string(10), self._company_name, "The attempt to enter random string into company name field on provider edit company data page was unsuccessful")
        self.clear_field_and_send_keys(get_random_string(10), self._company_krs, "The attempt to enter random string into company krs field on provider edit company datapage was unsuccessful")
        self.clear_field_and_send_keys(get_random_integer(10), self._company_nip, "The attempt to enter random integer into company nip field on provider edit company data page was unsuccessful")
        self.clear_field_and_send_keys(self._change_phone, self._company_mobile, "The attempt to enter random integer into company mobile number field on provider edit company data page was unsuccessful")
        self.click(self._company_country_dropdown, "The company country dropdown couldn't be clicked or wasn't visible on edit provider company data page")
        self.get_driver().execute_script("return arguments[0].scrollIntoView();", self.find_element(self._random_company_country_button))
        self.click(self._random_company_country_button, "The random country on company country dropdown couldn't be clicked or wasn't visible on edit provider company data page")
        self.clear_field_and_send_keys(self._change_street, self._company_street, "The attempt to enter random string into company street field on provider edit company data page was unsuccessful")
        self.clear_field_and_send_keys(get_random_integer(2), self._company_building, "The attempt to enter random integer into company building number field on provider edit company data page was unsuccessful")
        self.clear_field_and_send_keys(get_random_string(9), self._company_city, "The attempt to enter random string into company city field on provider edit company data page was unsuccessful")
        self.clear_field_and_send_keys(self._change_postal_code, self._company_postal, "The attempt to enter random postal code into company postal code field on provider edit company data page was unsuccessful")
        self.clear_field_and_send_keys("www."+get_random_string(5)+".pl", self._company_www, "The attempt to enter random www address into company www field on provider edit company data page was unsuccessful")
        # self.send_keys_to_element(self.find_element(self._company_upload_file_button), os.path.join(os.path.abspath(''),"img.jpg"))
        # WebDriverWait(self.get_driver(), 20).until(EC.text_to_be_present_in_element(self._company_uploaded_file_button, ".jpg"), "File was not uploaded on provider edit company data page")
        # self.get_driver().execute_script("return arguments[0].scrollIntoView();", self.find_element(self._company_data_save_button))
        self.click(self._company_data_save_button)
        # self.click(self._company_data_save_button, "The company data save changes button couldn't be clicked or wasn't visible on edit provider company data page")

    def edit_provider_notifications(self):
        self.condition_click(self._provider_profile_button, "The provider edit profile button couldn't be clicked or wasn't visible in provider profile")
        self.click(self._notification_settings_tab, "The notification settings tab couldn't be clicked or wasn't visible on edit provider profile page")
        self.click(self._random_notification_period_radio, "The random notification period radio couldn't be clicked or wasn't visible on edit provider notifications page")
        self.click(self._notification_category_custom_radio, "The notification category custom radio couldn't be clicked or wasn't visible on edit provider notifications page")
        while True:
            try:
                self.click(self._remove_first_notification_category_button, "Remove first notification category button is not clickable on edit provider notifications page", 2)
            except TimeoutException:
                break
        self.click(self._notification_category_dropdown, "The notification category dropdown couldn't be clicked or wasn't visible on edit provider notifications page")
        self.condition_click(self._random_notification_category, "The random notification category on notification category dropdown couldn't be clicked or wasn't visible on edit provider notifications page")
        self.click(self._notifications_countries_custom_radio, "The notification countries custom radio couldn't be clicked or wasn't visible on edit provider notifications page")
        while True:
            try:
                self.click(self._remove_first_country_button, "Remove first country button is not clickable on edit provider notifications page", 2)
            except TimeoutException:
                break
        self.click(self._notifications_countries_custom_dropdown, "The notifications countries custom dropdown couldn't be clicked or wasn't visible on edit provider notifications page")
        self.get_driver().execute_script("return arguments[0].scrollIntoView(true);", self.find_element(self._random_notifications_countries_custom_button))
        self.condition_click(self._random_notifications_countries_custom_button, "The random notifications countries custom button on notifications countries custom dropdown couldn't be clicked or wasn't visible on edit provider notifications page")
        self.click(self._save_notifications_button, "The save notifications changes button couldn't be clicked or wasn't visible on edit provider notifications page")

    def change_password(self, file):
        self.click(self._edit_profile_button, "The edit profile button couldn't be clicked or wasn't visible on the page")
        self.click(self._change_password_tab, "The change password tab couldn't be clicked or wasn't visible on provider profile page")
        self.clear_field_and_send_keys(get_password(file), self._change_password_old_field, "The attempt to enter password from file into old password field on change password page was unsuccessful")
        change_password_value(file)
        self.clear_field_and_send_keys(get_password(file), self._change_password_new_field, "The attempt to enter password from file into new password field on change password page was unsuccessful")
        self.clear_field_and_send_keys(get_password(file), self._change_password_new2_field, "The attempt to enter password from file into repeat new password field on change password page was unsuccessful")
        self.click(self._change_password_submit, "The change password submit button couldn't be clicked or wasn't visible on change password page")

    def open_first_message(self):
        self.click(self._messages_menu, "The messages menu couldn't be clicked or wasn't visible on provider profile page")
        self.click(self._first_message, "The first message button couldn't be clicked or wasn't visible on messages menu on provider profile page")
        return ConsignmentPage(self.get_driver())

    def user_open_first_message(self):
        self.click(self._user_messages_menu, "The user messages menu couldn't be clicked or wasn't visible on user profile page")
        self.click(self._user_first_message, "The first message button couldn't be clicked or wasn't visible on messages menu on user profile page")
        return ConsignmentPage(self.get_driver())

    def user_click_reply_to_question(self):
        self.click(self._user_messages_menu, "The user messages menu couldn't be clicked or wasn't visible on user profile page")
        self.click(self._user_first_link_reply_to_question, "The first link to reply to question button couldn't be clicked or wasn't visible on messages menu on user profile page")
        return ConsignmentPage(self.get_driver())

    def make_offer_executed(self):
        self.click(self._my_offers_menu, "The my offers menu couldn't be clicked or wasn't visible on provider profile page")
        self.click(self._accepted_tab, "The accepted tab couldn't be clicked or wasn't visible in my offers menu on provider profile page")
        self.get_driver().execute_script("window.scrollTo(1100, 320);")
        self.click(self._set_executed_link, "The set executed link for first consignment couldn't be clicked or wasn't visible in my offers menu on provider profile page")
        sleep(2)
        self.click2(self._set_executed_submit)
        # self.click(self._set_executed_submit, "The set executed submit button for first consignment couldn't be clicked or wasn't visible in my offers menu on provider profile page")

    def provider_send_commentary_from_my_offers_menu(self):
        self.click(self._my_offers_menu, "The my offers menu couldn't be clicked or wasn't visible on provider profile page")
        self.click(self._accepted_tab, "The accepted tab couldn't be clicked or wasn't visible in my offers menu on provider profile page")
        self.get_driver().execute_script("window.scrollTo(1100, 320);")
        self.click(self._my_offers_send_commentary_button, "The send commentary button couldn't be clicked or wasn't visible in my offers menu on provider profile page")
        sleep(2)
        self.click2(self._random_commentary_type_button)
        # self.click(self._random_commentary_type_button, "The random commentary type button couldn't be clicked or wasn't visible in my offers menu on provider profile page while adding commentary")
        self.clear_field_and_send_keys("This is my commentary", self._my_offers_commentary_content, "The attempt to enter commentary content while adding commentary from my offers menu as provider was unsuccessful")
        self.click(self._my_offers_commentary_submit_button, "The commentary submit button in my offers menu in provider profile couldn't be clicked or wasn't visible")

    def provider_send_commentary_from_commentaries_menu(self):
        self.click(self._provider_commentaries_menu, "The commentaries menu couldn't be clicked or wasn't visible on provider profile page")
        self.get_driver().execute_script("window.scrollTo(1, 50);")
        self.click(self._provider_send_commentary_button, "The send commentary button for first consignment couldn't be clicked or wasn't visible in commentaries menu on provider profile page")
        sleep(2)
        self.click2(self._provider_send_random_commentary_type_button)
        # self.click(self._provider_send_random_commentary_type_button, "The random commentary type button for first consignment couldn't be clicked or wasn't visible in commentaries menu on provider profile page")
        sleep(2)
        self.send_keys("This is my commentary", self._provider_send_commentary_content)
        # self.send_keys_to_element(self.find_element(self._provider_send_commentary_content), "This is my commentary")
        # self.clear_field_and_send_keys("This is my commentary", self._provider_send_commentary_content, "The attempt to enter commentary content while adding commentary from commentaries menu as provider was unsuccessful")
        self.click(self._provider_send_commentary_submit_button, "The send commentary submit button for first consignment couldn't be clicked or wasn't visible in commentaries menu on provider profile page")

    def enter_provider_sent_commentaries_tab(self):
        self.click(self._provider_sent_commentaries_tab, "The sent commentaries tab couldn't be clicked or wasn't visible on provider profile page")

    def provider_reply_to_negative_commentary(self):
        self.click(self._provider_commentaries_menu, "The commentaries menu couldn't be clicked or wasn't visible on provider profile page")
        self.click(self._provider_received_commentaries_tab, "The received commentaries tab couldn't be clicked or wasn't visible on provider profile page")
        self.click(self._provider_reply_to_negative_commentary_button, "The reply to negative commentary button in received commentaries menu in provider profile couldn't be clicked or wasn't visible")
        self.clear_field_and_send_keys("This is my reply", self._provider_reply_to_negative_commentary_content, "The attempt to enter commentary content while replying to negative commentary commentary as provider was unsuccessful")
        self.click(self._provider_reply_to_negative_commentary_submit_button, "The reply to negative commentary submit button in received commentaries menu in provider profile couldn't be clicked or wasn't visible")

    def user_send_commentary_from_ended_transactions_menu(self):
        self.click(self._my_consignments_menu, "The my consignments menu in user profile couldn't be clicked or wasn't visible")
        self.click(self._ended_transactions_tab, "The ended transactions tab in my consignments menu in user profile couldn't be clicked or wasn't visible")
        self.click(self._first_ended_transaction_send_commentary_button, "first ended transaction send commentary button in my consignments menu in user profile couldn't be clicked or wasn't visible")
        self.click(self._first_ended_transaction_commentary_random_type)
        self.click(self._first_ended_transaction_commentary_random_type, "first ended transaction commentary random type in my consignments menu in user profile couldn't be clicked or wasn't visible")
        self.clear_field_and_send_keys("This is my commentary", self._first_ended_transaction_commentary_content, "The attempt to enter first ended transaction commentary content in user profile was unsuccessful")
        self.click(self._first_ended_transaction_submit_commentary_button, "first ended transaction submit commentary button in my consignments menu in user profile couldn't be clicked or wasn't visible")

    def user_send_commentary_from_commentaries_menu(self):
        self.click(self._commentaries_menu, "The commentaries menu in user profile couldn't be clicked or wasn't visible")
        self.click(self._first_transaction_send_commentary_button, "The first transaction send commentary button in commentaries menu in user profile couldn't be clicked or wasn't visible")
        self.click2(self._first_transaction_random_commentary_type_button)
        # self.click(self._first_transaction_random_commentary_type_button, "The first transaction random commentary type in commentaries menu in user profile couldn't be clicked or wasn't visible")
        self.clear_field_and_send_keys("This is my commentary", self._first_transaction_commentary_content, "The attempt to enter first transaction commentary content in commentaries menu in user profile was unsuccessful")
        self.click(self._first_transaction_submit_commentary_button, "The first transaction submit commentary button in commentaries menu in user profile couldn't be clicked or wasn't visible")

    def user_send_negative_commentary(self):
        self.click(self._commentaries_menu, "The commentaries menu in user profile couldn't be clicked or wasn't visible")
        self.click(self._first_transaction_send_commentary_button, "The first transaction send commentary button in commentaries menu in user profile couldn't be clicked or wasn't visible")
        self.click(self._first_transaction_negative_commentary_type_button, "The first transaction negative commentary type in commentaries menu in user profile couldn't be clicked or wasn't visible")
        self.clear_field_and_send_keys("This is my negative commentary", self._first_transaction_commentary_content, "The attempt to enter first transaction commentary content in commentaries menu in user profile was unsuccessful")
        self.click(self._first_transaction_submit_commentary_button, "The first transaction submit commentary button in commentaries menu in user profile couldn't be clicked or wasn't visible")

    def store_provider_data(self):
        self.condition_click(self._provider_profile_button, "The provider edit profile button couldn't be clicked or wasn't visible in provider profile")
        self.click(self._my_data_tab, "The my data tab couldn't be clicked or wasn't visible in provider profile")
        self.name1 = self.get_text(self._provider_data_saved_name)
        self.tel = self.get_text(self._provider_data_saved_tel)
        self.mail = self.get_text(self._provider_data_saved_mail)
        # self.kom = self.get_text(self._provider_data_saved_kom)
        self.click(self._company_data_tab, "The provider company data tab couldn't be clicked or wasn't visible in provider profile")
        self.www = self.get_text(self._provider_data_saved_www)
        self.address = self.get_text(self._provider_data_saved_address)
        self.address_without_html = re.sub("<.*?>", "", self.address)
        self.address_table = self.address_without_html.splitlines()
        self.address_table_0_splitted = re.findall(r'\S+', self.address_table[0])

    def ask_for_offer_for_added_consignment(self):
        self.click(self._my_consignments_menu, "The my consignments menu in user profile couldn't be clicked or wasn't visible")
        self.click(self._ask_for_offers_button, "The ask for offers button in my consignments menu in user profile couldn't be clicked or wasn't visible")
        self.click(self._first_offer, "The first offer in ask for offers in my consignments menu in user profile couldn't be clicked or wasn't visible")

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
        self.click(self._my_consignments_menu, "The my consignments menu in user profile couldn't be clicked or wasn't visible")

    def provider_open_my_consignments_menu(self):
        self.click(self._provider_my_consignments_menu, "The my consignments menu in provider profile couldn't be clicked or wasn't visible")

    def user_click_first_consignment_distinguish_button(self):
        self.click(self._first_consignment_distinguish_button)

    def provider_click_first_consignment_distinguish_button(self):
        self.click(self._provider_first_consignment_distinguish_button)

# coding=utf-8
from pages.base import BasePage
from pages.page import *
from selenium.webdriver.common.by import By
from time import sleep
from utils.utils import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import *

class SearchCriteriaPage(BasePage):

    _title = "Search criteria"

    _phone_finder_header = (By.CSS_SELECTOR, ".article-info-name")
    _brand_dropdown = (By.XPATH, "//div/div/div/button")
    _brand_index_random = str(randint(1, 116))
    _brand_index_random_button = (By.XPATH, "//li[%s]/a/i"%_brand_index_random)
    _accept_cookies_button = (By.XPATH, "//*[@i'ttons']/button[2]")
    _accept_cookies_button2 = (By. XPATH, "//*[@id='qcCmpButtons']/button[2]")
    _slider_year = (By.XPATH, "//div[2]/div/div[2]/div/div/div")
    _slider_year_start = (By.XPATH, "//div[2]/div/div[2]/div/div/div/div")
    _slider_year_end = (By.XPATH, "//div[2]/div/div/div[2]/div")

    def __init__(self, driver):
        super(SearchCriteriaPage, self).__init__(driver, self._title)

    def chose_random_brand(self):
        # self.click(self._accept_cookies_button)
        self.click(self._accept_cookies_button2)
        self.click(self._brand_dropdown)
        self.click(self._brand_index_random_button)

    def move_slider_year(self):
        procent = randint(10,30)
        width = self.find_element(self._slider_year).size['width']
        start = ActionChains(self.get_driver())
        start.click_and_hold(self.find_element(self._slider_year_start)).move_by_offset(procent * width/100, 0).release().perform()
        procent2 = randint(0,5)
        end = ActionChains(self.get_driver())
        end.click_and_hold(self.find_element(self._slider_year_end)).move_by_offset(procent2 * width/100 *(-1), 0).release().perform()
        sleep(1000)


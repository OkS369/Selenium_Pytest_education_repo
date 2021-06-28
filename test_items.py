import pytest
from selenium import webdriver
import time


def test_add_to_basket_button_at_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    button = browser.find_elements_by_css_selector('#add_to_basket_form > button')
    assert len(button) == 1, 'Test failed. More than 1 button or button not found'

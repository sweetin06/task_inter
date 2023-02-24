"""Signup"""

import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from env import link
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from pathfunctions import find_tag_name, find_tag_names, ec_xpath, find_id, find_xpath, ec_id

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


def signup(driver, mail_id, first_name, last_name):

    signup_btn = find_tag_names(driver, "a")
    for signup in signup_btn:
        if signup.text == "Sign up":
            driver.execute_script("arguments[0].click()", signup)

    mail = find_id(driver, "free_user_mail")
    ActionChains(driver).move_to_element(mail).click(mail)
    mail.send_keys(mail_id)

    continue_btn = find_xpath(driver, "button", "type", "submit")
    driver.execute_script("arguments[0].click()", continue_btn)

    driver.implicitly_wait(4)
    first_name_field = find_id(driver, "user_name")
    first_name_field.send_keys(first_name)

    last_name_field = find_id(driver, "user_name")
    last_name_field.send_keys(last_name)

    submit_btn = find_xpath(driver, "button", "type", "submit")
    driver.execute_script("arguments[0].click()", submit_btn)


if __name__ == '__main__':
    link(driver, "https://arun.devam.pro/gr/promo/be04")
    signup(driver, "testuser@test.co", "test", "user")

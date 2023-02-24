from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


def find_xpath(driver, element, type, value):
    return driver.find_element(By.XPATH, f"//{element}[@{type}='{value}']")


def find_id(driver, value):
    return driver.find_element(By.ID, f"{value}")


def find_class_name(driver, value):
    return driver.find_element(By.CLASS_NAME, f"{value}")


def find_class_names(driver, value):
    return driver.find_elements(By.CLASS_NAME, f"{value}")


def find_tag_name(driver, value):
    return driver.find_element(By.TAG_NAME, f"{value}")


def find_tag_names(driver, value):
    return driver.find_elements(By.TAG_NAME, f"{value}")


def find_xpaths(driver, element, type, value):
    return driver.find_elements(By.XPATH, f"//{element}[@{type}='{value}']")


def find_link_text(driver, value):
    return driver.find_element(By.LINK_TEXT, f"{value}")


def find_partial_link(driver, value):
    return driver.find_element(By.PARTIAL_LINK_TEXT, f"//{value}")


def find_css_selector(driver, value):
    return driver.find_element(By.CSS_SELECTOR, f"//{value}")


def ec_xpath(element, type, value):
    return EC.element_to_be_clickable((By.XPATH, f"//{element}[@{type}='{value}']"))


def ec_id(value):
    return EC.element_to_be_clickable((By.ID, f"{value}"))

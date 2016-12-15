#!/usr/bin/env python
import re
# NOTE: running this script requires selenium and chrome driver
#   `pip install selenium && brew install chromedriver` 
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

driver = webdriver.Chrome()

# TODO: provision this script with your PagerDuty username and password
username = ""
password = ""

def is_row_noise(row):
  desc = get_row_desc(row)
  is_noise = is_desc_noise(desc)

  print desc
  print '>> IS NOISE: {}'.format(is_noise)

  return is_noise

# TODO: override this function to identify noise based on the description
def is_desc_noise(desc):
  return False

def login():
  driver.get("http://comprehend.pagerduty.com/sign_in")
  driver.find_element_by_id("user_email").send_keys(username)
  driver.find_element_by_id("user_password").send_keys(password)
  driver.find_element_by_name("commit").click()

def get_rows():
  return driver.find_elements_by_css_selector(".pd-incidents-table table tbody tr")

def get_row_desc(row):
  return row.find_element_by_css_selector("td.details-cell").find_element_by_css_selector("a").text

def select_row(row):
  row.find_element_by_css_selector('td.select-row-cell input[type="checkbox"]').click()

def select_my_incidents():
  driver.find_element_by_class_name("assign-me").click()

def select_noise():
  for row in filter(is_noise, get_rows()):
    select_row(row)

def has_rows():
  try:
    driver.find_element_by_css_selector(".pd-incidents-table table tbody tr td.dataTables_empty")
    return False
  except NoSuchElementException:
    return True

def resolve():
  driver.find_element_by_css_selector(".pd-incident-table-actions div span a.resolve-incidents").click()

def main():
  try:
    login()
    select_my_incidents()
    sleep(5)
    if has_rows():
      select_noise()
      resolve()
  finally:
    driver.close()

main()

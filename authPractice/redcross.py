# %%

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time

from keys import USERNAME, PASSWORD, emails
from constants import DRIVER_FILE, REDCROSS_SITE, CLASSES

# EXTRACT EMAILS

# go to whentowork
# login
# go to employees tab
# select all
# export to clipboard

# EXTRACT DETAILS FOR ONE EMAIL

driver = Chrome(DRIVER_FILE)
driver.get(REDCROSS_SITE)
records = {}

def searchEmail(email):
  emailField = driver.find_element_by_id("dwfrm_certificate_email")
  emailField.send_keys(Keys.CONTROL, 'a')
  emailField.send_keys(email)
  emailField.send_keys(Keys.RETURN)
  time.sleep(1)

def getValidCertificates(email):
  certs = driver.find_elements_by_class_name("result-certificate-dt")
  for c in certs:
    klass, _, name, status = c.text.split("\n")[:4]
    if status == "Valid" and klass in CLASSES:
      records.setdefault(email, {
        "name": name,
        "classes": []
      })["classes"].append(klass)

for email in emails:
  searchEmail(email)
  getValidCertificates(email)
  
driver.close()

print(records)
# print(names)

#!/bin/python3

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www2.fazenda.mg.gov.br/arrecadacao/ctrl/ARRECADA/ARRECADA/DOCUMENTO_ARRECADACAO?ACAO=VISUALIZAR#"
chrome_options = webdriver.ChromeOptions()
# Usar somente quando precisar fazer download de arquivos
# prefs = {"download.default_directory": "./git/gdantas/selenium-automations"}

# chrome_options.add_experimental_option("prefs",prefs)

chrome_options.binary_location = r'./chromedriver'

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)
driver.maximize_window()

driver.implicitly_wait(4)

print("Obtendo dados do site:", url)

ICMS_INPUT = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/form/table[2]/tbody/tr[2]/td[2]/div/input')
print(ICMS_INPUT.text)
ICMS_INPUT.click()
ICMS_SELECT_OPTION = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/form/table[2]/tbody/tr[2]/td[2]/div/div[2]/span[2]')
ICMS_SELECT_OPTION.click()

TD_TXTCPN = driver.find_element(By.XPATH, '//*[@id="containerConteudoPrincipal"]/div/form/table[3]/tbody/tr/td/a/img')
print(TD_TXTCPN.text)
TD_TXTCPN.click()
time.sleep(4)

print("Done!")

driver.quit()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import os

CHROME_DRIVER_PATH = r'./chromedriver'
CERT_PATH = './certificados/nucleo.pfx'
CERT_PASSWORD = '999999999'
SITE = "https://cav.receita.fazenda.gov.br/autenticacao/Login"
PROFILE_DIR = os.path.abspath("temp_profile")

def configure_chrome_with_cert():
  options = Options()
  options.add_argument('--ignore-certificate-errors')
  options.add_argument(f'--user-data-dir={PROFILE_DIR}')
  driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH), options=options)
  driver.get('chrome://settings/certificates')
  time.sleep(2)
  driver.quit()

def main():
  print("Por favor, importe o certificado digital no perfil do Chrome localizado em:")
  print(PROFILE_DIR)
  print("Depois disso, pressione Enter para continuar...")
  input()
  options = Options()
  options.add_argument(f'--user-data-dir={PROFILE_DIR}')
  options.add_argument('--start-maximized')
  driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH), options=options)
  try:
    driver.get(SITE)
    time.sleep(10)
  finally:
    driver.quit()

if __name__ == "__main__":
  main()

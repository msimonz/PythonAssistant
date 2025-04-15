from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

def excel_to_pdf(ruta_excel, download_dir):

    options = Options()
    options.add_experimental_option("prefs", {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "directory_upgrade": True,
        "safebrowsing.enabled": True
    })
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://www.ilovepdf.com/es/excel_a_pdf")
        time.sleep(2)

        input_file = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        input_file.send_keys(ruta_excel)
        time.sleep(5)

        convertir_btn = driver.find_element(By.ID, "processTask")
        convertir_btn.click()
        time.sleep(10)

        print("✅ PDF descargado en:", download_dir)

    finally:
        driver.quit()

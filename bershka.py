import time
import requests
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

VPS_MODU = True
TOKEN = "8539943154:AAEcAMcDyIU6sKwnIQMVoc4NmmCcUvvRoRA"
ALICILAR = ["8205875564", "8556439449"]
URL = "https://www.bershka.com/tr/bowling-%C3%A7antas%C4%B1-c0p191238954.html?colorId=700"

def telegram_gonder(mesaj):
    for chat_id in ALICILAR:
        try:
            requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage",
                        json={"chat_id": chat_id, "text": mesaj}, timeout=10)
        except:
            pass

def tarayici_baslat():
    opts = Options()
    if VPS_MODU:
        opts.add_argument("--headless")
        opts.add_argument("--no-sandbox")
        opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--disable-blink-features=AutomationControlled")
    opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    opts.add_argument("--window-size=1920,1080")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)

def stok_analiz(driver):
    kaynak_kod = driver.page_source.lower()
    if any(word in kaynak_kod for word in ["gelince haber ver", "tükendi", "benzer ürünleri gör"]):
        return False

    xpath_query = "//button[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'sepete')]"
    butonlar = driver.find_elements(By.XPATH, xpath_query)

    for btn in butonlar:
        try:
            if (btn.is_displayed() and btn.is_enabled() and 
                btn.get_attribute("aria-disabled") != "true" and 
                "disabled" not in (btn.get_attribute("class") or "")):
                return True
        except:
            continue
    return False

def kontrol_et():
    driver = None
    try:
        driver = tarayici_baslat()
        driver.get(URL)
        try:
            WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        except:
            pass
        time.sleep(5)

        if stok_analiz(driver):
            time.sleep(5)
            driver.refresh()
            time.sleep(5)
            if stok_analiz(driver):
                telegram_gonder(f"STOKTA VAR\n{URL}")
                return True
        return False
    except:
        return False
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    while True:
        if kontrol_et():
            time.sleep(random.randint(900, 1200))
        else:
            time.sleep(random.randint(150, 240))

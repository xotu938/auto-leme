from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime

START_HOUR = 6   # 06:00 WIB
END_HOUR = 20    # 20:00 WIB

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://lemehost.com/server/3362244/free-plan")

print("Silahkan login manual dulu! Bot akan mulai otomatis setelah login dan sesuai jam.")

# Tunggu sampai login
while True:
    if "free-plan" in driver.current_url:
        break
    time.sleep(2)

print("Login terdeteksi! Bot siap.\n")

while True:
    now = datetime.now().hour
    
    # Jika di luar jam kerja bot
    if not (START_HOUR <= now < END_HOUR):
        print("⏸ Di luar jam kerja bot. Menunggu jam 06:00 WIB...")
        time.sleep(60 * 10)  # cek lagi tiap 10 menit
        continue

    print("🔄 Cek tombol Extend...")

    try:
        button = driver.find_element(By.XPATH, "//button[contains(text(),'Extend')]")
        if button.is_enabled():
            button.click()
            print("🟢 Extend diklik ✓")
        else:
            print("🟡 Tombol belum bisa diklik")
    except:
        print("🔴 Tombol tidak muncul")

    time.sleep(60 * 5)  # cek 5 menit sekali

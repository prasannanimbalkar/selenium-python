from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path="chromedriver")

driver = webdriver.Chrome(service=service)
driver.get("https://google.com")

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="APjFqb"]'))
)

search = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
search.send_keys("cookie clicker" + Keys.ENTER)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Cookie Clicker'))
)
driver.find_element(By.PARTIAL_LINK_TEXT, 'Cookie Clicker').click()

WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "English")]'))
    )
driver.find_element(By.XPATH, '//*[contains(text(), "English")]').click()



while True:
    WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.ID, "bigCookie"))
    )
    cookie = driver.find_element(By.ID, "bigCookie")

    cookie.click()

    cookies_count = driver.find_element(By.ID, "cookies").text.split(" ")[0]
    cookies_count = int(cookies_count.replace(",", ""))

    for i in range(4):
        product_price = driver.find_element(By.ID, "productPrice"+str(i)).text.replace(",", " ")

        if not product_price.isdigit():
            continue

        product_price = int(product_price)

        if cookies_count >= product_price:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "product"+str(i)))
            )
            product = driver.find_element(By.ID, "product"+str(i))
            product.click()
            break

time.sleep(10)
driver.quit()
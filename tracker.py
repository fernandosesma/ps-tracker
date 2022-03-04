# TO-DO: Suppress warnings in terminal: usb_device_handle_win.cc

# Import statements

import time
import webbrowser as wb
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys # DEBUG
from selenium.webdriver.common.by import By
from plyer import notification

# Import Chrome as a 'Service' object

service = Service("C:/Users/Fernando Sesma/Documents/Code/ps-tracker/chromedriver_v99/chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service = service)

# Relevant links to open/variables to work with

stores = ['Amazon', 'Best Buy', 'Target', 'PlayStation Direct']

amazon = "https://www.amazon.com/PlayStation-5-Console/dp/B09DFCB66S?ref_=ast_sto_dp"
bestBuy = "https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149"
targetLanding = "https://www.target.com/c/playstation-5-video-games/-/N-hj96d" # Landing page
playstation = "https://direct.playstation.com/en-us/consoles/console/playstation5-console.3006646"

links = [amazon, bestBuy, targetLanding, playstation]
xPaths =    ["//span[@class='a-size-medium a-color-price']", \
            "//button[@class='c-button c-button-disabled c-button-lg c-button-block add-to-cart-button']", \
            "//div[@data-component-id='WEB-342680']", \
            "//div[@class='out-stock-wrpr js-out-stock-wrpr']"]

# 0 - Amazon
# 1 - Best Buy
# 2 - Target
# 3 - PlayStation Direct

# Initialize statuses with empty strings

oldStockStatuses = ["","","",""]
newStockStatuses = ["","","",""]

def statusInit():
    for i in range(len(links)):
        driver.get(links[i])
        if i < 3:
            oldStockStatuses[i] = driver.find_element(By.XPATH, xPaths[i]).text
        else:
            psDirectElements = driver.find_elements(By.XPATH, xPaths[i])
            oldStockStatuses[i] = psDirectElements[1].text
    driver.quit

statusInit()
oldStockStatuses = newStockStatuses # Initialize new array, which will change with loop

# Initialize windows to check

def windowInit():
    driver.get(links[0]) # First tab
    # Probably not the most elegant indexing, fix later
    driver.maximize_window()
    for i in range(len(links)-1):
        driver.execute_script("window.open()")
        driver.switch_to.window(driver.window_handles[i+1])
        driver.get(links[i+1])
    driver.switch_to.window(driver.window_handles[0]) # Return to the first tab

windowInit()

# Notification method

def storeNotify(storeIndex):
    notification.notify(
        title=stores[storeIndex],
        message=stores[storeIndex] + " now has PS5s in stock!",
        app_icon=None,
        timeout=10
    )

# --- MAIN LOOP --- #

while oldStockStatuses == newStockStatuses:
    for i in range(len(links)):
        driver.switch_to.window(driver.window_handles[i])
        if i < 3: # Not PS Direct
            status = driver.find_element(By.XPATH, xPaths[i]).text
            newStockStatuses[i] = status
        if i == 3: # PS Direct
            status = driver.find_elements(By.XPATH, xPaths[i])
            newStockStatuses[i] = status[1].text
        time.sleep(10) # refresh timer
else:
    for i in range(len(links)):
        if oldStockStatuses[i] != newStockStatuses[i]:
            newStockIndex = i
            storeNotify(newStockIndex)
            wb.open_new_tab(links[newStockIndex])

from selenium import webdriver
from selenium.webdriver.support.color import Color
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import Variables
import Notifications
import re
import time

# Website Settings
url = "https://badfishbarbershop.nearcut.de/"
class_name = "test"
css_property = "background_color"
red_tone = "#b21d1a"
grey_tone = "#eeeeee"
time_sleep = 20
url_time_table = "https://badfishbarbershop.nearcut.de/book/shops/KJAXY4?barbers%5B%5D=ACI61M&filter_barbers%5B%5D=ACI61M&service_options%5B%5D=XKTC8E"
start_date = 12 #th day of the month
end_date = 15 #th day of the month
reset_notification_state = 1 #hour

# Start browser
driver = webdriver.Firefox()
driver.get(url)

# Login process
menu_bar = ""
proceed_login = True
try:
    menu_bar = driver.find_element(By.CLASS_NAME, "masthead-nav")
except NoSuchElementException:
    proceed_login = False

if proceed_login:
    login_button = menu_bar.find_element(By.LINK_TEXT, "Login")
    login_button.click()
    email_input = ""
    try:
        email_input = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "user_email")))
    except TimeoutException:
        print("Timout, Quitting")
        driver.quit()
        exit()

    password_input = driver.find_element(By.ID, "user_password")
    email_input.send_keys(Variables.username)
    password_input.send_keys(Variables.password)
    driver.find_element(By.CLASS_NAME, "btn-login").click()

driver.get(url_time_table)

# Group days

def group_days():
    selected_days = []
    try:
        days = driver.find_elements(By.CLASS_NAME, "day-calendar")
    except NoSuchElementException:
        driver.quit()
    for day in days:
        date = day.text
        match = re.search(r"\d+", date)
        date = int(match.group())
        if date>=start_date and date <=end_date:
            grandparent_element = day.find_element(By.XPATH, "../..")
            gp_bg = Color.from_string(grandparent_element.value_of_css_property("background-color")).hex
            if gp_bg != grey_tone:
                selected_days.append(day)
    return selected_days

start_time = time.time()
notified = False

while True:
    selected_days = group_days()
    current_time = time.time()
    elapsed_hours = int((current_time-start_time)/3600)
    if(elapsed_hours>=reset_notification_state):
        notified = False
    for day in selected_days:
        background_color = Color.from_string(day.find_element(By.XPATH, "../..").value_of_css_property("background-color")).hex
        if background_color != red_tone and not notified:
            Notifications.notify(Variables.event_name, Variables.description, Variables.priority, Variables.url, Variables.app_name)
            notified = True
    time.sleep(time_sleep)
    driver.refresh()
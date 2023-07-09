from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from selenium.common.exceptions import ElementNotInteractableException
import datetime
import time


def select_bookings():
    for i in courts:
        for j in time_index:
            xpath = (
                '/html/body/div[2]/main/div[3]/div/article/section[3]/div[5]/div/form[1]/div[1]/div[{court}]/div/div[{time}]/input')
            params = {
                'court': i,
                'time': j, }
            xpath = xpath.format(**params)
            slot = driver.find_element(By.XPATH, xpath)
            driver.execute_script("arguments[0].click();", slot)


# leave window open when done
options = uc.ChromeOptions()
# options.set_capability("detach", True)
driver = uc.Chrome(options=options)
# *** CUSTOMIZE BOOKING HERE ***
total_courts = [1, 2, 3, 4, 5, 6, 7, 8]
courts = [3]
total_time_slots = ["7am", "8am", "9am", "10am", "11am", "12pm",
                    "1pm", "2pm", "3pm", "4pm", "5pm", "6pm", "7pm", "8pm", "9pm"]
time_slots = ["10am", "11am"]
# Only badminton @ bedok heartbeat for now
activity_id = 18
venue_id = 895
now = datetime.datetime.now()
d = datetime.timedelta(days=15)
time_stamp = int((now + d).timestamp())

# *** SET LOGIN DETAILS HERE ***
username = "your_username"
password = "your_password"

# get time_index for xpath in select_bookings
time_index = []
for i in time_slots:
    index = total_time_slots.index(i) + 1
    time_index.append(index)

# go to bookings
driver.get("https://members.myactivesg.com/auth/signinSP")
driver.maximize_window()
wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/div/div/div/div/div[2]/div[2]/div/div/div[2]/div/div/div[1]/div/div/div/button[2]"))).click()
driver.find_element(
    By.XPATH, "/html/body/div/div/div/div/div[2]/div[2]/div/div/div[2]/div/div/div[2]/form/div/div[1]/div/input").send_keys(username)
driver.find_element(
    By.XPATH, "/html/body/div/div/div/div/div[2]/div[2]/div/div/div[2]/div/div/div[2]/form/div/div[2]/div/input").send_keys(password)
driver.find_element(
    By.XPATH, "/html/body/div/div/div/div/div[2]/div[2]/div/div/div[2]/div/div/div[2]/form/div/div[3]/button").click()
wait.until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/div[2]/header/div/div[1]/div[3]/div/div/nav/ul/li[7]/a")))
url = (
    'https://members.myactivesg.com/facilities/view/activity/{activity_id}/venue/{venue_id}?time_from={time}')
params = {
    'activity_id': activity_id,
    'venue_id': venue_id,
    'time': time_stamp
}
url = url.format(**params)
driver.get(url)
time.sleep(2)

# refresh till bookings selected
while True:
    try:
        select_bookings()
        driver.find_element(By.ID, "addtocartbtn").click()
        break
    except ElementNotInteractableException:
        print("Bookings not found, refreshing page...")
        driver.refresh()
        time.sleep(2)

# get past speed detector
print("Bookings found!")
time.sleep(2)
ok = driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div[2]/button")
driver.execute_script("arguments[0].click();", ok)
time.sleep(1)
print("Speed detector bypassed")

# actual add to cart
select_bookings()
time.sleep(1)
select_bookings()
time.sleep(3)
driver.find_element(By.ID, "addtocartbtn").click()
time.sleep(2)
driver.find_element(
    By.XPATH, "/html/body/div[6]/div/div/div[2]/button").click()
print("Added to cart")

# select debit
driver.find_element(
    By.XPATH, "/html/body/div[2]/main/div[3]/div/article/section[2]/form/div[1]/div[1]/ul/li[1]/input").click()

# enter pin
driver.find_element(
    By.XPATH, "/html/body/div[2]/main/div[3]/div/article/section[2]/form/div[1]/div[2]/div/div[1]/input[1]").sendkeys("8")
driver.find_element(
    By.XPATH, "/html/body/div[2]/main/div[3]/div/article/section[2]/form/div[1]/div[2]/div/div[1]/input[2]").sendkeys("5")
driver.find_element(
    By.XPATH, "/html/body/div[2]/main/div[3]/div/article/section[2]/form/div[1]/div[2]/div/div[1]/input[1]").sendkeys("5")
driver.find_element(
    By.XPATH, "/html/body/div[2]/main/div[3]/div/article/section[2]/form/div[1]/div[2]/div/div[1]/input[1]").sendkeys("7")
driver.find_element(
    By.XPATH, "/html/body/div[2]/main/div[3]/div/article/section[2]/form/div[1]/div[2]/div/div[1]/input[1]").sendkeys("8")
driver.find_element(
    By.XPATH, "/html/body/div[2]/main/div[3]/div/article/section[2]/form/div[1]/div[2]/div/div[1]/input[1]").sendkeys("0")

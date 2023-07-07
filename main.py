from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from datetime import datetime
import time

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)

# *** CUSTOMIZE BOOKING HERE ***
# Only badminton @ bedok heartbeat for now
courts = [3]
time_slots = ["10am", "11am"]
activity_id = 18
venue_id = 895
time_stamp = int(datetime.now().timestamp())

# go to bookings
driver.get("https://members.myactivesg.com/auth/signinSP")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/div/div/div/div/div[2]/div[2]/div/div/div[2]/div/div/div[1]/div/div/div/button[2]"))).click()
driver.find_element(
    By.XPATH, "/html/body/div/div/div/div/div[2]/div[2]/div/div/div[2]/div/div/div[2]/form/div/div[1]/div/input").send_keys("username")
driver.find_element(
    By.XPATH, "/html/body/div/div/div/div/div[2]/div[2]/div/div/div[2]/div/div/div[2]/form/div/div[2]/div/input").send_keys("password")
driver.find_element(
    By.XPATH, "/html/body/div/div/div/div/div[2]/div[2]/div/div/div[2]/div/div/div[2]/form/div/div[3]/button").click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
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
driver.execute_script("window.scrollTo(0, 675)")
time.sleep(5)

# select bookings
xpath = (
    '/html/body/div[2]/main/div[3]/div/article/section[3]/div[5]/div/form[1]/div[1]/div[{court_i}]/div/div[{time_i}]/input')
params = {
    'i': activity_id,
    '': venue_id,
    'time': time_stamp
}

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Chrome()
driver.get("https://healthreport.zju.edu.cn/ncov/wap/default/index")
# Input your own username and password in send_keys("?")
driver.find_element_by_id("username").send_keys("xxxxxxx")
driver.find_element_by_id("password").send_keys("xxxxxxx")
driver.find_element_by_id("dl").click()
time.sleep(10)
try:
    driver.find_element_by_xpath("//*[@name='sfzx']/div/div[1]")
except NoSuchElementException:
    time.sleep(5)

# Are you on campus today
# Yes
driver.find_element_by_xpath("//*[@name='sfzx']/div/div[1]").click()
# No
# driver.find_element_by_xpath("//*[@name='sfzx']/div/div[2]").click()

# Your location
driver.find_element_by_xpath("//*[@name='area']/input").click()
time.sleep(15)
try:
    # Close pop-up
    driver.find_element_by_xpath("//*[@id='wapat']/div/div[2]/div").click()
    # Select your location
    Select(driver.find_element_by_xpath("//*[@name='ip']/div/div/select[1]")).select_by_visible_text("浙江省")
    time.sleep(1)
    Select(driver.find_element_by_xpath("//*[@name='ip']/div/div/select[2]")).select_by_visible_text("杭州市")
    time.sleep(1)
    Select(driver.find_element_by_xpath("//*[@name='ip']/div/div/select[3]")).select_by_visible_text("西湖区")
except NoSuchElementException:
    print("Location permission is allowed")

# Have your family members (including other close contact persons）entered Chinese Mainland 
# over the past 14 days or plan to enter Chinese Mainland in 14 days
# Yes
# driver.find_element_by_xpath("//*[@name='sfymqjczrj']/div/div[1]").click()
# No
driver.find_element_by_xpath("//*[@name='sfymqjczrj']/div/div[2]").click()

# Promise
driver.find_element_by_xpath("//*[@name='sfqrxxss']").click()
# Submit info
driver.find_element_by_xpath("//*[@class='footers']").click()
time.sleep(5)
#Submit
try:
    driver.find_element_by_xpath("//*[@class='wapcf-btn wapcf-btn-ok']").click()
    print("Sign in successfully")
except NoSuchElementException:
    print("You have already signed in")

driver.close()

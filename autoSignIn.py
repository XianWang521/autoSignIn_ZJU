from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import time

def autosign(username,password,flag):
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('blink-settings=imagesEnabled=false')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://healthreport.zju.edu.cn/ncov/wap/default/index")
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("dl").click()
    time.sleep(10)
    try:
        driver.find_element_by_xpath("//*[@name='sfzx']/div/div[1]")
    except NoSuchElementException:
        time.sleep(5)

    driver.find_element_by_xpath("//*[@name='sfbyjzrq']/div/div[5]").click()
    # flag: 1: vaccinated; 2: not vaccinated; 3: one stitch
    if(flag == 1):
        driver.find_element_by_xpath("//*[@name='jzxgymqk']/div/div[2]").click()
    elif(flag == 2):
        driver.find_element_by_xpath("//*[@name='jzxgymqk']/div/div[3]").click()
    elif(flag == 3):
        driver.find_element_by_xpath("//*[@name='jzxgymqk']/div/div[1]").click()
    # Are you on campus today
    driver.find_element_by_xpath("//*[@name='sfzx']/div/div[1]").click()
    # No
    # driver.find_element_by_xpath("//*[@name='sfzx']/div/div[2]").click()

    driver.find_element_by_xpath("//*[@name='area']/input").click()
    time.sleep(15)
    try:
        driver.find_element_by_xpath("//*[@id='wapat']/div/div[2]/div").click()
        Select(driver.find_element_by_xpath("//*[@name='ip']/div/div/select[1]")).select_by_visible_text("浙江省")
        time.sleep(1)
        Select(driver.find_element_by_xpath("//*[@name='ip']/div/div/select[2]")).select_by_visible_text("杭州市")
        time.sleep(1)
        Select(driver.find_element_by_xpath("//*[@name='ip']/div/div/select[3]")).select_by_visible_text("西湖区")
    except NoSuchElementException:
        print("Location permission is allowed")

    driver.find_element_by_xpath("//*[@name='sfymqjczrj']/div/div[2]").click()
    driver.find_element_by_xpath("//*[@name='sfqrxxss']").click()
    driver.find_element_by_xpath("//*[@class='footers']").click()
    time.sleep(5)
    try:
        driver.find_element_by_xpath("//*[@class='wapcf-btn wapcf-btn-ok']").click()
        print(username + " sign in successfully")
    except NoSuchElementException:
        print(username + " has already signed in")
    driver.close()

username1 = []
password1 = []
username2 = []
password2 = []
username3 = []
password3 = []
# flag: 1: vaccinated; 2: not vaccinated; 3: one stitch
flag = 1
for i,j in zip(username1, password1):
    autosign(i,j,flag)

flag = 2
for i,j in zip(username2, password2):
    autosign(i,j,flag)

flag = 3
for i,j in zip(username3, password3):
    autosign(i,j,flag)
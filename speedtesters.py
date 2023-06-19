from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from datetime import datetime
import pandas as pd

service = Service(executable_path="C:\chromedriver\chromedriver.exe")


def test_speedtest_net():
    service_name = 'speedtest.net'
    start_time = datetime.now()
    test_date = start_time.strftime("%Y-%m-%d")
    test_time = start_time.strftime("%H:%M")

    print(f"speedtest.net:  test started")
    # ----
    driver = webdriver.Chrome(service=service)
    URL = "https://www.speedtest.net/"

    driver.get(URL)
    time.sleep(3)

    accept_cookies = driver.find_element(By.ID, "onetrust-accept-btn-handler")
    accept_cookies.click()

    go_button = driver.find_element(By.CSS_SELECTOR,".start-button a")
    go_button.click()

    while (driver.current_url == URL):
        time.sleep(1)

    ping = driver.find_element(By.CLASS_NAME, "ping-speed").text
    ping = float(ping)
    download_speed = driver.find_element(By.CLASS_NAME, "download-speed").text
    download_speed = float(download_speed)
    upload_speed = driver.find_element(By.CLASS_NAME, "upload-speed").text
    upload_speed = float(upload_speed)

    finish_time = datetime.now()
    test_duration = (finish_time - start_time).seconds
    driver.close()
    # ----
    testdata = {'service_name': service_name, 'ping': ping, 'upload_speed': upload_speed,
                'download_speed': download_speed, 'duration': test_duration, 'test_date': test_date,
                'test_time': test_time}

    print (testdata)
    return testdata

def test_fast_com():
    service_name = 'fast.com'
    start_time = datetime.now()
    test_date = start_time.strftime("%Y-%m-%d")
    test_time = start_time.strftime("%H:%M")
    print(f"fast.com:  test started")
    # ----
    driver = webdriver.Chrome(service=service)
    URL = "https://fast.com/"

    driver.get(URL)
    time.sleep(15)
    show_more_info_btn = driver.find_element(By.ID,"show-more-details-link")
    show_more_info_btn.click()
    time.sleep(15)

    download_speed = driver.find_element(By.ID,"speed-value").text
    download_speed=float(download_speed)
    upload_speed = driver.find_element(By.ID,"upload-value").text
    upload_speed = float(upload_speed)
    ping = driver.find_element(By.ID,"latency-value").text
    ping = float(ping)

    finish_time = datetime.now()
    test_duration = (finish_time - start_time).seconds
    driver.close()
    # ----
    testdata = {'service_name': service_name, 'ping': ping, 'upload_speed': upload_speed,
                'download_speed': download_speed, 'duration': test_duration, 'test_date': test_date,
                'test_time': test_time}

    print(testdata)
    return testdata


def test_broadbandspeedchecker_co_uk():
    service_name='broadbandspeed'
    start_time = datetime.now()
    test_date = start_time.strftime("%Y-%m-%d")
    test_time = start_time.strftime("%H:%M")

    print(f"broadbandspeedchecker.co.uk:  test started")
    # ----
    URL = "https://www.broadbandspeedchecker.co.uk/"
    driver = webdriver.Chrome(service=service)

    driver.get(URL)

    time.sleep(3)
    #accept_privacy = driver.find_element(By.CLASS_NAME, "css-47sehv")
    accept_privacy = driver.find_element(By.ID, "accept-choices")
    accept_privacy.click()
    time.sleep(5)
    start_speed_test = driver.find_element(By.CLASS_NAME, "button")
    start_speed_test.click()
    #time.sleep(1)
    test_url = driver.current_url
    while (driver.current_url == test_url):
        time.sleep(1)
    #time.sleep(5)
    ping = driver.find_element(By.NAME, "ping").text
    ping=float(ping.split(' ms')[0])

    download_speed = driver.find_element(By.NAME, "download").text
    download_speed = float(download_speed.split(' Mb/s')[0])

    upload_speed = driver.find_element(By.NAME, "upload").text
    upload_speed = float(upload_speed.split(' Mb/s')[0])

    finish_time = datetime.now()
    test_duration = (finish_time - start_time).seconds
    driver.close()
    #---

    testdata = {'service_name': service_name, 'ping': ping, 'upload_speed': upload_speed,
                'download_speed': download_speed,'duration': test_duration, 'test_date':test_date, 'test_time':test_time}

    print(testdata)
    return testdata
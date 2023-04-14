import os
import time
import shutil


from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

#YOU NEED TO SET THE CHROME DRIVER PATH
# CATEGORIES = ["Mystical","HD","Synthwave","Vibrant"]

#This is all current categories on wombo.art
# CATEGORIES = ["Etching","Baroque","Mystical","Festive","Dark Fantasy","Psychic","Pastel","HD","Vibrant","Fantasy Art","Steampunk","Ukiyoe","Synthwave","No Style"]


# def delete(path):
#     dele = os.listdir(path)
#     for dlt in dele:
#         print(dlt)
#         dlt = str(path + dlt)
#         os.remove(dlt)
# #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! jestli chci delete
# delete("Download/")


def click_on_xpath(driver, xpath, wait=30):
    btnGenerate = WebDriverWait(driver, wait).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    btnGenerate.click()

def write_text_xpath(driver, text, xpath, wait=30):
    textfield = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    for a in text:
        textfield.send_keys(a)
        time.sleep(0.05)


def downloadImage():
    headless = False
    username = "_steampunk_art_"
    password = "B0TB0T6"
    # get dir
    dir_path = os.getcwd()
    WEB_DRIVER_PATH = "{}/webdriver_veci/geckodriver".format(dir_path)   # add your chromedriver path
    # options
    browserOptions = webdriver.FirefoxOptions()
    if headless:
        browserOptions.add_argument("--head less")
    # create driver
    driver = webdriver.Firefox(executable_path=WEB_DRIVER_PATH,options=browserOptions)
    driver.get("https://www.instagram.com/")

    # allow cookies
    click_on_xpath(driver, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]')
    # username
    write_text_xpath(driver, username, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
    # password
    write_text_xpath(driver, password, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')
    # click login
    click_on_xpath(driver, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button/div')
    # click no_notifications
    click_on_xpath(driver, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
    # click on create
    click_on_xpath(driver, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[7]/div/div/a/div')
    
    # drag'n'drop image
    UPLOAD_XPATH = '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div/button'
    btnGenerate = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, UPLOAD_XPATH)))
    drag_drop = driver.find_element_by_xpath(UPLOAD_XPATH)
    drag_drop.send_keys('/home/michael/Documents/GitHub/ig_bot_selenium/image.png')


    time.sleep(60)
    driver.close()
    # #Type the text
    # # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    # textfield = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH ,XPATH_TEXT_FIELD)))
    # for a in inputText:
    #     textfield.send_keys(a)
    #     time.sleep(0.1)

    # #Select the img type to generate
    # imgTypeBox = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div[2]/div/div[2]/div[1]/div/div/img")))
    # imgTypeBox.click()

    # #Click on the "Create" button
    # btnGenerate = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,XPATH_GENERETE)))
    # btnGenerate.click()

    # time.sleep(1)


    # #Type the text
    # textfield = WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH ,XPATH_NAME_TEXT)))
    # textfield.send_keys(inputText)

    # #Click on the "Save" button
    # btnGenerate = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,XPATH_SAVE)))
    # btnGenerate.click()

    # time.sleep(10)


downloadImage("XX", "town")
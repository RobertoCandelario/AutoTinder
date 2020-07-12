from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains as ac
from selenium.webdriver.support.ui import Select
from datetime import datetime
import time
import random



class tinderbot:

    def __init__(self):

        self.driver = webdriver.Chrome()


    def closeBrowser(self):
        self.driver.close()


    def login(self):
        driver = self.driver
        driver.get("https://tinder.com/app/recs")
        time.sleep(8)

        #find login facebook button
        #face_book_button = driver.find_element_by_xpath("//*[@id='modal-manager']/div/div/div/div/div[3]/span/div[2]/button")
        #face_book_button.click()

        time.sleep(45)

        #location button
        allow_location = driver.find_element_by_xpath("//*[@id='modal-manager']/div/div/div/div/div[3]/button[1]")
        allow_location.click()

        time.sleep(5)
        #disable notifications
        no_notifications = driver.find_element_by_xpath("//*[@id='modal-manager']/div/div/div/div/div[3]/button[2]")
        no_notifications.click()

    def like_button_click(self):
        time.sleep(2)
        driver = self.driver
        game = driver.find_element_by_xpath("//*[@id='Tinder']/body")
        game.send_keys(Keys.ARROW_RIGHT)

    def runbot(self):
        self.login()

        loopNumber = 1

        while loopNumber != 9900:
             self.like_button_click()
             loopNumber = loopNumber + 1
             print loopNumber
testbot = tinderbot()
testbot.runbot()


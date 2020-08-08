from selenium import webdriver
import time
import random

driver = webdriver.Chrome("/Users/MatthewSzurkowski/Desktop/ohmSweeper/chromedriver")
driver.get("https://www.omegle.com/")
textButton = driver.find_element_by_xpath("//img[@id='textbtn']")
print(textButton)
textButton.click()
time.sleep(3)


def sendMessage(message):
    chatBox = driver.find_element_by_tag_name('textarea')
    print(chatBox)
    chatBox.send_keys(message + '\n')


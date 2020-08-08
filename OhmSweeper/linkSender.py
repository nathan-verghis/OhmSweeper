from selenium import webdriver
import time
import random

def sendMessage(message):
    chatBox = driver.find_element_by_tag_name('textarea')
    print(chatBox)
    chatBox.send_keys(message + '\n')

def getLink():
    grabify = input("Enter a grabify link\n")
    sendMessage(grabify)

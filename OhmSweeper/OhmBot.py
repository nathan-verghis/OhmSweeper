from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

'''
class OhmBot:
    def __init__(self):
        self.bot = webdriver.Chrome()
        self.log_history = []

    def get_reply(self):
        logbox = self.bot.find_elements_by_class_name("logbox")
        print(logbox)

    def is_human(self):


    def communicate:


    def identify_predator:


    def upload_predator:


def type_speed(message, time):
    length = len(message)
    wpm = length / time

def timer

statuslog
def is_typing():

connected = True

while connected:
    typing = is_typing()
    if typing:
        timer.start
    if message_received:
        timer.stop'''

bot = webdriver.Firefox()
possible_endings =\
    ["Great chat? Save the log: Get a link • Select all • Or post log to: Facebook • Tumblr • Twitter • reddit",
     "Stranger has disconnected", "Find strangers with common interests (Enable)"]
bot.get("https://www.omegle.com")
newchat = bot.find_element_by_id("chattypetextcell")
newchat.click()
time.sleep(5)
logbox = []
while bot.find_elements_by_class_name("logitem")[-1].text not in possible_endings:
    time.sleep(2)
    if bot.find_elements_by_class_name("logitem")[-1].text not in logbox:
        logbox.append(bot.find_elements_by_class_name("logitem")[-1].text)

logbox.remove(logbox[len(logbox) - 1])
for chat in logbox:
    print(chat)
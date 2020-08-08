from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class OhmBot:
    def __init__(self):
        self.bot = webdriver.Chrome()
        self.log_history = []

    def store_reply(self):
        self.log_history.append(self.bot.find_elements_by_class_name("logitem")[-1].text)

    def get_last_input(self):
        return self.log_history[-1].text

    def is_human(self):
        if type_speed(self.get_last_input(), self.type_time()) > 12.5:
            return False
        else:
            return True

    def type_time(self):
        if self.get_last_input() == "Stranger is typing":
            time_start = time.time()
        if self.get_last_input() != "Stranger is typing":
            time_end = time.time()
        return time_end - time_start

    def communicate:


    def identify_predator:


    def upload_predator:

    def chat_is_over(self):
        possible_endings = \
            ["Great chat? Save the log: Get a link • Select all • Or post log to: Facebook • Tumblr • Twitter • reddit",
             "Stranger has disconnected", "Find strangers with common interests (Enable)"]
        if self.get_last_input() in possible_endings:
            return True
        else:
            return False


def type_speed(message, time):
    length = len(message)
    wpm = length / time

def timer

def is_typing():

connected = True

while connected:
    typing = is_typing()
    if typing:
        timer.start
    if message_received:
        timer.stop
'''
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
    print(chat)'''
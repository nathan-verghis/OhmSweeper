from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import linkSender as sender


class OhmBot:
    def __init__(self):
        self.bot = webdriver.Chrome(ChromeDriverManager().install())
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
        pass

    def communicate(self, message):
        chatBox = self.bot.find_element_by_tag_name('textarea')
        chatBox.send_keys(message + '\n')

    def identify_predator():
        pass


    def upload_predator():
        pass

    def chat_is_over(self):
        possible_endings = \
            ["Great chat? Save the log: Get a link • Select all • Or post log to: Facebook • Tumblr • Twitter • reddit",
             "Stranger has disconnected", "Find strangers with common interests (Enable)"]
        if self.get_last_input() in possible_endings:
            return True
        else:
            return False

    def newchat(self):
        self.bot.get("https://www.omegle.com/")
        textButton = self.bot.find_element_by_xpath("//img[@id='textbtn']")
        textButton.click()
        time.sleep(3)
        
        
        
        

bot = OhmBot()
bot.newchat()
while True:
    time.sleep(1)
    if (bot.chat_is_over() == True):
        bot.newchat()
    message = input("Enter message")
    bot.communicate(message)
    

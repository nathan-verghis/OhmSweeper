from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import linkSender as sender


class OhmBot:
    def __init__(self):
        self.bot = webdriver.Chrome(ChromeDriverManager().install())
        self.log_history = []
    #Stranger is typing...
    def store_reply(self):
        if len(self.log_history) > 1:
            if self.log_history[-1] != self.bot.find_elements_by_class_name("logitem")[-1].text:
                self.log_history.append(self.bot.find_elements_by_class_name("logitem")[-1].text)
                #print(self.log_history[-1])
        else:
            self.log_history.append(self.bot.find_elements_by_class_name("logitem")[-1].text)
            #print(self.log_history[-1])

    def get_last_input(self):
        return self.log_history[-1]

    def is_human(self, type_time):
        if type_speed(self.get_last_input(), type_time) > 12.5:
            return False
        else:
            return True

    def type_time(self, time1):
        self.wait_for_message()
        time_end = float(time.time())
        return time_end - time1

    def wait_for_message(self):
        while self.log_history[-1][:3] == "You" or self.log_history[-1] == "Stranger is typing...":
            self.store_reply()
            time.sleep(1)
            if self.log_history[-1][:3]!= "You" and self.log_history[-1]!= "Stranger is typing...":
                print(self.log_history[-1])
                break
        self.communicate()



    def communicate(self):
        #Need to check whether if over or not
        #Also, I'm having a problem with when
        #They respond right away like I can't log both responses
        #So this needs to be fixed
        time.sleep(1.5)
        self.store_reply()
        if self.log_history[-1] == "Stranger is typing...":
            time.sleep(3)
            self.store_reply()
            print(self.log_history[-1])
        try:
            message = input("Enter message\n")
            bot.send_message(message)
        except:
            self.newchat()
            


    def send_message(self, message):
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
    bot.store_reply()
    time.sleep(1)
    if (bot.chat_is_over() == True):
        bot.newchat()
    bot.wait_for_message()
    
        

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import linkSender as sender
from OhmSweeper import Functions
from random import randint


class OhmBot:
    def __init__(self):
        self.bot = webdriver.Chrome(ChromeDriverManager().install())
        self.log_history = []
        self.dirty_response_counter = 0
        self.clean_response_counter = 0
        self.link = ""

    def store_reply(self):
        if self.log_history[-1] != self.bot.find_elements_by_class_name("logitem")[-1].text:
            self.log_history.append(self.bot.find_elements_by_class_name("logitem")[-1].text)

    def get_last_input(self):
        return self.log_history[-1]

    def is_human(self, type_time):
        if Functions.type_speed(self.get_last_input(), type_time) > 12.5:
            return False
        else:
            return True

    def type_time(self, time1):
        self.wait_for_message()
        time_end = float(time.time())
        return time_end - time1

    def wait_for_message(self):
        while self.log_history[-2] != "Stranger is typing...":
            pass

    def communicate(self):
        while not self.chat_is_over():
            current_message = self.bot.find_elements_by_class_name("logitem")[-1].text
            self.store_reply()
            if current_message == "Stranger is typing...":
                time_start = float(time.time())
                type_time = self.type_time(time_start)
                if not self.is_human(type_time):
                    break
            if self.is_predator():
                response = self.predator_response()
                self.send_message(response)
                if self.dirty_response_counter > 3:
                    break
            else:
                response = self.calculate_response()
                self.send_message(response)
                if self.clean_response_counter > 2:
                    break

    def identify_predator():
        # kal
        pass

    def send_message(self, message):
        chatBox = self.bot.find_element_by_tag_name('textarea')
        chatBox.send_keys(message + '\n')

    def predator_response(self):
        self.dirty_response_counter += 1
        if self.dirty_response_counter == 1:
            return "lol, maybe..."
        if self.dirty_response_counter == 2:
            return "first i wanna know if you think im cute xD"
        if self.dirty_response_counter == 3:
            return "mmm here ill send you a link: " + self.link
        if self.dirty_response_counter > 3:
            return "shit i gtg, my snap code is in that pic ;)"

    def is_predator(self):
        red_flags = ["sex", "sexy", "nudes", "pics", "touch", "tits", "pussy", "address", "suck", "lick",
                     "load", "ass", "horny", "nude", "pic"]
        if self.get_last_input().lower() in red_flags:
            return True
        else:
            return False

    def calculate_response(self):
        random_age = randint(13, 16)
        standard_questions = {"m": "f" + str(random_age), "asl": "im " + str(random_age) + "f lol but idk you"}
        for sq in standard_questions:
            if sq in self.get_last_input().lower():
                return standard_questions[sq]
        self.clean_response_counter += 1
        if self.clean_response_counter == 1:
            return "so wyd"
        if self.clean_response_counter == 2:
            return "lol same xD"
        if self.clean_response_counter == 3:
            return "lol, i gtg"

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
        
        
        
        
if __name__ == "__main__":
    bot = OhmBot()
    bot.newchat()
    while True:
        time.sleep(1)
        if (bot.chat_is_over() == True):
            bot.newchat()
        message = input("Enter message")
        bot.communicate(message)


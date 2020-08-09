from selenium import webdriver
# from webdriver.manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
# import linkSender as sender
from OhmSweeper.OhmSweeper import Functions
from random import randint


class OhmBot:
    def __init__(self):
        self.bot = webdriver.Firefox()
        self.log_history = []
        self.dirty_response_counter = 0
        self.clean_response_counter = 0
        self.link = ""

    def store_reply(self):
        if len(self.log_history) >= 1:
            if self.log_history[-1] != self.bot.find_elements_by_class_name("logitem")[-1].text and\
                    self.bot.find_elements_by_class_name("logitem")[-1].text != 'Stranger is typing...' and\
                    self.bot.find_elements_by_class_name("logitem")[-1].text != \
                    "You're now chatting with a random stranger. Say STAND WITH HONG KONG AGAINST THE CCP!":
                self.log_history.append(self.bot.find_elements_by_class_name("logitem")[-1].text)
        else:
            if self.bot.find_elements_by_class_name("logitem")[-1].text != 'Stranger is typing...' and\
                    self.bot.find_elements_by_class_name("logitem")[-1].text != \
                    "You're now chatting with a random stranger. Say STAND WITH HONG KONG AGAINST THE CCP!":
                self.log_history.append(self.bot.find_elements_by_class_name("logitem")[-1].text)

    def get_last_input(self):
        return self.log_history[-1]

    def wait_for_message(self):
        print(len(self.log_history))
        if len(self.log_history) > 1:
            log_length = len(self.log_history)
            while self.bot.find_elements_by_class_name("statuslog"):
                self.store_reply()
                print(log_length, end=" ")
                print(len(self.log_history))
                if log_length < len(self.log_history):
                    break
                print(self.log_history)
                pass
        else:
            while len(self.log_history) < 1:
                self.store_reply()
                print(self.log_history)
                print("YAAAA")
                pass

    def communicate(self):
        while not self.chat_is_over():
            self.wait_for_message()
            self.store_reply()
            time.sleep(3)
            if self.is_predator():
                response = self.predator_response()
                self.send_message(response)
                if self.dirty_response_counter > 4:
                    break
            else:
                response = self.calculate_response()
                self.send_message(response)
                print("yeah")
                if self.clean_response_counter > 4:
                    break

    def identify_predator(self):
        # kal
        pass

    def send_message(self, message):
        chatBox = self.bot.find_element_by_tag_name('textarea')
        chatBox.send_keys(message + '\n')

    def predator_response(self):
        # This is meant to bait predators to click the link so we can ip grab them
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
                     "load", "ass", "horny", "nude", "pic", "dick", "cock", "cunt", "wearing"]
        if self.get_last_input().lower() in red_flags:
            return True
        else:
            return False

    def calculate_response(self):
        random_age = randint(13, 16)
        standard_questions = {"m": "f" + str(random_age), "asl": "im " + str(random_age) + "f lol but idk you",
                              "age": str(random_age) + " hbu", "from": "idk you tho", "wyd": "nm hbu"}
        for sq in standard_questions:
            if sq in self.get_last_input().lower():
                '''if sq == "m" and \
                        (self.get_last_input().lower() != "m" or self.get_last_input().lower() != "m" + str(int)):
                    pass
                else:'''
                return standard_questions[sq]
        self.clean_response_counter += 1
        if self.clean_response_counter == 1:
            return "hi"
        if self.clean_response_counter == 2:
            return "so wyd"
        if self.clean_response_counter == 3:
            return "lol same xD"
        if self.clean_response_counter == 4:
            return "lol, i gtg"

    def upload_predator(self):
        pass

    def chat_is_over(self):
        possible_endings = \
            ["Great chat? Save the log: Get a link • Select all • Or post log to: Facebook • Tumblr • Twitter • reddit",
             "Stranger has disconnected", "Find strangers with common interests (Enable)"]
        if len(self.log_history) > 1:
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


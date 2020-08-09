from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from OhmSweeper.OhmSweeper.Functions import *
from OhmSweeper.OhmSweeper.linkSender import LinkSender
import time


class OhmBot:
    def __init__(self, ls):
        self.bot = webdriver.Chrome(ChromeDriverManager().install())
        self.log_history = []
        self.standard_count = 1
        self.flagged_count = 1
        self.is_predator = False
        self.ip_logger = ls
        self.url = ls.get_url()
    # Stranger is typing...

    def store_reply(self):
        if len(self.log_history) > 1:
            if self.log_history[-1] != self.bot.find_elements_by_class_name("logitem")[-1].text:
                self.log_history.append(self.bot.find_elements_by_class_name("logitem")[-1].text)
                # print(self.log_history[-1])
        else:
            self.log_history.append(self.bot.find_elements_by_class_name("logitem")[-1].text)
            # print(self.log_history[-1])

    def get_last_input(self):
        return self.log_history[-1]

    def type_time(self, time1):
        self.wait_for_message()
        time_end = float(time.time())
        return time_end - time1

    def wait_for_message(self):
        while self.log_history[-1][:3] == "You" or self.log_history[-1] == "Stranger is typing...":
            self.store_reply()
            time.sleep(1)
            if self.log_history[-1][:3] != "You" and self.log_history[-1] != "Stranger is typing...":
                print(self.log_history[-1])
                break
        self.communicate()

    def communicate(self):
        time.sleep(1.5)
        self.store_reply()
        if self.log_history[-1] == "Stranger is typing...":
            time.sleep(3)
            self.store_reply()
        try:
            message = self.create_message()
            if message is None:
                pass
            bot.send_message(message)
            if message == "here try this link " + self.url:
                info = identify_predator(self.ip_logger)
                ip_address = info[0]
                upload_predator(info, self.log_history)
                bot.send_message("Thank you for your time " + ip_address +
                                 ". You will be exposed. This has been OhmBot :)")
            if self.standard_count == 5 or self.flagged_count == 6:
                print("done")
                time.sleep(50)
        except:
            pass

    def create_message(self):
        standard_responses = {"m": "f16", "m" + str(int): "f16", "hello": "hi", "hi": "hi", "wassup": "hi",
                              "hey": "hi", "heyy": "hi", "howdy": "hi", "m or f": "f16", "f?": "yeah, f16",
                              "m or f?": "f16", "from": "idk you tho", "from?": "idk you tho"}
        red_flags = ["sex", "horny", "hornyy", "hornyyy", "cum", "pussy", "cunt", "bed", "nudes", "naked", "fuck",
                     "babe", "baby", "beat",
                     "nude", "dick", "penis", "cock", "sexy", "wet", "load", "jizz", "masturbate", "jacking", "smash"]
        for response in standard_responses:
            if "stranger: " + response == self.log_history[-1].lower():
                return standard_responses[response]

        for flag in red_flags:
            if flag in self.log_history[-1].lower():
                self.standard_count = 0
                self.is_predator = True

        if self.standard_count != 0:
            if self.standard_count == 1:
                self.standard_count += 1
                return "wyd"
            elif self.standard_count == 2:
                self.standard_count += 1
                return "lol same XD"
            elif self.standard_count == 3:
                self.standard_count += 1
                return "why you on omegle?"
            elif self.standard_count == 4:
                self.standard_count += 1
                return "im here cuz im so boreddd lol"

        if self.is_predator:
            if self.flagged_count == 1:
                self.flagged_count += 1
                return "maybeee"
            elif self.flagged_count == 2:
                self.flagged_count += 1
                return "lol, how do ik i can trust you tho"
            elif self.flagged_count == 3:
                self.flagged_count += 1
                return "first you have to do me favor"
            elif self.flagged_count == 4:
                self.flagged_count += 1
                return "should i post this pic on my insta? "
            elif self.flagged_count == 5:
                self.flagged_count += 1
                return "here try this link " + self.url

    def send_message(self, message):
        chatBox = self.bot.find_element_by_tag_name('textarea')
        chatBox.send_keys(message + '\n')

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


x = 10
while x < 10:
    ip_logger = LinkSender()
    bot = OhmBot(ip_logger)
    bot.newchat()
    while True:
        bot.store_reply()
        time.sleep(1)
        if bot.chat_is_over():
            break
        bot.wait_for_message()
    x += 1

        

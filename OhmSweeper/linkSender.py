from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time


class LinkCollector:
    def __init__(self):
        self.bot = webdriver.Chrome(ChromeDriverManager().install())
        self.url = ""
        self.data = ""
        self.data_history = []

    def create_new_link(self):
        self.bot.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        info_tab = self.bot.find_element_by_xpath("//span[text()='Information about IPLogger']")
        info_tab.click()
        change_domain = self.bot.find_element_by_xpath("//select[@id='choosesite']")
        change_domain.click()
        domain = self.bot.find_element_by_xpath("//option[@value='02ip.ru']")
        domain.click()
        change_ext = self.bot.find_element_by_xpath("//select[@id='chooseext']")
        change_ext.click()
        ext = self.bot.find_element_by_xpath("//option[@value='jpg']")
        ext.click()
        copy_button = self.bot.find_element_by_xpath("//input[@id='fromfirst']")
        # STORES THE LINK IN SELF.URL
        self.url = copy_button.get_attribute("data-clipboard-text")
        return self.url

    def get_history(self):
        log_tab = self.bot.find_element_by_xpath("//span[text()='Logged IP’s']")
        log_tab.click()
        for i in range(len(self.bot.find_elements_by_class_name("statline"))):
            self.data_history.append(self.bot.find_elements_by_class_name("statline")[i].text)

    def get_data(self):
        log_tab = self.bot.find_element_by_xpath("//span[text()='Logged IP’s']")
        log_tab.click()
        stat_line = self.bot.find_elements_by_class_name("statline")[1].text
        '''while stat_line in self.data_history:
            self.refresh()
            stat_line = self.bot.find_elements_by_class_name("statline")[1].text
            pass'''
        self.data = stat_line
        self.data_history.append(self.data)
        return self.data

    def refresh(self):
        refresh_button = self.bot.find_element_by_xpath("//div[@name='refresh']")
        refresh_button.click()

    def login(self):
        self.bot.get("https://iplogger.org/")
        sign_in = self.bot.find_element_by_xpath("//div[@class='mLogin']")
        sign_in.click()
        email = self.bot.find_element_by_xpath("//input[@id='lusername']")
        email.click()
        email.send_keys("nbverghis@gmail.com")
        password = self.bot.find_element_by_xpath("//input[@id='lpassword']")
        password.click()
        password.send_keys("qwertyqwertyqwerty" + "\n")
        time.sleep(3)
        loggers = self.bot.find_element_by_xpath("//span[@class='dropmenu' and text()=' Your IPLoggers']")
        loggers.click()
        time.sleep(2)
        my_logger = self.bot.find_element_by_xpath("//a[text()=' IPLoggers in your account [1]']")
        my_logger.click()
        time.sleep(2)
        my_logger = self.bot.find_element_by_xpath("//a[text()='Shortened URL']")
        my_logger.click()
        self.bot.find_element_by_tag_name('body').send_keys(Keys.COMMAND + Keys.TAB)
        time.sleep(2)
        self.bot.switch_to.window(self.bot.window_handles[1])


'''link = LinkCollector()
link.login()
link.create_new_link()
link.check_logged_ip()'''


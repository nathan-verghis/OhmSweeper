from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time



class linkCollector:
    def __init__(self):
        self.bot = webdriver.Chrome(ChromeDriverManager().install())
        self.url = ""
        self.data = ""

    def createNewLink(self):
        self.bot.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        infoTab = self.bot.find_element_by_xpath("//span[text()='Information about IPLogger']")
        infoTab.click()
        changeDomain = self.bot.find_element_by_xpath("//select[@id='choosesite']")
        changeDomain.click()
        domain = self.bot.find_element_by_xpath("//option[@value='02ip.ru']")
        domain.click()
        changeExt = self.bot.find_element_by_xpath("//select[@id='chooseext']")
        changeExt.click()
        ext = self.bot.find_element_by_xpath("//option[@value='jpg']")
        ext.click()
        copyButton = self.bot.find_element_by_xpath("//input[@id='fromfirst']")
        #STORES THE LINK IN SELF.URL
        self.url = copyButton.get_attribute("data-clipboard-text")
        return self.url

    def checkLoggedIP(self):
        logTab = self.bot.find_element_by_xpath("//span[text()='Logged IP’s']")
        logTab.click()
        statline = self.bot.find_elements_by_class_name("statline")[1].text
        self.data = statline
        return self.data
        
        
    def login(self):
        self.bot.get("https://iplogger.org/")
        signIn = self.bot.find_element_by_xpath("//div[@class='mLogin']")
        signIn.click()
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
        myLogger = self.bot.find_element_by_xpath("//a[text()=' IPLoggers in your account [1]']")
        myLogger.click()
        time.sleep(2)
        myLogger = self.bot.find_element_by_xpath("//a[text()='Shortened URL']")
        myLogger.click()
        self.bot.find_element_by_tag_name('body').send_keys(Keys.COMMAND + Keys.TAB)
        time.sleep(2)
        self.bot.switch_to.window(self.bot.window_handles[1])
        
        
link = linkCollector()
link.login()
link.createNewLink()
link.checkLoggedIP()
    

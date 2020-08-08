from selenium import webdriver
def type_speed(message, time):
    length = len(message)
    cpm = length/time
    return cpm

def is_typing(OhmBot):
    log = []
    for x in OhmBot.bot.find_elements_by_class_name("statuslog"):
        log.append(x.text)
    if("Stranger is typing...") in log:
        return True
    else:
        return False
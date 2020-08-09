from selenium import webdriver


def identify_predator(ip_logger):
    return ip_logger.get_data()


def upload_predator(info, log):
    file = open("predators.txt", "a")
    file.write(info + "\n")
    '''for entry in log:
        file.write(entry)
    file.write("\n\n")'''
    file.close()

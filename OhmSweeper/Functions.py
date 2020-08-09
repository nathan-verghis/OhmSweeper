from selenium import webdriver


def identify_predator(ip_logger):
    ip = ip_lower.get_ip_address()
    location = ip_logger.get_location()
    return ip, location


def upload_predator(info, log):
    file = open("predators.txt", "a")
    file.write(info[0] + " located at: " + info[1] + "\n")
    for entry in log:
        file.write(entry)
    file.write("\n\n")
    file.close()

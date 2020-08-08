from OhmSweeper.OhmSweeper.OhmBot import OhmBot

exit_key = False

while not exit_key:
    ch = OhmBot()
    ch.newchat()
    ch.communicate()

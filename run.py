from time import sleep
from publish_image import publish_image
from send_notification import send_notif
for x in range(117):
    try:
        publish_image("https://instabotsoubory.michael36500.repl.co/steampunk/{}.png".format(x))
    except Exception as e:
        print("fucked up", e)
        send_notif("fucked up", e)
    sleep(15*60)
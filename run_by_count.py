from time import sleep
from publish_image import publish_image
from send_notification import send_notif

file = open("count.txt", "r")
actual_num = int(file.readlines()[0])
file.close()

file = open("count.txt", "w")
file.write(str(actual_num + 1))

try:
    publish_image("https://instabotsoubory.michael36500.repl.co/steampunk/{}.png".format(actual_num))
except Exception as e:
    print("fucked up", e)
    send_notif("fucked up", e)


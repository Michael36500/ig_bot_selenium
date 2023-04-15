from time import sleep
from publish_image import publish_image

for x in range(117):
    publish_image("https://instabotsoubory.michael36500.repl.co/steampunk/{}.png".format(x))
    sleep(15*60)
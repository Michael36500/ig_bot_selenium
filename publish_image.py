import json
import requests
from send_notification import send_notif
from time import sleep

def publish_image(image_url):
    access_token = "EAANr4f2un40BAGNwlx7V9DZAvKDG1vS3cRQ1Vuwc3PPy4eN2ZCpj4xPJ6e2qpRTCEGLOA0ZAZCUkFqdUAxZAKMKb3KWkSdAgZBgoZBQZBFnIuiAgCFfkqKkzZA1z6ZCItFuirT5bWO8XorFcMj6zQCqD73sGUO33LbbYBWoDyd6ZCYwoKe2Dr5cP3AZB"
    ig_user_id = "17841453253198967"
    # image_url = "http://pure80spop.co.uk/wp-content/uploads/2020/07/Rick_Astley-1600x1069.jpg"

    post_url = "https://graph.facebook.com/v16.0/{}/media".format(ig_user_id)

    payload = {
        "image_url" : image_url,
        "caption" : "Lul going back",
        "access_token" : access_token
    }

    r = requests.post(post_url, data=payload)
    print(r.text)
    print("gut upload")

    results = json.loads(r.text)
    if "id" in results:
        creation_id = results["id"]
        second_url = "https://graph.facebook.com/v16.0/{}/media_publish".format(ig_user_id)
        second_payload = {
            "creation_id" : creation_id,
            "access_token" : access_token
        }
        r = requests.post(second_url, data=second_payload)
        print(r.text)
        send_notif("steampunk - GUT", image_url)
        print("gut")
    else:
        send_notif("steampunk - NEIN GUT", image_url)
        print("nein gut")


for x in range(117):
    publish_image("https://instabotsoubory.michael36500.repl.co/steampunk/{}.png".format(x))
    sleep(15*60)
import json
import requests

e
def publish_image(image_url):
    access_token = "EAANr4f2un40BAC3Cl97yMJZAcR5L9ZCv3j2K2J7Ok8BKa0LWFYcTMwWtxRkqK9gsZAXWZAobYZAVzJ0MjwNT6BmhSYLagyyXKszkNCcR6LsmZC0olcDDI2nynyOqxLtiXckYhVbVTjlrx2EQptHGyCDOwx0RaZARA2pczKOKP2IVHEZBYall17ZA9o3tybIUVKzKUyZAAlJj0lenjBORhO3M3J"
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
        print("all gut")
    else:
        print("not gut")+

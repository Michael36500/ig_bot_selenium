def send_notif(title, body):
    import pushbullet
    
    token = open("tokens.txt", "r").readlines()[1]
    pb = pushbullet.PushBullet(token)
    push = pb.push_note(title, body)

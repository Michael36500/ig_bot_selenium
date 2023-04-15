def send_notif(title, body):
    import pushbullet

    token = "o.ZtewAmm8EzYaeRQ3BflYDMRvPBJ6Cu3i"
    pb = pushbullet.PushBullet(token)
    push = pb.push_note(title, body)
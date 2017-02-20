def is_email(txt):
    txt = txt.decode('utf8').lower()
    return (len(txt) >= 5 and txt.find("@") >= 0) or (txt.find("mail") >= 0 and len(txt) >= 11)
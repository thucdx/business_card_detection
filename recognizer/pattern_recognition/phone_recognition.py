import re

def is_phone(txt):
    m = re.findall(r'\d', txt)
    if len(m) >= 8:
        return True
    return False
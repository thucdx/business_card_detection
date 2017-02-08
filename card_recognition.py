import pytesseract
import re
import jsonpickle
import common_name_recognition as name_recog

try:
    import Image
except ImportError:
    from PIL import Image

from contact import Contact


def recognize_contact(img_path):
    txt = extract(img_path)
    tokens = tokenizer(txt)
    contact = Contact()

    contact.name = name_recog.find_best_guessed_name(tokens)[2]

    for token in tokens:
        # if name_recog.is_name(token):
        #     contact.name = token
        if is_email(token):
            contact.emails.append(token)
        if is_phone(token):
            contact.phones.append(token)
        if is_job_title(token):
            contact.job_title = token
        if is_website(token):
            contact.website = token
    print(tokens)
    return contact


def extract(img_path):
    txt = pytesseract.image_to_string(Image.open(img_path))
    return txt


def tokenizer(txt):
    lines = txt.split("\n")
    tokens = []
    for line in lines:
        line = line.strip()
        if len(line) > 0:
            tokens.append(line)

    return tokens


def is_email(txt):
    txt = txt.lower()
    return (len(txt) >= 5 and txt.find("@") >= 0) \
           or (txt.find("mail") >= 0 and len(txt) >= 11)


def is_phone(txt):
    m = re.findall(r'\d', txt)
    if len(m) >= 8:
        return True
    return False


def is_website(txt):
    txt = txt.lower()
    return txt.find("\\\\") >= 0 or txt.find("www") >= 0


def is_job_title(txt):
    return False


# def is_name(txt):
#     return False


if __name__ == '__main__':
    # sample_path = 'business_cards/Reference/011.jpg'
    sample_path = '010.jpg'
    # sample_path = 'samples/BC_5.jpg'
    # sample_path = 'business_cards/Droid/010.jpg'
    contact = recognize_contact(sample_path)
    print(' ' * 30)
    print(' * ' * 30)
    print(jsonpickle.encode(contact))


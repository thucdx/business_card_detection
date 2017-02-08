from json import JSONEncoder

class Contact(object):
    def __init__(self):
        self.name = ''
        self.emails = []
        self.phones = []
        self.job_title = []
        self.company = ''
        self.website = ''
        self.other_info = {}

    # def __str__(self):
    #     return JSONEncoder.encode(self)

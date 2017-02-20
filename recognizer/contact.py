from json import JSONEncoder


class Contact(object):
    def __init__(self):
        self.name = 'N/A'
        self.emails = []
        self.phones = []
        self.job_title = 'N/A'
        self.company = 'N/A'
        self.website = 'N/A'
        self.addr = []
        self.other_info = {}

    # def __str__(self):
    #     return JSONEncoder.encode(self)

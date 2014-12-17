from email.utils import parseaddr as email_parseaddr

class Headers():
    def __init__(self, items):
        self._headers = [(key.lower(), decode_header(value)) for key, value in items]

    @property
    def hfrom(self):
        return email_parseaddr(self['from'])

    @property
    def hto(self):
        return email_parseaddr(self['from'])



    def __getitem__(self, name):
        return self._headers[name.lower()]


class Message():
    def __init__(self, headers, text, html, files):
        self.headers = Headers(headers)


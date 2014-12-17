import getpass
from imaplib import IMAP4, IMAP4_SSL

from smailbox.transports.base import EmailTransport

class ImapTransport(EmailTransport):
    def __init__(self, host, port=None, ssl=False):
        self.host = host
        self.port = port

        if ssl:
            self._transport = IMAP4_SSL
            if self.port is None:
                self.port = 993
        else:
            self._transport = IMAP4
            if self.port is None:
                self.port = 143
        self._connection = None

    def connect(self, username, password):
        self._connection = self._transport(username, password)
        self._connection.login(username, password)
        self._connection.select()

    def get_message(self):
        # @todo
        pass


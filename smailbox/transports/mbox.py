__author__ = 'smialy'

import mailbox

from smailbox.transports.base import FileTransport


class GenericFileTransport(FileTransport):

    def get_message(self):
        respository = self.get_instance(self.get_filepath())
        respository.lock()
        for msg in respository:
            yield msg
        respository.unlock()

    def get_instance(self):
        return self._instance(self.get_filepath())


class MboxTransport(GenericFileTransport):
    _instance = mailbox.mbox


class MaildirTransport(GenericFileTransport):
    _instance = mailbox.Maildir


class MMDFTransport(GenericFileTransport):
    _instance = mailbox.MMDF


class MHTransport(GenericFileTransport):
    _instance = mailbox.MH


class MHTransport(GenericFileTransport):
    _instance = mailbox.Babyl


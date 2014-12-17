__author__ = 'smialy'

import sys
import os.path
import abc


class EmailTransport(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_message(self):
        pass

class FileTransport(EmailTransport):
    def __init__(self, filepath):
        if not os.path.exists(filepath):
            raise FileNotFoundError('Nof found file: "{0}"'.format(self.filepath))
        self._filepath = filepath

    def get_filepath(self):
        return self._filepath
from common import *
import string
import requests
import sys
import logging
logger = logging.getLogger(__name__)

class Analyzer:
    def _check_printable(self, message):
        for c in self._unprintable:
            if c in message:
                return False
        return True

    def _values_to_percentage(self, values):
        total = sum(values.values())
        for key in values:
            values[key] = (float(values[key]) / total) * 100
        return values

    def _init_checking_values(self, url):
        logger.info("Downloading checking text (%s)" % (url))
        response = requests.get(url)
        content  = response.content
        values = {}
        logger.info("Initializing checking values")
        for c in string.printable:
            values[c] = 0
        for c in content:
            if c in string.printable:
                values[c] += 1
        self.checking_values = self._values_to_percentage(values)
        logger.info("Done initializing")

    def _init_highest_values(self):
        self.highestText  = ""
        self.highestValue = -1
        self.highestKey   = ""
        self.highestNr    = 0

    def _init_unprintable(self):
        self._unprintable = [chr(i) for i in xrange(0, 0x100)]
        for c in string.printable:
            if c in self._unprintable:
                self._unprintable.pop(self._unprintable.index(c))

    def __init__(self, checking_url="http://www.textfiles.com/etext/AUTHORS/JEFFERSON/jefferson-summary-260.txt"):
        self._init_unprintable()
        self._init_checking_values(checking_url)
        self._init_highest_values()

    def _analyze(self, message):
        total = 0.0
        for c in message:
            if c in string.printable:
                total += self.checking_values[c]
        return (float(total) / len(message))

    def incremental_brute(self, ciphertext):
        self.highestNr += 1
        keys = [chr(i) for i in xrange(0, 0x100)]
        for key in keys:
            message = xor(ciphertext, key)
            if self._check_printable(message):
                value = self._analyze(message)
                if (value > self.highestValue):
                    self.highestValue = value
                    self.highestText  = message
                    self.highestKey   = key

    def single_brute(self, ciphertext):
        self._init_highest_values()
        self.incremental_brute(ciphertext)

    def getCurrent(self):
        logger.info("[Score = %.2f, key='\\x%x', nr=%d] %s" % (self.highestValue, \
                                                         ord(self.highestKey), \
                                                         self.highestNr, \
                                                         self.highestText))
    def getLikelyKey(self):
        return self.highestKey

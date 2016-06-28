import string
import requests


class Analyzer:
    def __values_to_percentage(self, values):
        total = sum(values.values())
        for key in values:
            values[key] = (float(values[key]) / total) * 100
        return values

    def __init__(self):
        url = "http://www.textfiles.com/etext/AUTHORS/JEFFERSON/jefferson-summary-260.txt"
        response = requests.get(url)
        content  = response.content
        values = {}
        for c in string.printable:
            values[c] = 0
        for c in content:
            if c in string.printable:
                values[c] += 1
        self.checking_values = self.__values_to_percentage(values)

    def analyze(self, message):
        total = 0.0
        for c in message:
            if c in string.printable:
                total += self.checking_values[c]
        return (float(total) / len(message)) 
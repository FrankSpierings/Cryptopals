import requests
from analyzer import Analyzer

def main():
    analyzer = Analyzer()
    response = requests.get("http://cryptopals.com/static/challenge-data/4.txt")
    content  = response.content.split('\n')
    for line in content:
        decoded_str = line.decode("hex")
        analyzer.incremental_brute(decoded_str)
    analyzer.getCurrent()

if __name__ == "__main__": main()


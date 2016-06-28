import keyanalyzer
import analyzer
import requests
from common import *
import base64

def main():
    response = requests.get("http://cryptopals.com/static/challenge-data/6.txt")
    content = base64.b64decode(response.content)
    ka = keyanalyzer.KeyAnalyzer()
    ka.analyze(content)
    an = analyzer.Analyzer()
    key = ""
    for keysize in ka.keysize_order():
        blocks = transpose_blocks(content, keysize)
        for block in blocks:
            an.single_brute(block)
            key += an.getLikelyKey()
        logger.info("Keysize %d - Key=%s" % (keysize,repr(key)))


if __name__ == '__main__':
    import logging.config
    import logging
    logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
    logger = logging.getLogger(__name__)
    main()
from common import *
import requests
import base64

def main():
    response = requests.get("http://cryptopals.com/static/challenge-data/8.txt")
    content = response.content
    linenr= 0
    for line in content.split("\n"):
        linenr+=1
        counter=0
        logger.info("Line: %d" % linenr)
        blocks = get_blocks(line.decode("hex"), 8)
        for block in blocks:
            counter += (blocks.count(block)-1)
            logger.info("Counter %d; Block: %s" % (counter, repr(block)))
            while block in blocks:
                blocks.pop(block.index(block))

            



if __name__ == '__main__':
    import logging.config
    import logging
    logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
    logger = logging.getLogger(__name__)
    main()
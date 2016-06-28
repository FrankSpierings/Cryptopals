from common import *
import logging
logger = logging.getLogger(__name__)


class KeyAnalyzer():
    def __init__(self):
        self.distances={}

    def analyze(self, data, maxkeysize=45):
        if (maxkeysize > (len(data)/2)):
            maxkeysize = (len(data)/2)
        logger.debug("Maximum keysize: %d" % (maxkeysize))
        for keysize in xrange(2, maxkeysize):
                logger.debug("Testing keysize %d" % (keysize))
                blocks = get_blocks(data, keysize, exclude_smaller=True)
                total_distance = []
                for index in xrange(0, (len(blocks)-1)):
                    distance = hamming_distance(blocks[index], blocks[index+1])
                    normalized_distance = float(distance / keysize)
                    logger.debug("Block: %s vs %s" % (repr(blocks[index]), repr(blocks[index+1]) ))
                    logger.debug("Comparing block %d to %d; normalized distance: %f" % (index, index+1, normalized_distance))
                    total_distance += [normalized_distance]
                
                average_distance = float(sum(total_distance)/len(total_distance))
                logger.debug("Hamming distance average %f (sum(%s)/%d)" % (average_distance, repr(total_distance), len(total_distance)))
                self.distances[keysize] = average_distance

    def print_result(self):
        order=self.keysize_order()
        for i in order:
            logger.debug("Keysize %d - Value: %f" % (i, self.distances[i]))

    def keysize_order(self):
        return sorted(self.distances, key=self.distances.__getitem__, reverse=False)
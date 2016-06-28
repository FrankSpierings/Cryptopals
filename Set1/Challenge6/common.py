def hamming_distance(str1, str2):
    if (len(str1) != len(str2)):
        raise ValueError("Strings not equal in length")
    r = 0
    for c1, c2 in zip(str1, str2):
        r += '{0:08b}'.format( ord(c1) ^ ord(c2) ).count('1')
    return r

def get_blocks(data, blocksize, exclude_smaller=True):
    if (not exclude_smaller):
        r = [ data[i:i+blocksize] for i in xrange(0, len(data), blocksize)]
    else:
        r = [ data[i:i+blocksize] for i in xrange(0, ((len(data)/blocksize)*blocksize), blocksize)]
    return r

def transpose_blocks(data, keysize):
    #abcdefghi 3
    #[adg] [beh] [cfi]
    #
    #abcdefgh 3
    #[ad] [be] [cf]
    blocks = []
    for offset in xrange(0, keysize):
        block = ""
        for index in xrange(offset, len(data)/keysize*keysize, keysize):
            block += data[index]
        blocks += [block]
    return blocks


def xor(message, key):
    ik = 0
    lk = len(key)
    result = ""
    for im in range(0, len(message)):
        if(ik == lk):
            ik = 0
        result += chr(ord(message[im]) ^ ord(key[ik]))
        ik += 1
    return result
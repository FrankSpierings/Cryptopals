import string
from analyzer import Analyzer

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

def hexdecode(encoded):
    split = [encoded[i:i+2] for i in range(0,len(encoded),2)]
    decoded_tuple = [chr(int(c, base=16)) for c in split]
    decoded = ''.join(decoded_tuple)
    return decoded

def brute(ciphertext):
    analyzer = Analyzer()
    highestText  = ""
    highestValue = 0
    keys = [chr(i) for i in xrange(0, 0x100)]
    for key in keys:
        message = xor(ciphertext, key)
        value = analyzer.analyze(message)
        if (value > highestValue):
            highestValue = value
            highestText  = message
    print "[Score = %f] %s" % (highestValue, highestText)


# def check_printable(message):
#     unprintable = [chr(i) for i in xrange(0, 0x100)]
#     for c in string.printable:
#         if c in unprintable:
#             unprintable.pop(unprintable.index(c))
#     for c in unprintable:
#         if c in message:
#             return False
#     return True

def main():
    encoded_str = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    decoded_str = hexdecode(encoded_str)
    brute(decoded_str)

if __name__ == "__main__": main()
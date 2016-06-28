import string

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


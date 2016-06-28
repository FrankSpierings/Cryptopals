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

def main():
    encoded_str = "1c0111001f010100061a024b53535009181c"
    encoded_key = "686974207468652062756c6c277320657965"
    decoded_str = hexdecode(encoded_str)
    decoded_key = hexdecode(encoded_key)
    print xor(decoded_str, decoded_key)

if __name__ == "__main__": main()
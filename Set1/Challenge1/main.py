def hexdecode(encoded):
    split = [encoded[i:i+2] for i in range(0,len(encoded),2)]
    decoded_tuple = [chr(int(c, base=16)) for c in split]
    decoded = ''.join(decoded_tuple)
    return decoded

def main():
    encoded = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    print hexdecode(encoded)

if __name__ == "__main__": main()
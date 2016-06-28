from Crypto.Cipher import AES
import requests
import base64


def ECB_Encrypt(message, key):
    cipher = AES.AESCipher(key, mode=AES.MODE_ECB)
    ciphertext = cipher.encrypt(message)
    return ciphertext

def ECB_Decrypt(ciphertext, key): 
    cipher = AES.AESCipher(key, mode=AES.MODE_ECB)
    message = cipher.decrypt(ciphertext)
    return message

def main():
    key = "YELLOW SUBMARINE"
    url = "http://cryptopals.com/static/challenge-data/7.txt"
    response = requests.get(url)
    content = base64.b64decode(response.content)
    print ECB_Decrypt(content,key)

if __name__ == "__main__": main()
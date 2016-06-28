from common import *


def main():
	content = '''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''
	ciphertext = xor(content, "ICE")
	print ciphertext.encode("hex")

if __name__ == "__main__": main()
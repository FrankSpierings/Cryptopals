def pkcs7_pad(message, blocksize=8):
    modulus = len(message) % blocksize
    if (modulus):
        pad_length = blocksize - modulus
    else:
        pad_length = blocksize
    padding = chr(pad_length) * pad_length
    return message + padding
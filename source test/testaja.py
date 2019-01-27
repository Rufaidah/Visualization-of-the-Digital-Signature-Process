import rsa
import base64

(pub_key, priv_key) = rsa.newkeys(512, poolsize=2)

def encryption(file):
    # encrypt
    crypto = rsa.encrypt(file.encode('utf-8'), pub_key)
    result = crypto.decode('utf-8', errors='ignore')
    return crypto, result


def decryption(crypto):
    # decrypt
    crypto = rsa.decrypt(crypto, priv_key)
    return crypto.decode('utf8')


filename = "/home/rufaidah/Documents/TA/chapter13.pdf"

with open(filename, mode='rb') as file:
    test = base64.b64encode(file.read())


result_b64 = test.decode('ascii')

print("hasil base64 =>", result_b64)
print("melakukan enkripsi => ", filename)
crypto, result = encryption(result_b64)
print("hasil enkripsi => ", result)
print("melakukan dekripsi . . .")
print("hasil deksripsi => ", decryption(crypto))
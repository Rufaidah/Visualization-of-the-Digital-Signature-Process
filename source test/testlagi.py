from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import zlib
import base64

#result_b64 = "jeklfklfjlkawjfkawjfwaafwwfwaawfwjawfwafaf23535wa324f"

def encrypt_blob(blob, public_key):
    rsa_key = RSA.importKey(public_key)
    rsa_key = PKCS1_OAEP.new(rsa_key)
    blob = zlib.compress(blob)

    chunk_size = 512
    offset = 0
    end_loop = False
    encrypted =  ""

    while not end_loop:
        chunk = blob[offset:offset + chunk_size]

        if len(chunk) % chunk_size != 0:
            end_loop = True
            chunk += " " * (chunk_size - len(chunk))

        encrypted += rsa_key.encrypt(chunk)
        offset += chunk_size

    return base64.b64encode(encrypted)


def decrypt_blob(encrypted_blob, private_key):
    rsakey = RSA.importKey(private_key)
    rsakey = PKCS1_OAEP.new(rsakey)
    encrypted_blob = base64.b64decode(encrypted_blob)

    chunk_size = 512
    offset = 0
    decrypted = ""

    while offset < len(encrypted_blob):
        chunk = encrypted_blob[offset: offset + chunk_size]
        decrypted += rsakey.decrypt(chunk)
        offset += chunk_size

    return zlib.decompress(decrypted)


fd = open("public.pem", "rb")
public_key = fd.read()
fd.close()

filename = "/home/rufaidah/Documents/TA/test.jpg"

fd = open(filename, "rb")
unencrypted_blob = fd.read()
fd.close()

encrypted_blob = encrypt_blob(unencrypted_blob, public_key)
print("hasil encryption => ", encrypted_blob)
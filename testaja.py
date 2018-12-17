from Crypto.PublicKey import RSA
from Crypto import Random

def test(filename):
    # Pembuatan kunci
    # Fungsi untuk menghasilkan data random
    rng = Random.new().read
    # Generate kunci dengan panjang 5120 bit
    key = RSA.generate(256 * 20, rng)
    # Export private-key ke private.pem
    open('private.pem', 'wb').write(key.exportKey())
    # Export public-key ke public.pem
    open('public.pem', 'wb').write(key.publickey().exportKey())

    # Enkripsi
    file = filename
    file_to_encrypt = open(file, 'rb').read()
    key = open('public.pem', 'rb').read()
    # pub_key = open('my_pub_key.pem', 'rb').read()
    o = RSA.importKey(key)

    to_join = []
    step = 0

    while 1:
        # Read 128 characters at a time.
        s = file_to_encrypt[step * 128:(step + 1) * 128]
        if not s: break
        # Encrypt with RSA and append the result to list.
        # RSA encryption returns a tuple containing 1 string, so i fetch the string.
        to_join.append(o.encrypt(s, 0)[0])
        step += 1

    # Join the results.
    # I hope the \r\r\r sequence won't appear in the encrypted result,
    # when i explode the string back for decryption.
    return to_join

print(test("/home/rufaidah/Documents/TA/ui/public.pem"))
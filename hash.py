import binascii
import pycryptonight

for x in range(500):
    m = "Hello RandomX {}".format(x)
    bh = pycryptonight.cn_fast_hash(m)
    hh = binascii.hexlify(bh).decode()
    print("Result: {}".format(hh))

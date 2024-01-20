import binascii
import pycryptonight

for x in range(5):
    m = "Hello RandomX {}".format(x)
    bh = pycryptonight.cn_slow_hash(m, 4, 0, 1)
    hh = binascii.hexlify(bh).decode()
    print("Result: {}".format(hh))

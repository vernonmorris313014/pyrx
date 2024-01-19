import pyrx
import time
import binascii


seed_hash = binascii.unhexlify('63eceef7919087068ac5d1b7faffa23fc90a58ad0ca89ecb224a2ef7ba282d48')

def current_milli_time():
    return round(time.time() * 1000)


start = current_milli_time()

x = 0

print(current_milli_time() - start)

while(current_milli_time() - start < 10000):
    m = "Hello RandomX {}".format(x)
    print("Hashing: {}".format(x))
    h = x
    x += 1
    bh = pyrx.get_rx_hash(m, seed_hash, h)
    hh = binascii.hexlify(bh).decode()
    print("Result: {}".format(hh))

print("Hashing: {}".format(x))

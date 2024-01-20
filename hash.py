import binascii
import pycryptonight

hash = pycryptonight.cn_fast_hash(b'1')
print(hash)
# hexcoded: b'c89efdaa54c0f20c7adf612882df0950f5a951637e0307cdcb4c672f298b8bc6

hash = pycryptonight.cn_slow_hash(b'1')
print(hash)
# hexcoded: b'cbdfba46388e040422b4a9daa471726be659ae184ee86420c2795647f0b301d5

# variant 1:
hash = pycryptonight.cn_slow_hash(binascii.unhexlify(b'38274c97c45a172cfc97679870422e3a1ab0784960c60514d816271415c306ee3a3ed1a77e31f6a885c3cb'), 1)  # variant 1
print(hash)
# hexcoded: b'ed082e49dbd5bbe34a3726a0d1dad981146062b39d36d62c71eb1ed8ab49459b

# variant 2:
hash = pycryptonight.cn_slow_hash(b'1', 2)  # variant 2
print(hash)
# hexcoded: b'44016d2376838d89b374e99a20118c0e8916e8c0a5b910744efc7d8f426509ca

# variant 4:
hash = pycryptonight.cn_slow_hash(b'1', 4)  # variant 4
print(hash)
# hexcoded: b'97db7e03629f7c17e4d78b36a2d247d226b88a8df6cf69f2e4cdae1f1b706b4a

# variant 4, height:
hash = pycryptonight.cn_slow_hash(b'1', 4, prehashed=0, height=1)  # variant 4, height 1
print(hash)
# hexcoded: b'09bcf4997132dc3d7980125620724acc9c90dc393cb6694097a7d745c57b6b5b

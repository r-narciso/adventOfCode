#!/usr/bin/env python

import hashlib
key = "ckczppom"
hash = ''
index = 0
while hash[0:5] != "00000":
    index += 1
    hash = hashlib.md5((key + str(index)).encode('utf-8')).hexdigest()
print("index = %d"%index)
print("hash = %s"%str(hash))

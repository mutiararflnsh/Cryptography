import binascii
from unittest import result

code = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
flag = ''

bytetext = bytearray.fromhex(code)

for i in range(256):
    trans = []
    for n in bytetext:
        trans.append(chr(n^i))
    
    flag = "".join(trans)
    if (flag.startswith('crypto')):
        print(flag)
        print(i)

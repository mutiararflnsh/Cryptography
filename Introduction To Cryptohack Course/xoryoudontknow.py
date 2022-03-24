from pwn import xor
import binascii

code = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")

partial_key = "myXORkey"

key = (partial_key * (len(code)//len(partial_key)+1))[:len(code)]

flag = xor(code, key)

print(flag)
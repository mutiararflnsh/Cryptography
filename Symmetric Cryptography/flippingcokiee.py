import requests

BASE_URL = "http://aes.cryptohack.org/flipping_cookie"
BLOCKSIZE = 32

def split_blocks(ctxt, blocksize=BLOCKSIZE):
    if len(ctxt) % blocksize != 0:
        raise Exception("!")
    else:
        number_of_blocks = len(ctxt) // blocksize
        return [ctxt[i*blocksize:(i+1)*blocksize] for i in range (number_of_blocks)]

def get_cookie():
    get_cookie_request = requests.get(f"{BASE_URL}/get_cookie/")
    return get_cookie_request.json()["cookie"]

def check_admin(cookie, iv):
    check_admin_request = requests.get(f"{BASE_URL}/check_admin/{cookie}/{iv}")
    return check_admin_request.json()

def string_to_hex(txt):
    return txt.encode("utf-8").hex()

def hex_xor(s1, s2):
    a = bytes.fromhex(s1)
    b = bytes.fromhex(s2)
    result = bytes([b1 ^ b2 for b1, b2 in zip(a,b)])
    return result.hex()

ciphertext = get_cookie()
ciphertext_blocks = split_blocks(ciphertext)
IV = ciphertext_blocks[0]
cookie = ciphertext_blocks[1] + ciphertext_blocks[2]

P_known = "admin=False;expi"
P_expected = "admin=True;expir"
Pk_hex = string_to_hex(P_known)
Pe_hex = string_to_hex(P_expected)

D = hex_xor(Pk_hex, IV)

IV_crafted_hex = hex_xor(D, Pe_hex)

FLAG = check_admin(cookie, IV_crafted_hex)

print(FLAG)
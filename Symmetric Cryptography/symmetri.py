import requests

ciphertext_hex = requests.get('http://aes.cryptohack.org/symmetry/encrypt_flag/').json() # {'ciphertext': '8cd8ac578bf1add64379a8f66a98c86f6bd87c5967d77aa073ad25afd8cf26d23f0c1a4bead27f6ab34c38adf2d74ad4a4'}
ciphertext = ciphertext_hex['ciphertext']
# print(ciphertext) # '8cd8ac578bf1add64379a8f66a98c86f6bd87c5967d77aa073ad25afd8cf26d23f0c1a4bead27f6ab34c38adf2d74ad4a4'


iv = ciphertext[:16*2] # iv is 32 first hex characters of ciphertext
# print(iv) # iv = '8cd8ac578bf1add64379a8f66a98c86f'

ciphertext = ciphertext[32:]
# print(ciphertext) # ciphertext = '6bd87c5967d77aa073ad25afd8cf26d23f0c1a4bead27f6ab34c38adf2d74ad4a4'


plaintext_hex = requests.get('http://aes.cryptohack.org/symmetry/encrypt/'+ciphertext+'/'+iv+'/').json() # {'ciphertext': '63727970746f7b3066625f31355f35796d6d3337723163346c5f2121213131217d'}
plaintext = plaintext_hex['ciphertext'] # plaintext = '63727970746f7b3066625f31355f35796d6d3337723163346c5f2121213131217d'
plaintext = bytes.fromhex(plaintext) # Decode hex
print(plaintext)
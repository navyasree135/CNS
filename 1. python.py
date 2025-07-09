ceaser cipher
def caesar_encrypt(text, k):
    return ''.join(chr((ord(c)-97+k)%26+97) if c.isalpha() else c for c in text.lower())
print(caesar_encrypt("hello", 3))  # khoor

mono alphabetic cipher
import string
key = dict(zip(string.ascii_lowercase, "QWERTYUIOPASDFGHJKLZXCVBNM".lower()))
def mono_encrypt(text): return ''.join(key.get(c, c) for c in text.lower())
print(mono_encrypt("hello"))  # itssg

poly alphabetic cipher/vigener cipher
def vigenere_encrypt(text, key):
    return ''.join(chr((ord(t)-97+ord(key[i%len(key)])-97)%26+97) for i, t in enumerate(text.lower()) if t.isalpha())
print(vigenere_encrypt("attackatdawn", "lemon"))  # lxfopvefrnhr

affine cipher
def affine_encrypt(text, a, b): return ''.join(chr((a*(ord(c)-97)+b)%26+97) if c.isalpha() else c for c in text.lower())
print(affine_encrypt("hello", 5, 8))  # rclla

hill cipher
import numpy as np
def hill(msg, key):
 m = [ord(c)-97 for c in msg]
 k = np.array(key).reshape(2,2)
 return ''.join(chr(x%26+97) for i in range(0,len(m),2) for x in k.dot(m[i:i+2]))
print(hill("meetme", [9,4,5,7]))

one-time tap
def otp_encrypt(msg, key):
    return ''.join(chr((ord(c)-97+k)%26+97) for c, k in zip(msg, key))
print(otp_encrypt("sendmoremoney", [9,0,1,7,23,15,21,14,11,11,2,8,9]))  # encrypted

rsa key
from Crypto.Util.number import inverse
e, n = 31, 3599
p, q = 59, 61  # trial factorization
phi = (p-1)*(q-1)
d = inverse(e, phi)
print(f"Private key: {d}")  # 1163

play fair cipher
def create_matrix(key):
    key = "".join(dict.fromkeys(key + "abcdefghiklmnopqrstuvwxyz"))
    return [list(key[i:i+5]) for i in range(0, 25, 5)]

def pos(m, c):
    for i in range(5):
        for j in range(5):
            if m[i][j] == c: return i, j

def playfair_encrypt(msg, key):
    msg = msg.replace("j", "i").lower()
    if len(msg) % 2: msg += 'x'
    matrix = create_matrix(key)
    res = ''
    for i in range(0, len(msg), 2):
        a, b = msg[i], msg[i+1]
        if a == b: b = 'x'
        r1, c1 = pos(matrix, a)
        r2, c2 = pos(matrix, b)
        if r1 == r2: res += matrix[r1][(c1+1)%5] + matrix[r2][(c2+1)%5]
        elif c1 == c2: res += matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c2]
        else: res += matrix[r1][c2] + matrix[r2][c1]
    return res
print(playfair_encrypt("hello", "monarchy"))  # encrypted text

keyword-based mono alphabetic Cipher
from string import ascii_lowercase
def keyword_cipher(text, keyword):
    key = "".join(dict.fromkeys(keyword + ascii_lowercase))
    table = str.maketrans(ascii_lowercase, key)
    return text.lower().translate(table)
print(keyword_cipher("hello", "cipher"))  # output varies

simple substitution cipher
cipher = "53‡‡†305))6*;4826)...etc..."  # your actual ciphertext
mapping = {
    '‡': 'e', '†': 't', '8': 'h', '5': 'o', '3': 'm', '0': 'n',
    '6': 's', '4': 'r', '2': 'a', ')': 'l', '*': 'd', ';': 'i'
    # Add more symbols as you decipher further
}
plain = ''.join(mapping.get(c, '?') for c in cipher)
print(plain)







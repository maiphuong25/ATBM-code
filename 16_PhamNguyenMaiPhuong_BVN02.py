def caesar_encrypt(plaintext, k):
    ciphertext = ""
    for ch in plaintext:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            c = (ord(ch) - base + k) % 26 + base
            ciphertext += chr(c)
        else:
            ciphertext += ch  
    return ciphertext

P = "PhamNguyenMaiPhuong"
k = 16

C = caesar_encrypt(P, k)
print("Plaintext :", P)
print("Ciphertext:", C)

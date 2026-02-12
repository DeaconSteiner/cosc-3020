# solution.py
# Deacon Steiner
# COSC 3020
# Lab03
# 11 February, 2026

def gcd(a, b):
    if b == 0:
        return a;
    return gcd(b, a % b)

def ext_gcd(a, b):
    if b == 0:
        return (a, 1, 0)
    (g, x1, y1) = ext_gcd(b, a % b)
    return (g, y1, x1 - (a//b)*y1)

def mod_inverse(e, phi):
    g, x, y = ext_gcd(e, phi)
    if g != 1:
        raise ValueError("No inverse exists")
    return x % phi

def rsa_keygen(p, q, e):
    n = p*q
    phi = (p-1)*(q-1)
    if gcd(e, phi) == 1:
        d = mod_inverse(e, phi)
        public_key = (e, n)
        private_key = (d, n)
    else:
        raise ValueError("E and phi are not coprime")
    return public_key, private_key

def encrypt(m, public_key):
    e, n = public_key
    return pow(m, e, n)

def decrypt(c, private_key):
    d, n = private_key  
    return pow(c, d, n)

def main():
    p = 61
    q = 53
    e = 17
    n = p*q
    phi = (p-1)*(q-1)

    pub, priv = rsa_keygen(p, q, e)
    print(f"N = {n}, phi = {phi}")
    print(f"Public key is: {pub} and Private key is: {priv}")

    for grade in [92, 7, 100]:
        ciphertext = encrypt(grade, pub)
        print(f"Encrypted grade is: {ciphertext}")
        recovered = decrypt(ciphertext, priv)
        print(f"Recovered grade is: {recovered}")
        if recovered == grade:
            print("OK\n")
        else: 
            raise ValueError(f"Mismatch: {recovered} != {grade}")

if __name__ == "__main__":
    main()

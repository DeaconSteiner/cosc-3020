# test.py
# Deacon Steiner
# COSC 3020
# Lab03
# 11 February, 2026

from solution import *

def main():
    print(gcd(30, 12))
    print(ext_gcd(30, 12))
    print(mod_inverse(17, 3120))
    pub, priv = rsa_keygen(61, 53, 17)
    print(pub)
    print(priv)

if __name__ == "__main__":
    main()

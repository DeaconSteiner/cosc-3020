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


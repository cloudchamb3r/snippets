# three prime numbers 
p1,p2,p3 = 2,5,11

# c_k == flag % p_k
c1,c2,c3 = 1,3,2


def egcd(a, b): 
    if a == 0: return b, 0, 1
    gcd, x, y = egcd(b % a, a) 
    return gcd, y - (b//a) * x, x

M = p1 * p2 * p3 
m1, m2, m3 = (p2 * p3, p1 * p3, p1 * p2)

gcd, a, b = egcd(m1, p1)
i1 = (a % p1)

gcd, a, b = egcd(m2, p2) 
i2 = (a % p2)

gcd, a, b = egcd(m3, p3) 
i3 = (a % p3)

flag = (c1 * m1 * i1 + c2 * m2 * i2 + c3 * m3 * i3) % M 
print(flag)

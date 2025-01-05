from Crypto.Util.number import getPrime, bytes_to_long
from math import gcd

flag = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
FLAG = flag.encode()

out = open('output.txt', 'w')

rsa_q = getPrime(512)
rsa_p = getPrime(512)
n = rsa_q * rsa_p
exp1 = 0x10003
exp2 = 0x10001

assert gcd(exp1, exp2) == 1
assert gcd(exp1, n) == 1
assert gcd(exp2, n) == 1

    
def encryption(plaintext):
    cip1 = pow(plaintext, exp1, n)
    cip2 = pow(plaintext, exp2, n)
    return (cip1, cip2)

cip1, cip2 = encryption(bytes_to_long(FLAG))

out.write("n = "+ str(n)+ "\ncip1 = "+ str(cip1)+ "\ncip2 = "+str(cip2))
out.close()

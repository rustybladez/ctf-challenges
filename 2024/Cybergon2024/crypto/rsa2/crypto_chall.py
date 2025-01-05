from Crypto.Util.number import getPrime

e = 65537
p = getPrime(1024)
q = getPrime(1024)
n = p * q

print("n =", n)

value1 = p
value2 = 2 ** 1024
value3 = getPrime(1024)   
value4 = getPrime(1024) 

def Calculation():
    global value1, value2, value3, value4
    output = 0
    value1_ = value1
    value3_ = value3
    while value3_ > 0:
        if (value3_ & 1) == 1:
            output = (output + value1_) % value2
        value1_ = (value1_ * 2) % value2
        value3_ >>= 1
    value1 = (output + value4) % value2
    return value1

plaintext = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
int_plaintext = int.from_bytes(plaintext.encode(), 'big')
encrypted = pow(int_plaintext, e, n)

print("enc =", encrypted)

for num in range(3):
    print("Result", Calculation())

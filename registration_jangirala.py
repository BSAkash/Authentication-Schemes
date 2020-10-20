import nacl.hash
import random
import math
import binascii

def strtobin(x):
    e=x.encode('utf-8')
    h = binascii.hexlify(e)
    i = int(h, 16)
    return i

def concatenate(a, b="", c="", d="", e="", f=""):
	temp = str(a) + str(b) + str(c) + str(d) + str(e) + str(f)
	temp = temp.encode()
	return temp


print("Please enter your ID")
ID = input()

print("Enter your password")
PW = input()

b= random.randrange(50,9999,1)
print("secret key")
x = input()
y = random.randrange(50,9999,1)
A = int(nacl.hash.sha256(concatenate(strtobin(ID) ^ (b) ^ strtobin(PW))),16)
# print(A)
B = nacl.hash.sha256(concatenate(A, x))
# print('bbbbbbbbbbbbbbbbbbbbbbb', int(B,16))
C = nacl.hash.sha256(concatenate(ID,(nacl.hash.sha256(concatenate(y))),A))
Z = nacl.hash.sha256(concatenate(x,y))
D = nacl.hash.sha256(concatenate(B,Z))
E = int(B, 16) ^ int(Z, 16)
# print('eeeeeeeeeeeeeeee', E)
L = b ^ int(nacl.hash.sha256(concatenate(ID, PW)), 16)
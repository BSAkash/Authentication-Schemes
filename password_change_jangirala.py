import nacl.hash
import random
import sys
import math
import binascii
from registration_jangirala import x,y,Z,D
from login_jangirala import *
from authen_jangirala import *

def strtobin(x):
    e=x.encode('utf-8')
    h = binascii.hexlify(e)
    i = int(h, 16)
    return i


b = L ^ int(nacl.hash.sha256(concatenate(ID,PW)),16)
A = int(nacl.hash.sha256(concatenate(strtobin(ID) ^ (b) ^ strtobin(PW))),16)
C1 = nacl.hash.sha256(concatenate(ID,(nacl.hash.sha256(concatenate(y))),A))
temp=0
while temp==0:
    if C1 == C:
        temp=1
        continue
    elif C1 != C:
        print("Authentication failed and login terminated")
        temp=1
        sys.exit()

print("New password")
PW_new = input()
A_new = int(nacl.hash.sha256(concatenate(strtobin(ID) ^ (b) ^ strtobin(PW_new))),16)
# A = int(nacl.hash.sha256(concatenate(strtobin(ID) ^ (b) ^ strtobin(PW))),16)
C_new = nacl.hash.sha256(concatenate(ID,(nacl.hash.sha256(concatenate(y))),(A_new)))
L_new = (b) ^ int(nacl.hash.sha256(concatenate(ID,(PW_new))),16)
print(int(SK,16))
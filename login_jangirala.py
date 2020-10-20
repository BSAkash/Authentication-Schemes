import nacl.hash
import random
import sys
import math
import binascii
from registration_jangirala import *

def strtobin(x):
    e=x.encode('utf-8')
    h = binascii.hexlify(e)
    i = int(h, 16)
    return i

b = L ^ int(nacl.hash.sha256(concatenate(ID,PW)),16)
# A = nacl.hash.sha256(concatenate(strtobin(ID) ^ (b) ^ strtobin(PW)))
# print('A',A)
C1 = nacl.hash.sha256(concatenate(ID,(nacl.hash.sha256(concatenate(y))),A))
# print(C1)
# print(C)    
temp=0
while temp==0:
    if C1 == C:
        temp=1
        continue
    elif C1 != C:
        print("Authentication failed and login terminated")
        temp=1
        sys.exit()
N = random.randrange(50,9999,1)
print("server identity")
SID = input()
CID = A ^ int(nacl.hash.sha256(concatenate(D,SID,N)),16)
# print('eeeeeeeeeeeeeeeeeeeeeeeeeee', E)
P = E ^ int(nacl.hash.sha256(concatenate(nacl.hash.sha256(concatenate(SID,(nacl.hash.sha256(concatenate(y))))),N)),16)
# print('eeeeeeeeeeeeeeeeeeeeeeeeeeee', E)
M1 = nacl.hash.sha256(concatenate(P,CID,A,N))
# print("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")
# print(D)
# print(SID)
# print(N)
# print('A', A)
# print("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")
M2 = int(nacl.hash.sha256(concatenate(SID,(nacl.hash.sha256(concatenate(y))))),16) ^ (N)
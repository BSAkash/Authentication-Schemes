import nacl.hash
import random
import sys
import math
import binascii
import time
from registration_jangirala import x,y,Z,D
from login_jangirala import *


def strtobin(x):
    e=x.encode('utf-8')
    h = binascii.hexlify(e)
    i = int(h, 16)
    return i

# ar2=[]
# count2 = 0 
# array =[100,200,300,400,500]
# for i in array:
#     while(i!=0):
# start_time = time.time()
N = M2 ^ int(nacl.hash.sha256(concatenate(SID,(nacl.hash.sha256(concatenate(y))))),16)
E = P ^ int(nacl.hash.sha256(concatenate(str(nacl.hash.sha256(concatenate(SID,(nacl.hash.sha256(concatenate(y)))))),N)),16)
# print('eeeeeeeeeeeeeeeeeeeee',E)
B = E ^ int(Z,16)
# print('bbbbbbbbbbbbbbbb', B)
# D = nacl.hash.sha256(concatenate(B,Z))
A = (CID ^ int(nacl.hash.sha256(concatenate(D,SID,N)),16))
# print("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")
# print(D)
# print(SID)
# print(N)
# print('A', A)
# print("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")
M11 = nacl.hash.sha256(concatenate(P,CID,A,N))
temp=0
while temp ==0:
    if M11 == M1:
        temp=1
        continue
    elif M11 != M1:
        print("Authentication failed and login terminated")
        temp=1
        sys.exit()
SK1 = nacl.hash.sha256(concatenate(D,A))    
N1 = random.randrange(50,9999,1)
M3 =  nacl.hash.sha256(concatenate(SK1,A,SID,N1))
M4 = int(SK1,16) ^ N1

SK1 = nacl.hash.sha256(concatenate(D,A))
N1 = M4 ^ int(SK1,16)
M31 = nacl.hash.sha256(concatenate(SK1,A,SID,N1))
while temp==0:
    if M31 == M3:
        temp=1
        continue
    elif M31 != M3:
        print("Received message is inaccurate")
        temp=1
        sys.exit()

M5 = nacl.hash.sha256(concatenate(SK1,A,SID,N,N1))

SK = nacl.hash.sha256(concatenate(SK1,A,SID,N,D,N1))
# print("aa")
# i=i-1
# count2 = count2 + time.time()-start_time
# print(count2)
# ar2.append(count2)
print(int(SK,16))
# import matplotlib.pyplot as plt
# plt.plot(array,ar2,'b')
# plt.show()
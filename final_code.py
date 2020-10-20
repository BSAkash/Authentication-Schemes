import tinyec
from tinyec import registry
import nacl.hash
import random
import sys
import math
import binascii
import time
curve = registry.get_curve('secp192r1')
import secrets
import os
import base64
from Crypto.Cipher import AES
P=curve.g
x= secrets.randbelow(curve.field.n)
Q=x*P
from CryptoAPI import *
# from authen_jangirala import count2,ar2
ar1=[]

def strtobin(x):
    e=x.encode('utf-8')
    h = binascii.hexlify(e)
    i = int(h, 16)
    return i

def concatenate(a, b="", c="", d="", e="", f=""):
	temp = str(a) + str(b) + str(c) + str(d) + str(e) + str(f)
	temp = temp.encode()
	return temp

# count = 0 
# array =[100,200,300,400,500]
# for i in array:

# 	while(i!=0):

print("Please enter your ID")
ID = input()

print("Enter your password")
PW = input()

print("server identity")
SID = input()

# start_time = time.time()

s = nacl.hash.sha256(concatenate(SID,x))
R = secrets.randbelow(curve.field.n)

 #//////////////////////////////////////////////////USER REGISTRATION////////////////////////////////////////////


r = secrets.randbelow(curve.field.n)
RPW = nacl.hash.sha256(concatenate(PW,r))
RID = nacl.hash.sha256(concatenate(ID,R))
K = int(nacl.hash.sha256(concatenate(RID,x)),16)
A = K ^ int(nacl.hash.sha256(concatenate(ID,RPW)),16)
B = nacl.hash.sha256(concatenate(K))






K1 = A ^ int(nacl.hash.sha256(concatenate(ID,nacl.hash.sha256(concatenate(PW,r)))),16)
B1 = nacl.hash.sha256(concatenate(K1))


temp=0
while temp==0:
    if B1 == B:
        temp=1
        continue
    elif B1 != B:
        print("login terminated")
        temp=1
        sys.exit()
alpha = secrets.randbelow(curve.field.n)
X = alpha * P
X1 = alpha * Q
list1 = [RID,nacl.hash.sha256(concatenate(K1,SID)) ]
CID = encrypt(nacl.hash.sha256(concatenate(X1)),list1)
zz,z = decrypt(nacl.hash.sha256(concatenate(X1)),CID)
beta = secrets.randbelow(curve.field.n)
#////////////////////////////////////////////////////////server///////////////////////////////////////
Y = beta * P
M = nacl.hash.sha256(concatenate(X,Y,s,SID))
list2 = [M,CID,X,Y]
V = encrypt(s,list2)
#////////////////////////////////////////////////////Registartion center/////////////////////////////
dec1,dec2,dec3,dec4 = decrypt(s,V)

# if  (M!=dec1) or (CID!=dec2) or (X!=dec3) or (Y!=dec4):
# 	print("cannot proceed further...error")

RID_new,dec5 = decrypt(nacl.hash.sha256(concatenate(x*X)),CID)

if K == K1 and nacl.hash.sha256(concatenate(K1,SID)) == z :
	print(" ") 
else:
	print("request aborted")

Y1 = x * Y
SK = nacl.hash.sha256(concatenate(RID,SID,X1,Y))
list3 = [SK,X,Y]
K = nacl.hash.sha256(concatenate(RID,x))
C2 = encrypt(K,list3)
list4 =[Y1,C2,SK]
D = encrypt(s,list4)
#///////////////////////////////server////////////////////////////////////////
dec6,dec7,dec8 = decrypt(s,D)
temp=0
while temp==0:
    if Y1 == beta * Q:
        temp=1
        continue
    elif Y1 != beta * Q:
        print("login terminated")
        temp=1
        sys.exit()
dec9,dec10,dec11 = decrypt(K,C2)
temp=0
while temp==0:
    if dec9 == nacl.hash.sha256(concatenate(RID,SID,X1,Y)):
        temp=1
        continue
    elif dec9 != nacl.hash.sha256(concatenate(RID,SID,X1,Y)):
        print("terminated")
        temp=1
        sys.exit()


	

F =nacl.hash.sha256(concatenate(SID,SK,X,Y))
F1 =nacl.hash.sha256(concatenate(SID,dec9,X,Y))
temp=0
while temp==0:
    if F1 == F:
    	# print(" a")
    	temp=1
    	continue
    elif F1 != F:
        print("terminated")
        temp=1
        sys.exit()

N = random.randrange(50,9999,1)
N1 = random.randrange(50,9999,1)
SK1 = alpha * beta * P
SK2 = nacl.hash.sha256(concatenate(SK,A,SID,N,D,N1))

print(SK1)

print(SK2)

# print("--- %s seconds ---" % (time.time() - start_time))

# i=i-1
# count = count + time.time()-start_time
# 	print(count)
# 	ar1.append(count)
# import matplotlib.pyplot as plt

# plt.plot(array,ar1,'g')
# # plt.plot(array,ar2,'b')
# plt.show()
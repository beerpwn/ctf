#!/usr/bin/python
#-*- coding:utf-8 -*-
import math
import sys
from Crypto.Util import number
from Crypto.PublicKey.RSA import construct
from Crypto.PublicKey import RSA
from colorama import Fore, Back, Style

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

# sito di rifermimento http://www.factordb.com/index.php

p = int(sys.argv[1])
q = int(sys.argv[2])
n = p*q
# phi(n) = (p-1)*(q-1) Euler Totient è il numero di tutti i numeri (minori di n)
# coprimi con n: essendo n composto da 2 soli fattori primi allora => phi(n) = phi(p*q) = phi(p)*phi(q)
y = (p-1)*(q-1)
e = 65537#113#
d = modinv(e,y)
print "[+] d: "+str(d)
enc = int(sys.argv[3])

test = (e * d) - 1
if test % y == 0:#per RSA vale => e*d-1=k*phi(n) ossia e*d deve essere congruo a 1 modulo phi(n)
	print( Fore.GREEN + "[+] test ==> e*d-1=k*phi(n) ok!")
if n%p!=0:
    print( Fore.RED + "[!] ERROR!! p non e' un fattore di n ==> (n%p != 0)")
    exit(0)
else:
    print( Fore.GREEN + "[+] test ==> (n%p == 0) ok!")

print Fore.BLUE
key_params = (long(n), long(e), long(d))
key = RSA.construct(key_params)
print key.exportKey()
print '\n[+] Message: ', key.decrypt(enc)

print Fore.YELLOW
m = pow(enc, d, n)
print "[+] Dec value of the message is: " +str(m)
print "[+] Hex value of the message is: ", str((hex)(m))
try:
    print "[+] ASCII text of the message is: ", str((hex)(m)[2:-1]).decode('hex')
except:
    print "[+] ASCII text of the message is: ", ("0"+str((hex)(m)[2:-1])).decode('hex')

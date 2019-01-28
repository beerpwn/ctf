 
We have a 32-bit ELF binary and libc is NOT provided:

<pre>
$ file leakless
leakless: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=168034ba2b6802df6058a4ceede506ffaf8dabb3, not strippeded
</pre>

Run the binary:
<pre>
$ ./leakless 
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Errore di segmentazione (core dump creato)
</pre>
and we get a segfault! :)

Also the binary seems dont use puts or printf, but if we analyze a bit we found:<br>
<pre>
$ rabin2 -s leakless | grep puts
004 0x000003f0 0x080483f0 GLOBAL   FUNC   16 imp.puts
</pre>

Quick reverse reveal that the function puts is used just in the handler function wich is called by the setup func that is (finally) called by main function.
<br>
Let's now analyze the protection that are enabled on this binary(assuming ASLR is active on the remote server):
<br>
<pre>
gef➤  checksec 
[+] checksec for 'leakless'
Canary                        : No
NX                            : Yes
PIE                           : No
Fortify                       : No
RelRO                         : Partial
</pre>
<br>

With that in mind we can start figure out our exploit.
Use the buffer overflow to override the ret addr and get control on eip, use <a href='https://en.wikipedia.org/wiki/Return-to-libc_attacks'>ret2libc</a> to leak some GOT addr and return into main func.
The leak payload will be like this <pre>[A*off][puts_plt][main_addr][some_GOT_addr]</pre>
After that we can serch for libc version. I used this site <a href='https://libc.blukat.me'>https://libc.blukat.me</a> to evaluate libc version.
<br>
Generate the final payload <pre>[A*off][system_libc][junk][/bin/sh]</pre> and send it.
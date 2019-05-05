### writeup by p4w@beerPWN team

# INS'HACK 2019 CTF
## gimme-your-shell PWN challnge

This is not the intended solution for this challenge since i used ROP to solve it.
We have a 64-bit binary and the libc of the remote server is NOT provided.
Let's start with a little bit of reverse on the binary.
As we can see from the image below the main() function will call the vuln() function.

![alt text](images/main.png)

The assembly of vuln() function show us that dangerous function 'gets()' will be used.

![alt text](images/vuln.png)

As we can see from the man page the gets(*s) function will read until \n or EOF, but there is no control on how many byte it will read and consequently write into *s.

![alt text](images/man_gets.png)

Reading the vuln function we can see that the argument for the gets function will be a variable located into the stack.
So what we expect from this is a stack-buffer overflow.
Let's verify this:

![alt text](images/segfault.png)

Segfault!
Let's also check for the protection on the binary
```
$ checksec ./weak
Canary                        : No
NX                            : No
PIE                           : No
Fortify                       : No
RelRO                         : No
```
As we can see the binary has no protection at all. So potentially we can also inject some shellcode into the stack/heap and jump on it, but instead of this i managed to do full ROP on this.
So what i did now was start to find some gadgets.
```
$ ROPgadget --binary ./weak --depth 50
```
the first gadget that i pick for this challenge is:
```
0x0000000000400637 : mov ebx, dword ptr [rsp + 8] ; mov rbp, qword ptr [rsp + 0x10] ; mov r12, qword ptr [rsp + 0x18] ; mov r13, qword ptr [rsp + 0x20] ; mov r14, qword ptr [rsp + 0x28] ; mov r15, qword ptr [rsp + 0x30] ; add rsp, 0x38 ; ret
```

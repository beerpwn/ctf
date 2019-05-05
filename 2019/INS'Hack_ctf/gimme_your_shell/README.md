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

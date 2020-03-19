## Angstrom CTF 2020
### pwn challenge 120 pti
### Author: p4w

We have a format string vuln.<br>
I used the fmt string to leak address of libc and one address of the stack. Form the stack addr. 
I calculated the offesst of the __saved ret__ then i ovewritten it with one_gadget.

<a href="./exp.py">Exploit</a> here

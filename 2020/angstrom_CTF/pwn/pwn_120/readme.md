## Angstrom CTF 2020
### pwn challenge 120 pti
### Author: p4w

We have a format string vuln.<br>
I used the fmt string to leak address of __libc__ and one address of the __stack__. From the leakaed stack address 
I calculated the offesst of the __saved ret__, then I ovewritten it with __one_gadget__.

<a href="./exp.py">Exploit</a> here.

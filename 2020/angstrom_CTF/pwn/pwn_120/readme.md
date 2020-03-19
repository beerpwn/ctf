## Angstrom CTF 2020
### pwn challenge 120 pti
### Author: p4w

* We have a format string vuln.<br>
* Use the fmt string to leak address of __libc__ and one address of the __stack__. 
* Calculating the offsett between the __leakaed stack address__ and the saved ret address
* ovewritten __ret address__ with __one_gadget__.

<a href="./exp.py">Exploit</a> here.

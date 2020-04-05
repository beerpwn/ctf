### Author: p4w

* binary analysis:
```
  $ file ./main
  main: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=bca3291bae283d68f245ce737825504c707a8751, for GNU/Linux 3.2.0, not stripped
```
* vulnerability:
We have a one byte off vulnerability affecting the stack. Basically we can override the last byte of the saved `Base Pointer` (EBP).
The overflow happen inside the `check_status` function which is called by the `main` function.
So that we have two `leave, ret` instruction after the overflow.
This will lead to a a <b>stack pivot</b>.

* exploit: pivot the stack upper, we populate the upper part with a `ret sladge` gadgets to increase the chanche, leak address and the restart execution to `call system('/bin/sh')`.

Exploit <a href="./x.py">here</a>.

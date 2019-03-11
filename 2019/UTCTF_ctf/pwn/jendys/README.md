### writeup by sk4 @ beerPWN sec-team

# UTCTF 2019 CTF
## Jendy's pwn level 1400 pti

<a href="https://exploitnetworking.com/en/security-en/jendys">Here</a> there is the original writeup. For test the exploit, setup an enviroment with the libc-2.23.so, for example an Ubuntu 16.04. Download the repository in enviroment:

docker run --name ubuntu1604 ubuntu:xenial

<pre> git clone https://github.com/beerpwn/ctf.git </pre>

Move in directory:

<pre> cd ctf/2019/UTCTF_ctf/pwn/jendys </pre>

And run the <a href="https://github.com/beerpwn/ctf/blob/master/2019/UTCTF_ctf/pwn/jendys/exploit.py">exploit.py</a>:

<pre> python exploit.py </pre>

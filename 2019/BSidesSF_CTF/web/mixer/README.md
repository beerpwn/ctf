### writeup by p4w @ beerpwn sec-team

# BSidesSF 2019 CTF
## Mixer crypto-web level 150pti

Let's start login with some creds.

![alt text](screen/login.png)

As we cen see the response include a cookie "user" witch is the one we need to focus on.
Just use this cookie and see what we get back

![alt text](screen/normal_login.png)

So, my guess is:
the cookie is encrypted with AES ECB mode, and if it is that's BAD!!! ;)
Since i'm not a crypt guy i'll demand to information about AES and ECB mode encryption to google.
Here you can just give an idea about how that works <link href="https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation">

Let's start modify user cookie at random position by just flipping one byte, in order to verify if the assumption is correct.

![alt text](screen/flip_one_byte.png)

As we can see the guess about AES ECB was probably correct, by flipping one byte we change the encrypted payload that now is no more a valid json.
Also we can see that the cookie is something like AES(json), where the json payload is:
### {"first_name":"paw","last_name":"paww","is_admin":0}

To get the flag we now need to modify the json payload to be something like this:
### {"first_name":"paw","last_name":"paww","is_admin":1}

First approach that i try was to just fuzz on the byte witch is responsible to encode the "0", but that doesn't work propelly.

So i start thinking a little bit ddeper on this and it comes in my mind that if i can control an entire block of the encoded cookie with something that will be equivalent to 1 and then i can reply the entire block between the <pre>"is_admin":</pre> and the <pre>0</pre>
So what about 1.00000000000000 ?
Note that length of 1.00000000000000 it's 16 byte.
The json payload will become:
{"first_name":"A1.000000000000000","last_name":"paww","is_admin":1.000000000000000}
and this will be also a valid json as we can see here:

![alt text](screen/json_check.png)

If we can obtain this situation then we should become admin and get the flag.

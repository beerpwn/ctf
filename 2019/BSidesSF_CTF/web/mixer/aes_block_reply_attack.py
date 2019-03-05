##### exploit by p4w #####

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = "https://mixer-f3834380.challenges.bsidessf.net"
action="""?action=login&first_name=A1.00000000000000&last_name=paww"""
r = requests.get(url+action, verify=False, allow_redirects=False)
for c in r.cookies:
    print(c.name, c.value)
    if c.name == "user":
        c.value = c.value[:-32] + c.value[32:64] + c.value[-32:]

resp = requests.get(url, cookies = r.cookies, verify=False, allow_redirects=False)

print resp.text

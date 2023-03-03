import urllib.parse
url = "http://abc.com:80/engineering/computer-science.html"
tpl = urllib.parse.urlparse(url)
print(tpl)

print(tpl.scheme)
print(tpl.port)
print(tpl.netloc)
print(tpl.params)
print(tpl.geturl())

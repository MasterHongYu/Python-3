import urllib.request as request
src = ""
with request.urlopen() as respone:
    data = respone.read()
print(data)

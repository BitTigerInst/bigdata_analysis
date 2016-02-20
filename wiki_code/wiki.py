import requests
import re
import random

url =  "https://en.wikipedia.org/wiki/Google"
req = requests.get(url)

#with open("sourcepage1.txt","w") as f:
	#f.write(req.text.encode('utf-8'))
	#f.write(req.content)
#matches = re.findall(r'href=[\'"]?([^\'" >#]+)',req.text)
matches = re.findall(r'href="/wiki/[0-9a-zA-Z]*"',req.text)
links = random.sample(matches,100)
num = 1
prefix = "https://en.wikipedia.org"
for link in links:
	url = prefix + link.lstrip('href="').rstrip('"')
	req = requests.get(url)
	filename = "wikiset/sourcepage%d.txt" % num
	num+=1
	with open(filename,"w") as f:
		f.write(req.text.encode('utf-8'))


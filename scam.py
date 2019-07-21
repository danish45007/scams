import os
import requests
import random
import string
import json
char = string.ascii_letters + string.digits + '!@#$^&*()'

random.seed = (os.urandom(1024))

url = 'https://www.toysloy.com/'

names = json.loads(open('names.json').read())

for name in names:
	name_extra = ''.join(random.choice(string.digits))

	username = name.lower() + name_extra + '@yahoo.com'
	password = ''.join(random.choice(char) for i in range(8))

	requests.post(url, allow_redirects=False, data={
		'dgsgdjcksjdokkk': username,
		'rararara': password 
    })



	print('sending username %s and password %s' % (username, password))

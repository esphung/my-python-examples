# -*- coding: utf-8 -*-
# @Author: homeuser
# @Date:   2017-11-29 10:16:53
# @Last Modified 2017-12-06
# @Last Modified time: 2017-12-06 01:55:00

import urllib.request
from bs4 import BeautifulSoup
import re
import sys

data = ""

#moores law
url = 'https://en.wikipedia.org/wiki/Quadratic_probing'

result = urllib.request.urlopen(url).read()
soup = BeautifulSoup(result, 'html.parser')
try:
	print(soup.p.text)
	data = soup.p.text
except Exception:
	data = (re.sub(r'[^\x00-\x7F]+','',soup.p.text))
finally:
	print(soup.title.text)

''' simple file writing '''
file = '{}.txt'.format(soup.title.text.replace(' ',''))
f = open(file,mode='w')
f.write(data)
f.write("\n")
f.truncate()
f.close()

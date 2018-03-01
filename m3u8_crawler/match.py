import requests
import re

r = requests.get('http://widestream.io/embed-9899')

findall = re.findall(r'file:\"([^\"]+m3u8[^\"]+)\"', r.text)
#findall = re.findall(r'file:.+', r.text)
print(findall)

search = re.search(r'file:.+', r.text)
print(search.group())

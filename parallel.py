#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

from requests_futures.sessions import FuturesSession
from concurrent.futures import wait
import re

session = FuturesSession(max_workers=100)

futures = [
   session.get('http://widestream.io/embed-9' + str(num))
   for num in range(100, 1000)
]
done, incomplete = wait(futures)

m3u8 = []
for r in futures:
   match = re.search(r'file:\"([^\"]+widestream[^\"]+m3u8[^\"]+)\"', r.result().text)
   if(match):
      m3u8.append(match.group(1))


futures = [
   session.head(src)
   for src in m3u8
]
done, incomplete = wait(futures)

i = 0
for r in futures:
   if(r.result().ok):
      print(m3u8[i])
   i += 1
      

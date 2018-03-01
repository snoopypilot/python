#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

from requests_futures.sessions import FuturesSession
from concurrent.futures import wait
import re
import os

session = FuturesSession(max_workers=100)

# get html sources
futures = [
   session.get('http://widestream.io/embed-' + str(num))
   for num in range(9000, 10000)
]
done, incomplete = wait(futures)

# extract m3u8 sources
m3u8 = []
for r in futures:
   match = re.search(r'file:\"([^\"]+widestream[^\"]+m3u8[^\"]+)\"', r.result().text)
   if(match):
      m3u8.append(match.group(1))

# check video source availability
futures = [
   session.head(src)
   for src in m3u8
]
done, incomplete = wait(futures)

# output all working live streams
it = iter(m3u8)
count = 0

for r in futures:
   src = next(it)
   if(r.result().ok):
      os.system('open -a Safari ' + src)
      count += 1

print(str(count) + ' live streams are extracted')

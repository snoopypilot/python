#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

from requests_futures.sessions import FuturesSession
from concurrent.futures import wait
import requests
import re
import os
import sys

if(len(sys.argv)>1):
   n = int(sys.argv[1])
   if(len(sys.argv)>2):
      p = True
   else:
      p = False
else:
   n = 9
   p = False


session = FuturesSession(max_workers=100)

def main(sess, resp):
   match = re.search(r'file:\"([^\"]+m3u8[^\"]+)\"', resp.text)
   if(match):
      src = match.group(1)
      #print(src)
      r = requests.get(src)
      if(r.status_code == requests.codes.ok and r.headers['Content-Type'] < 'applications'):
         if(p):
            print(src)
         else:
            os.system('open -a Safari ' + src)

# get html sources
futures = [
   session.get('http://widestream.io/embed-' + str(num), background_callback=main)
   for num in range(1000*n, 1000*(n+1))
]
done, incomplete = wait(futures)

#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import requests
import asyncio
import re
import os

async def crawl(s, e):
   loop = asyncio.get_event_loop()
   m3u8 = []
   futures = [
      loop.run_in_executor(None, requests.get, 'http://widestream.io/embed-98' + str(num))
      for num in range(s, e)
   ]
   for r in await asyncio.gather(*futures):
      m3u8.extend(re.findall(r'file:\"([^\"]+m3u8[^\"]+)\"', r.text))
   return m3u8
   



async def check(m3u8):
   loop = asyncio.get_event_loop()
   futures = [
      loop.run_in_executor(None, requests.head, src)
      for src in m3u8
   ]
   for r in await asyncio.gather(*futures):
      if(r.ok):
         print(r)





loop = asyncio.get_event_loop()
m3u8 = loop.run_until_complete(crawl(10, 100))
#print(m3u8)
#loop.run_until_complete(check(m3u8))
for src in m3u8:
   try:
      r = requests.head(src)
      if(r.ok):
         print(src)
   except Exception as e:
      print('----------------')
      print(src)
      print(e)
      print('----------------')

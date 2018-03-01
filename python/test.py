#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import asyncio
from aiohttp import ClientSession
import requests
import re
import os

m3u8 = []

async def fetch(url, session):
   async with session.get(url) as response:
      return await response.text()


async def run(s, e, m3u8):
   tasks = []
   links = []

   async with ClientSession() as session:
      for i in range(s, e):
         url = 'http://widestream.io/embed-98' + str(i)
         task = asyncio.ensure_future(fetch(url, session))
         tasks.append(task)

      pages = await asyncio.gather(*tasks)
      m3u8.extend(re.findall(r'file:\"([^\"]+m3u8[^\"]+)\"', str(pages)))
      #print(m3u8)


async def check(url, session):
   async with session.head(url) as response:
      return await response.text()


async def get_m3u8(links):
   tasks = []

   async with ClientSession() as session:
      for url in links:
         task = asyncio.ensure_future(check(url, session))
         tasks.append(task)

      ok_list = await asyncio.gather(*tasks)
      print(ok_list)


"""
      if(m3u8):
         for link in m3u8:
            x, src, y = link.split('"')
            links.append([src])
            video = requests.head(src)
            if(video.ok):
               print(src)
            else:
               print('X')
"""
loop = asyncio.get_event_loop()
future = asyncio.ensure_future(run(80, 100, m3u8))
loop.run_until_complete(future)

#print(m3u8)
loop = asyncio.get_event_loop()
future = asyncio.ensure_future(get_m3u8(m3u8))
loop.run_until_complete(future)


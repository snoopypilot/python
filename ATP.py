#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import requests
import re
import os

for i in range(80, 100):
   page = requests.get('http://widestream.io/embed-98' + str(i))
   print(i, end=' ')
   #print(r.json)
   m3u8 = re.search(r'file:.+', page.text)
   if(m3u8):
      x, src, y = m3u8.group(0).split('"')
      #print('[' + str(i) + '] ' + src)
      video = requests.head(src)
      #print(video.status_code)
      if(video.ok):
         print(src)
         #print('O')
         #os.system('open -a Safari ' + src)
      else:
         print('X')
   else:
      print('X') 

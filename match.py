#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import random

players = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0}

def next_up(players):
   eligible = {}
   for k, v in players.items():
      if(len(eligible)):
         if(v <= min_v):
            if(v < min_v):
               eligible.clear()
               min_v = v
            eligible[k] = v
      else:
         min_v = v
         eligible[k] = v
   #print(eligible)
   match = random.sample(eligible.keys(), min(len(eligible), 4))
   if(len(match)<4):
      match.extend(random.sample(players.keys() - match, 4 - len(match)))
   for p in match:
      players[p] += 1
   #print(players)
   return print(match) 

def lcm_4(num):
   mod = num % 4
   if(mod == 0):
      return num/4
   elif(mod == 2):
      return num/2
   else:
      return num

for i in range(lcm_4(len(players))):
   print("%2d" % (i+1), end=' ')
   next_up(players)

#print(players)


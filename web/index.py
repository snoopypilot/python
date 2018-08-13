from flask import Flask
from flask import render_template
from flask import request
import random

#app = Flask(__name__, static_url_path='/static')
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/match', methods=['POST'])
def match():
   names = request.form.getlist('name')
   players = {name: 0 for name in names if(name)}
   matches = []
   #print(players)
   for i in range(20):
      matches.append(next_up(players))
   return render_template('index.html', matches=matches)


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
   return match 

def lcm_4(num):
   mod = num % 4
   if(mod == 0):
      return num/4
   elif(mod == 2):
      return num/2
   else:
      return num



if __name__ == '__main__':
   app.run(host='127.0.0.1', debug=True)

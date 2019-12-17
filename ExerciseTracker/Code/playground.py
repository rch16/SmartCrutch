"""from flask import Flask, jsonify
from threading import Thread

app = Flask('')
@app.route('/')
def home():
	return  "I'm alive"

@app.route('/api/add', methods=['GET'])
def add():
	return jsonify({"2 + 2":  2 + 2})

def run():
	app.run(host='0.0.0.0',port=7000)

t = Thread(target=run)
t.start()"""

print("Win")
import pandas as pd
msg = [[1.5824941841576496, 0.02467203825922914, 0.5682399147168499], [1.6718440039887672, 0.023983586628506078, 0.3589849478433582], [1.5958826838779216, 0.29248178363725114, 0.7227166111410417], [1.70195318059245, 0.38841952066869756, 0.536478428551051], [1.6890551209164255, 0.17335939943748901, 0.3578125518577004], [1.6601252496660541, 0.02349492473240662, 0.1246910074276997], [1.6546328870610947, -0.1253922223657796, 0.36015734382901593], [1.6268903779813146, -0.34480289250849044, 0.4852236688812772], [1.521927923247053, -0.26929616746090235, 0.67939846238917]]


import json

parts = ["head", "neck", "left_hand", "left_elbow", "left_shoulder", "torso", "right_shoulder", "right_elbow", "right_hand"]

coordinates = ["x", "y", "z"]


def to_json(msg):
  parts = ["head", "neck", "left_hand", "left_elbow", "left_shoulder", "torso", "right_shoulder", "right_elbow", "right_hand"]

  coordinates = ["x", "y", "z"]

  result = [{parts[i]: {coordinates[j]: msg[i][j] for j in range(len(coordinates))} for i in range(len(parts))}]

  result = json.dumps(result, indent=4)

  result = pd.read_json(result)

  return result




def merge_pandas(panda1, panda2):
  #data = [panda1, panda2]
  panda1 = panda1.append(panda2, ignore_index=True, sort=False)

  return panda1

result = to_json(msg)
print(result)
res = merge_pandas(result,result)
print(res)
res = merge_pandas(res,result)
print(res)
print(res.loc[0]["torso"]['x'])

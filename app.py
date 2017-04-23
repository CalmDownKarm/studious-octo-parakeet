from flask import Flask, jsonify, request,abort, make_response
from upcoming_fights import upcoming_fights as u
import json
app = Flask(__name__)
events = ['one','two','three']


with open('Data/winners.json') as json_data:
  d = json.load(json_data)

@app.route('/')
def index():
  return "STILL HERE!"

@app.route('/api/v1.0/getprediction/<int:task_id>', methods=['GET'])
def get_fight_by_id(fight_id):
  fight = [fight for fight in u if fight['id']==fight_id]
  if(len(fight)==0):
    abort(404)
  else:
    return jsonify({'fight':fight[0]})

@app.route('/api/v1.0/getprediction/<title>', methods=['GET'])
def get_fight_by_title(title):
  fight = [fight for fight in u if fight['title']==title]
  if(len(fight)==0):
    abort(404)
  else:
    return jsonify({'fight':fight[0]})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'STATUS': 'NOT OK', 'reason':'404'}), 404)

if __name__ == '__main__':
  app.run(debug=True)

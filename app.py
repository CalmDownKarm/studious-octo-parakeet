from flask import Flask, jsonify, request,abort, make_response
import json
app = Flask(__name__)
events = ['one','two','three']
tasks = [
    {
        'id': 'lel1',
        'title': u'Whittaker vs Souza',
        'prediction': u'Souza',
        'done': False
    },
    {
        'id': 'lel2',
        'title': u'Mcgregor vs Mayweather',
        'description': u'Mcgregor',
        'done': False
    }
]

with open('Data/winners.json') as json_data:
  d = json.load(json_data)
  print d

@app.route('/')
def index():
  return "STILL HERE!"

@app.route('/api/v1.0/getprediction/<task_id>', methods=['GET'])
def get_tasks(task_id):
  task = [task for task in tasks if task['id']==task_id]
  if(len(task)==0):
    abort(404)
  else:
    return jsonify({'task':task[0]})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'STATUS': 'NOT OK', 'reason':'404'}), 404)

if __name__ == '__main__':
  app.run(debug=True)

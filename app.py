from flask import Flask, jsonify, request,abort

app = Flask(__name__)
events = ['one','two','three']
tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]
@app.route('/')
def index():
  return "STILL HERE!"

@app.route('/api/v1.0/gettask', methods=['GET'])
def get_tasks():
  fightid = request.args.get('fightid')
  return jsonify({'tasks': tasks})

if __name__ == '__main__':
  app.run(debug=True)

from flask import Flask,jsonify,request
app=Flask(__name__)
tasks=[{
    'id': 1,
    'Name': u'Raju',
    'Contact': u'9987644456',
    'done': False
    },
    {
    'id': 2,
    'Name': u'Rahul',
    'Contact': u'9876543222',
    'done': False
    }]
@app.route("/")
def hello_world():
    return "Hello World!"
@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please provide the data"
        },400)
    task={
        'id': tasks[-1]['id']+1,
        'title': request.json['Name'],
        'description': request.json.get('Contact',""),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        'status': 'success',
        'message': 'Task added successfully'
    })
@app.route("/get-data")
def get_task():
    return jsonify({
        'data': tasks
    })
if(__name__=="__main__"):
    app.run(debug=True)
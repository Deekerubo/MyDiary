from flask import Flask
from flask import jsonify, request
from app.models import Models

app = Flask(__name__)

# create an instance of models class
models = Models()
@app.route('/api/v1/', methods=["GET"])
def index():
    message = {"My diary": {
                    "Message":"Welcome to my diary"
                }
              }

    res = {"Message": message}
    return jsonify(res), 200

@app.route('/api/v1/entries', methods=["POST"])
def adding():
    
    data = request.get_json()
    title = data['title']
    content = data['content']
    models.add(title, content)
    return jsonify({"title":title, "content":content}), 201

@app.route('/api/v1/entries' ,methods=["GET"])
def get_entries():
    return jsonify(models.all_entries()), 200

@app.route('/api/v1/entries/<int:entryId>')
def get_one_entry(entryId):
    entries_in_model = models.all_entries()
    for i in entries_in_model:
        if i['id'] == entryId:
            return jsonify(i)

@app.route('/api/v1/entries/<int:entryId>', methods=['PUT'])
def edit_one_entry(entryId):
    entries_in_model = models.all_entries()
    for i in entries_in_model:
        if i['id'] == entryId:
            data = request.get_json()
            title = data['title']
            content = data['content']
            i['title'] = title
            i['content'] = content
            return jsonify({"title":title, "content":content})
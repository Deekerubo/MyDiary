from flask_api import FlaskAPI
from flask import request, jsonify
from app.models import Models

app = FlaskAPI(__name__)
 
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
    
    # data = request.get_json()
    title = request.data.get('title', "")
    content = request.data.get('content', "")
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
            title = request.data.get('title', "")
            content = request.data.get('content', "")
            i['title'] = title
            i['content'] = content
            return jsonify({"title":title, "content":content}), 201
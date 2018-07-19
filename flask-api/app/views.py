from flask import Flask
from app import app
from flask import jsonify, request
from app.models import Models

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
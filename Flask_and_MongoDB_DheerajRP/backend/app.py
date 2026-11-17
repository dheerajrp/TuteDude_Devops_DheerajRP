import os

from dotenv import load_dotenv
from flask import Flask, request
from pymongo import MongoClient

backend = Flask(__name__)

load_dotenv()
client = MongoClient(os.getenv('MONGO_URI'))

db = client.get_database('devops_db')
collection = db.get_collection('devops_coll')

@backend.route('/')
def hello():
    return "Hello, World!"

@backend.route('/view')
def view():
    data = list(collection.find())
    for item in data:
        del item['_id']
    return data

if __name__ == '__main__':
    backend.run(port=9000,debug=True)
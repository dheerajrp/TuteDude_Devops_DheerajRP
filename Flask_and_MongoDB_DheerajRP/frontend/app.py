import os

from dotenv import load_dotenv
from flask import Flask, render_template, request
from pymongo import MongoClient

frontend = Flask(__name__)

load_dotenv()
client = MongoClient(os.getenv('MONGO_URI'))

db = client.get_database('devops_db')
collection = db.get_collection('devops_coll')

@frontend.route('/api')
def load_form():
    return render_template('index.html')

@frontend.route('/submit', methods=['POST'])
def submit():
    try:
        data = dict(request.form)
        collection.insert_one(data)
        return "Data submitted successfully!"
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    frontend.run(port=5000, debug=True)
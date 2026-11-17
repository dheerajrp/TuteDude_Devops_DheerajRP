
from flask import Flask, jsonify
import json
import os

json_api = Flask(__name__)

@json_api.route('/api', methods=['GET'])
def get_data():

    file_path = os.path.join(
        os.path.dirname(__file__),
        'data.json'
    )

    try:
        with open(file_path, 'r') as file:
            data = json.load(file)

        return jsonify(data), 200

    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404

    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON format"}), 500


if __name__ == '__main__':
    json_api.run(debug=True)

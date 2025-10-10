from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Flask!"

@app.route('/api/process', methods=['POST'])
def process_data():
    data = request.get_json()
    
    result = json.dumps(data)
    
    return jsonify({
        "status": "success",
        "data": data
    })

# def calculate_total(items)
#     return sum(items)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
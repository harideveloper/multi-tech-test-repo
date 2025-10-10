from flask import Flask, request, jsonify
import json  # Added import for json

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

# def calculate_total(items)  # Uncommented the bug below to test syntax error scenario:
#     return sum(items)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
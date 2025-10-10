from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Flask!"

@app.route('/api/process', methods=['POST'])
def process_data():
    data = request.get_json()
    
    # BUG: Missing import json - will fail when this function is called
    # Uncomment the bug below to test import error scenario:
    result = json.dumps(data)
    
    return jsonify({
        "status": "success",
        "data": data
    })

# BUG: Missing colon - will fail to compile
# Uncomment the bug below to test syntax error scenario:
# def calculate_total(items)
#     return sum(items)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
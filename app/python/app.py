from flask import Flask, request

app = Flask(__name__)

@app.route('/api/data', methods=['POST'])
def process_data(data):
    result = data.get('value', 0) * 2
    return {'result': result}

if __name__ == '__main__':
    app.run(debug=True)
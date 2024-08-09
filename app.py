from flask import Flask, request, jsonify
from flask_cors import CORS
from llama_utils import generate_response  # Import the function

app = Flask(__name__)
CORS(app)  # Enable CORS to allow cross-origin requests

@app.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.json
        prompt = data.get('prompt', '')
        response = generate_response(prompt)  # Use the imported function
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=8000)  # Change port to 8000

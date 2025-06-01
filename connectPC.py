from flask import Flask, request, jsonify
import lmstudio as lms

app = Flask(__name__)

@app.route('/respond', methods=['POST'])
def respond():
    prompt = request.json.get('prompt', '')
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    print("Initializing client...")
    with lms.Client() as client:
        print("Client initialized. Loading model...")
        model = client.llm.model("qwen_qwen3-0.6b@q6_k_l")  # Replace with your model
        print("Model loaded. Sending prompt...")
        result = model.respond(prompt)
        print("Response received.")
        return jsonify({"response": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Expose the server on port 5000
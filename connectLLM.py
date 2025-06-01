# import lmstudio as lms

# print("Initializing client...")
# with lms.Client() as client:
#     print("Client initialized. Loading model...")
#     model = client.llm.model("qwen_qwen3-0.6b@q6_k_l")
#     print("Model loaded. Sending prompt...")
#     result = model.respond("What is the meaning of life?")
#     print("Response received:")
#     print(result)


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
        model = client.llm.model("llama-3.2-1b-instruct")  # Replace with your model
        print("Model loaded. Sending prompt...")
        result = model.respond(prompt)
        print("Response received.")

        # Ensure the result is JSON serializable
        if isinstance(result, dict) or isinstance(result, list):
            return jsonify({"response": result})
        else:
            return jsonify({"response": str(result)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # Expose the server on port 5000
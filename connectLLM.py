import lmstudio as lms

print("Initializing client...")
with lms.Client() as client:
    print("Client initialized. Loading model...")
    model = client.llm.model("qwen_qwen3-0.6b@q6_k_l")
    print("Model loaded. Sending prompt...")
    result = model.respond("What is the meaning of life?")
    print("Response received:")
    print(result)
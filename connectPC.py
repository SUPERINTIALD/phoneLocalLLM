import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def get_llm_response(prompt, server_ip):
    url = f"http://{server_ip}:port/respond"
    headers = {"Content-Type": "application/json"}
    data = {"prompt": prompt}

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        return response.json().get("response", "No response received.")
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    server_ip = os.getenv("SERVER_IP") 
    prompt = "What is the meaning of life?"
    print("Sending prompt to server...")
    result = get_llm_response(prompt, server_ip)
    print("Response from server:")
    print(result)

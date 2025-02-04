from flask import Flask, render_template, request,jsonify
import pandas as pd
import os
import google.generativeai as genai
genai.configure(api_key="AIzaSyABj9Y_6aQvXEquKA89IYWdjzl1ytNdnrI")  # Replace with your actual key

model = genai.GenerativeModel("gemini-1.5-flash")
app = Flask(__name__)
def send_messege(message):
    history=[
        {"role": "user", "parts": "Hello"},
    ]
    chat=model.start_chat(history=history)
    response=chat.send_message(message)
    history.append({"role":"model", "parts":response.text})
    return response.text,history
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    response ,history= send_messege(user_message)
    return jsonify({"message": response,"history":history})
if __name__ == '__main__':
    app.run(debug=True)
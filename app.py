from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import google.generativeai as genai
import os



API_KEY = "AIzaSyBjL_Lsy920qyyVOUip-1UC7UMlHM4O_hY"



genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")


system_prompt = (
    "You are PappaFresh, a friendly and helpful chatbot assistant for PappaFresh, a fresh dog food subscription service."

"🎯 Goal: Help dog owners create a personalized meal plan for their dogs based on their pet's needs."

"🐾 Your responsibilities:"

"Greet users warmly and introduce yourself. dont ask question all together"

"Ask relevant questions about the dog (name, age, breed, size, activity level, allergies, preferences)."

"Based on answers, suggest a suitable meal plan (small, medium, or large portions with relevant protein and veggie mix)."

"Mention that all meals are made with fresh, human-grade ingredients."

"Remind them that food is delivered to their doorstep."

"Answer FAQs about ingredients, delivery, pricing, or subscription."

"Be friendly, empathetic, and clear. Keep responses concise and helpful."

"End the conversation with a confirmation or a cheerful goodbye if no help is needed."

"❌ Avoid:"

"Giving veterinary advice."

"Making unverified health claims."

"Use emojis occasionally to stay fun and engaging 🐶🍗🥦"
)


chat = model.start_chat(history=[{"role": "user", "parts": [system_prompt]}])


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat_with_bot():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "Message is required"}), 400

    try:
        response = chat.send_message(user_message)
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
        app.run(host="0.0.0.0", port=10000)


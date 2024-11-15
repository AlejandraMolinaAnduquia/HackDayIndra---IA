from flask import Flask, render_template, request
from chain.chatbot import initialize_chatbot

app = Flask(__name__)
bot = initialize_chatbot()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = bot.ask(user_input)
    return {"response": response}

if __name__ == "__main__":
    app.run(debug=True)

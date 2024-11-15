from flask import Flask
from chain.chatbot import initialize_chatbot

app = Flask(__name__)
bot = initialize_chatbot()

@app.route("/")
def home():
    return "¡Bot inicializado correctamente!"

if __name__ == "__main__":
    app.run()

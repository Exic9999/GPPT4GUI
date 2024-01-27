
from typing import Tuple
from flask import Flask, render_template, request
import openai
import os
  
app = Flask(__name__)

def ask_chat_gpt(question: str) -> Tuple[str,bool]:
    # will blow up if no key is provided
    try:
        openai.api_key = os.environ['CHAT_GPT_API_KEY']
        response = openai.ChatCompletion.create( # type: ignore
            model="gpt-4-1106-preview",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question}
            ],
            max_tokens=4096
        )
        return (response['choices'][0]['message']['content'], True) # type: ignore
    except Exception as e:
        return ("Error: " + str(e), False)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=['POST'])
def ask():
    question = request.form["question"]
    (response, success) = ask_chat_gpt(question)
    if success:
        return render_template("response.html", question=question, answer=response)
    else:
        return render_template("response.html", question=question, answer=response), 500

if __name__ == "__main__":
    app.run(debug=False)

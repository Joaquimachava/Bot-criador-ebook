from flask import Flask, request, render_template
import openai
import os

app = Flask(__name__)

# Chave da API OpenAI
openai.api_key = "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"

@app.route("/", methods=["GET", "POST"])
def index():
    ebook = ""
    if request.method == "POST":
        tema = request.form["tema"]
        prompt = f"Crie um e-book detalhado com 5 capítulos sobre o tema: {tema}"
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )
        ebook = response.choices[0].message.content
    return render_template("index.html", ebook=ebook)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

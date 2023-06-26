from flask import Flask, render_template
from flask import request
import requests
from bs4 import BeautifulSoup

app= Flask(__name__)
entries = []

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/value', methods =['POST'])
def word_count():
    website_url = request.form.get("url")
    response = requests.get(website_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text()
    words = text.split()
    word_count = len(words)
    entries.append({'web': website_url, 'count': word_count})
    return render_template('word_count.html',entries=entries)
if __name__ == '__main__':
    app.run()

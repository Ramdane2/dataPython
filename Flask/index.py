from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world !"

@app.route('/books')
def books():
    listBook = ''
    with open('./books.json') as json_file:
        data = json.load(json_file)
        for p in data:
            listBook += 'Titre: ' + p['title'] + '\n'
    return listBook


if __name__ == "__main__":
    app.run()

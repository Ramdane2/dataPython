import json

def books():
    with open('./books.json') as json_file:
        data = json.load(json_file)
        for p in data:
            print('Titre: ' + p['title'])
            print('')

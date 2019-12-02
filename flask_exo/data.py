import json

data = {
    'Quarts': [
        'up', 'charm', 'strange'
    ],
    'Leitons': [
        'hyh', 'hbub', 'hubu'
    ],
    'Truc': "doub"
}
with open('data.json', 'w') as f:
    json.dump(data, f)

with open('data.json', 'r') as f:
    loaded_data = json.load(f)

print(loaded_data)
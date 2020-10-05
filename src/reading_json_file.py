import json

with open('../data/json/response_deputados.json', encoding='utf-8') as json_file:
    data = json.load(json_file)

    for p in data['dados']:
        print(p)

#    for p in data['dados']:
#        print('Nome: ' + p['nome'])
#        print('Partido: ' + p['siglaPartido'])
#        print('')

#    for line in json_file:
#        print(line)

import json

with open('data1.json') as data_file:    
    data = json.load(data_file)
print(data)
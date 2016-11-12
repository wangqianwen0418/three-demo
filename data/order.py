import json
with open("./data/newdata.json" ) as json_data:
    data = json.load(json_data)
nodes=data['nodes']
nodeRef={}

for uid in nodes:
    value=nodes[uid]
    print(uid)
    item={}
    item["x"]=value['x']
    item["y"]=value['y']
    item["z"]=value['z']
    item["degree"]=value['degree']
    item["depth"]=value['depth']
    item["timestamp"]=value['timestamp']
    nodeRef[uid]=item;


with open('./data/nodeRef.json', 'w') as outfile:
    json.dump(nodeRef, outfile)
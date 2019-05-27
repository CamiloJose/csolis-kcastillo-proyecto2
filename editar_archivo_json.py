import json
 
##json_data = '{"name": "Brian", "city": "Seattle"}'
##python_obj = json.loads(json_data)
##print (python_obj["name"])
##print (python_obj["city"])
        
data = {
    "Users": {
        "Name": [
            "red",
            "blue"
            ]
        },
    
    "Scores": [
        0
    ],
}

with open ("Users.json", "r") as fh:
    json_str = fh.read()
    json_value = json.loads(json_str)
    print(type(json_value))
    print(json_value["Users"])


with open ("Users.json", "w") as fh:
    fh.write(json.dumps(data))
    fh.write(json.dumps(data, indent=4))
    #json.dumps(data)
    #json.dumps(data, indent=4)

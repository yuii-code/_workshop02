import json

#a Python object (dict):
python_dict = {
    "name": "Yui & o",
    "age : 21",
    "city" : "Bangkok"
}

#convert into JSON:
json_string = json.dumps(python_dict)

#the result is a JSON string:
print(json_string)

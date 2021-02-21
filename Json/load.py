import json
#some JSON:
json_string = '{ "name" : "Yui & O", "age":26, "city" : "Bangkok"}'

#parse X:
python_dict = json.loads(json_string)

#the result is a Python dictionaty:
print(python_dict["name"])
print(python_dict["age"])
print(python_dict["city"])
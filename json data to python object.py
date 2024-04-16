# if we have JSON string, then we can parse it using json.loads() method

import json

#some json
j = '{"name":"Avishek", "age":21,"Faculty":"BCT"}' # if we use [] then json file is converted to list
print(type(j))

#parse j
l = json.loads(j)   #after loading json file is converted to dictionary
print(l)
print(type(l))
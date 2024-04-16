import json
j = {
    'name':'Avishek',
    'age':21,
    'Faculty':'BCT'
    }
d=json.dumps(j)
print(d)
print(type(d))  # json are string type
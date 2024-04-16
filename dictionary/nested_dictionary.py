# dictionary under dictionary seprated by comma

student ={
    'ram':{'roll':78,'faculty':'BCT','phone':894},    
    'shyam':{'roll':89,'faculty':'BCE','phone':873},   
    'hari':{'roll':93,'faculty':'BME','phone':234}    
}
print(student)  # printing whole dictionary
print(student['ram']) # prints whole row of ram
print(student['ram']['faculty']) # prints only the faculty of ram

# updating the value of nested dictionary
student['ram']['roll'] = 100
for k,v in student.items():
    print(k,v) # prints whole row under dictionary(student)
    print(k,v['roll'],v['faculty'],v['phone']) # prints only the values of given keys

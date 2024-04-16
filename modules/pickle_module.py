# pickle module implements fundamental but powerful algorithm for serializing(store) and deseriaalizing(read) a python object structure

#storing data with pickle
# We can store following data types inside pickle

'''
    booleans,integer, float, complex number, (normal and unicode)strings,Tuple, list,
    set and dictionary

'''

# dump()--> To serializes the data and write into file
# load()--> To deserializes the data and read from file


import pickle
l = ['Avishek','Boss','Apple','onion']

new_file =open("write_file.txt","wb")   # wb means writing in binary mode
pickle.dump(l,new_file) # Storing the data into new file
new_file.close()

file = open("write_file.txt","rb")  # rb means reading in binary mode
f=pickle.load(file)
print(f)


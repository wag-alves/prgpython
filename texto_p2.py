import pickle

x = open('datafile.txt', 'rb')
y = pickle.load(x)
print(y)

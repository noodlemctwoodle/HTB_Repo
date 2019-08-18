### To run type python LongBottom.py ###

import pickle

# Used for opening the string
x = open ('/root/Downloads/donotshare')
# Load the file
e = pickle.load(x)

outstr = ''
# Read every line
for line in e: 
    for char,n in line:
        outstr += char*n
    outstr =+ '\n'
print outstr
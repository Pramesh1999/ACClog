import os
location = '/Users/Pramesh/Downloads'
for filename in os.listdir(location):
    if filename == 'access_log':
       f  = open(os.path.join(location, 'access_log'), "r")
d = {}
for line in f:
    s =""
    s = line[line.find("]") + 2:]
    if(len(s.split(" "))>= 4):
        err = s.split(" ")[3]
        if err in d.keys():
            d[err]+=1
        else:
            d[err]=1

list_err = list(d.keys())
list_err.sort()

for errcode in list_err:
    print("status code %s -> count %d"%(errcode,int(d[errcode])))


data = open("data.txt").read().split(",")

count = 0

def hash(i):
    c = 0
    for j in i:
        c=((c+ord(j))*17) % 256
    return c

box = [[] for i in range(256)]
dic = {}
for i in data:
    if("=" in i):
        label, length = i.split("=")
        index = hash(label)
        if label not in box[index]:
            box[index].append(label)
        dic[label] = int(length)
    else:
        label = i[:-1]
        index = hash(label)
        if label in box[index]:
            box[index].remove(label)
            del dic[label]

count = 0
for i,v in enumerate(box):
    if(not v):
        pass
    else:
        for j,val in enumerate(v):
            count += ((i+1)*((j+1)* dic[val]))
print(count)
    


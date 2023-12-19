file = open("data.txt").read().split("\n")

data = [i.split() for i in file]

def pred(data):
    data = [int(i) for i in data]
    last = data[-1]
    roz = []
    while(set(data) != {0}):
        temp = []
        for i in range(len(data)-1):
            temp.append(data[i+1] - data[i])
        data = temp
        roz.append(temp[-1])
    return (sum(roz)+last)
count = 0
for i in data:
    count += pred(i)
    
print(count)
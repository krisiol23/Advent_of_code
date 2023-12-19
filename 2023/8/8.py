import re
inst, data = open("data.txt").read().split("\n\n")

inst = [" ".join(i) for i in inst]
data = data.splitlines()
dic = {}

for line in data:
    node, elements = line.split(" = ")
    dic[node] = tuple(re.findall(r'(\w+)', elements))


i = 0
x = "AAA"
while(x!="ZZZ"):
    for ins in inst:
        if(ins == "L"):
            x = dic.get(x)[0]
        else:
            x = dic.get(x)[1]
        i+=1
        
print(i)

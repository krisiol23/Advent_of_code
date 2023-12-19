data = open("data.txt").read().split(",")

count = 0

for i in data:
    c = 0
    for j in i:
        c=((c+ord(j))*17) % 256
    count+=c
    
print(count)
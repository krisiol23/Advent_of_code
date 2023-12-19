#Shoelace formula, pick's theorem

data = open("data.txt").read().splitlines()
points = [(0,0)]
i = 0
b = 0
for line in data:
    d, n, _ = line.split()
    n= int(n)
    b+=n
    if(d == "R"):
        points.append((points[i][0],points[i][1]+n))
    elif(d == "D"):
        points.append((points[i][0]+n,points[i][1]))
    elif(d == "L"):
        points.append((points[i][0],points[i][1]-n))
    elif(d == "U"):
        points.append((points[i][0]-n,points[i][1]))
    i+=1

tab = []
for i in range(len(points)):
    try:
        tab.append(points[i][1]*(points[i-1][0] - points[i+1][0]))
    except IndexError:
        continue
    
A = abs(sum(tab))//2
i = A - (b//2) +1
print(b + i)

    

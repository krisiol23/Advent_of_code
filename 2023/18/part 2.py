data = open("data.txt").read().splitlines()
points = [(0,0)]
i = 0
b = 0
for line in data:
    d, n, heks = line.split()
    heks = heks.replace("(" , "").replace(")", "").replace("#", "0x")
    n = int(heks[:-1],16)
    d = heks[-1]
    b+=n
    if(d == "0"):
        points.append((points[i][0],points[i][1]+n))
    elif(d == "1"):
        points.append((points[i][0]+n,points[i][1]))
    elif(d == "2"):
        points.append((points[i][0],points[i][1]-n))
    elif(d == "3"):
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

    

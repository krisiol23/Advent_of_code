from collections import defaultdict
file = open("data.txt").read().split()
data = [[c for c in line] for line in file]
#print(data)

def czyDobre(d, i,j):
    for xi in [-1,0,1]:
        for xj in [-1,0,1]:
            try:
                if(i+xi<0 or i+xi > len(d) or j+xj < 0 or j+xj > len(d) or d[xi+i][j+xj] == "." or d[xi+i][j+xj].isdigit()):
                    pass
                else:
                    return True
                    
            except IndexError:
                continue
    return False

count = 0
dic = defaultdict(list)
for i in range(len(data)):
    dobre = False
    num= 0
    gear = False
    gearS = []
    for j in range(len(data[i])):
        if(data[i][j].isdigit()):
            num =  num *10 +  int(data[i][j])

            for xi in [-1,0,1]:
                for xj in [-1,0,1]:
                    try:
                        if(data[xi+i][j+xj] == "*"):
                            gearS = (xi+i, xj+j)
                            gear = True
                    except IndexError:
                        continue
        else: 
            if(gear):
                dic[gearS].append(num)
                gear = False
                gearS = ()
            num = 0
            
    if(gear):
        dic[gearS].append(num)
     
count = 0   
for k,val in dic.items():
    if(len(val) == 2):
        count+= val[0]* val[1]
print(count)


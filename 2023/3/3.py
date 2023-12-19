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
for i in range(len(data)):
    dobre = False
    num= 0
    for j in range(len(data[i])):
        if(data[i][j].isdigit()):
            num =  num *10 +  int(data[i][j])
            dobre = dobre or czyDobre(data,i,j)
        else: 
            if(dobre ):
                #print(num)
                count +=num
                dobre = False
            num = 0
    if(dobre):
        count +=num
        
print(count)

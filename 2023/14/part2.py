data = [list(line.strip()) for line in open("data.txt")]

def roll_r(data,di):
    for i in range(len(data[0])):
        for z in range(len(data)):
            for j in range(len(data)):
                if(di == 1):
                    if(data[j][i] == "O" and j > 0 and data[j-di][i] == "." ):
                        data[j][i] = "."
                        
                        data[j-di][i] = "O"
                else:
                    try:
                        if(data[j][i] == "O"  and data[j-di][i] == "." ):
                            data[j][i] = "."
                            data[j-di][i] = "O"
                    except IndexError:
                        continue      
    return data

def roll_c(data,di):
    for i in range(len(data)):
        for z in range(len(data[i])):
            for j in range(len(data[i])):
                if(di == -1):
                    try:
                        if(data[i][j] == "O"  and data[i][j-di] == "." ):
                            data[i][j] = "."
                            
                            data[i][j-di] = "O"
                    except IndexError:
                        continue
                else:
                    try:
                        if(data[i][j] == "O"  and j> 0 and data[i][j-di] == "." ):
                            data[i][j] = "."
                            
                            data[i][j-di] = "O"
                    except IndexError:
                        continue                
    return data
  
for i in range(1000000000):
    data = roll_r(data,1)
    data = roll_c(data,1)
    data = roll_r(data,-1)
    data = roll_c(data,-1)
    
    count = 0
    for i, v in enumerate(data[::-1]):
        c = 0
        for j, ch in enumerate(v):
             if(ch == "O"):
                 c+=1
        count+= c*(i+1)
    print(count)
#if the numbers are repeatedd stop and find correct   
#79723


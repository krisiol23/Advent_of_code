data = [list(line.strip()) for line in open("data.txt")]

for i in range(len(data[0])):
    for z in range(len(data)):
        for j in range(len(data)):
            if(data[j][i] == "O" and j > 0 and data[j-1][i] == "." ):
                data[j][i] = "."
                
                data[j-1][i] = "O"
       

count = 0
for i, v in enumerate(data[::-1]):
    c = 0
    for j, ch in enumerate(v):
         if(ch == "O"):
             c+=1
    count+= c*(i+1)
print(count)
        
        
def convert(a):
    it = iter(a)
    res = dict(zip(it,it))
    return res

with open("data.txt") as f:
    file = f.read().replace(",", "").replace(";", "").replace(":", "").split("\n")
    file = [i.split(" ") for i in file]
    #file = [{i[j]: i[j+1] for j in range(0,len(i), 2)} for i in file ]
    #print(file)
    
    suma = 0
    for i in file:
        r = []
        g = []
        b = []
        #i = convert(i)
        #print(i)
        #for key, val in i.items():
            #if(val == "red"):
                #r.append(int(key))
            #elif(val == "green"):
                #g.append(int(key))
            #elif(val == "blue"):
                #b.append(int(key))
        for j in range(len(i)):
            if(i[j] == "red"):
                r.append(int(i[j-1]))
            elif(i[j] == "green"):
                g.append(int(i[j-1]))
            elif(i[j] == "blue"):
                b.append(int(i[j-1]))
        suma+=max(r) * max(g) * max(b)
    print(suma)
            
           

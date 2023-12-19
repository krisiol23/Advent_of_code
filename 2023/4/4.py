def check(tab, index):
    count = 0
    for j in range(0,len(tab),2):
            for val in range(2,len(tab[j])):
                if(tab[j][val] in tab[j+1]):
                    count+=1
    print(count)
    arr = [i for i in range(index+1,count+(index+1))]
    return arr

with open("example.txt") as f:
    file = f.read().strip().splitlines()
    
    file = [i.split("|") for i in file]
    file = [[j.split() for j in i] for i in file]
    print(file)
    
    suma = 0
    for index,i in enumerate(file):
        tab = []
        tab = check(i, index+1)
        print("Pocz",tab)
        
            
        suma+=1   
        #print(index+1,count)
       
print(suma-1)
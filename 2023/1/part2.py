with open("data.txt") as f:
    file = f.read().split()
    string = {"one":"o1e", "two":"t2o", "three":"t3te", "four":"f4r", "five":"f5e", "six":"s6x","seven":"s7n", "eight":"e8t", "nine":"n9e"}
    arr = []
    for i in file:
        tab = []
        for key,value in string.items():
            i = i.replace(key,value)
        
        for j in i:
            if(j.isdigit()):
                tab.append(j) 
        
                
        if(len(tab) > 1):
            tab = [tab[0], tab[-1]]
        else:
            tab = [tab[0],tab[0]]
        
        stri = ""
        for j in tab:
            stri += j
        arr.append(int(stri))
    print(sum(arr))

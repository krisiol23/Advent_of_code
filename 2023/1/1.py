with open("data.txt") as f:
    file = f.read().split()
    suma = 0
    arr = []
    for i in file:
        tab = []
        for j in i:
            if(j.isdigit()):
                tab.append(j)
        if(len(tab) > 1):
            tab = [tab[0], tab[-1]]
        else:
            tab = [tab[0],tab[0]]
        #print(tab)
        stri = ""
        for j in tab:
            stri += j
        arr.append(int(stri))
    print(sum(arr))
        

with open("data.txt") as f:
    file = f.read().replace(",", "").replace(";", "").replace(":", "").split("\n")
    file = [i.split(" ") for i in file]
    #print(file)

    suma = 0
    for i in file:
        flag = True
        for ind, val in enumerate(i):
            if(val == "blue" and int(i[ind-1]) >14):
                flag = False
            elif(val == "red" and int(i[ind-1]) >12):
                flag = False
            elif(val == "green" and int(i[ind-1]) >13):
                flag = False
        if(flag):
            suma += int(i[1])
    print(suma)

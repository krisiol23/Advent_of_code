def res(num,speed):
    dist = 0
    tab = []
    for i in range(num+1):
        dist = i*(num-i)
        if(dist > speed):
            tab.append(dist)
    return(len(tab))

time,speed = open("data.txt").read().split("\n")

time = [int(i) for i in time.split()[1:]]
speed = [int(i) for i in speed.split()[1:]]
#print(time, speed)

suma = 1
res(time[0], speed[0])
for i in range(len(time)):
    suma*=res(time[i], speed[i])
print(suma)
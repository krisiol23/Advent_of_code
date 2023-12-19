def res(num,speed):
    dist = 0
    tab = []
    for i in range(num+1):
        dist = i*(num-i)
        if(dist > speed):
            tab.append(dist)
    return(len(tab))

time,speed = open("data.txt").read().split("\n")

time = [i for i in time.split()[1:]]
speed = [i for i in speed.split()[1:]]
time = int("".join(time))
speed = int("".join(speed))

print(res(time, speed))
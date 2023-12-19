import numpy as np
def check(mini, maps):
    for i in maps:
        _, *ranges = i.split("\n")
        ranges = [i.split() for i in ranges]
        for num in ranges:
            src = int(num[1])
            dst = int(num[0])
            ran = int(num[2])
            if(src<=mini<src+ran):
                #tab = np.arange(src, src+ran)
                #tab1 = np.arange(dst, dst+ran)
                #temp = np.where(tab==mini)[0][0]
                #mini = tab1[temp]
                mini = mini+dst - src
                break
            else:
                mini = mini
    print(mini)

seeds, *maps = open('data.txt').read().split('\n\n')

seeds = [int(x) for x in seeds.split(":")[1].split()]
for i in seeds:
    check(i, maps)

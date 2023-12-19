data = open("data.txt").read().splitlines()
e_rows = [r for r, row in enumerate(data) if all(ch == "." for ch in row)]

e_cols = []
for i, val in enumerate(zip(*data)):
    if all(ch == "." for ch in val):
        e_cols.append(i)

tab = []
scale = 999999 # part2 / part1 scale = 1
index = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        if(data[i][j] == "#"):
            tab.append((i,j))

count = 0
for i in range(len(tab)):
    for j in range(len(tab[:i])):
        count += abs(tab[i][1] - tab[j][1]) + abs(tab[i][0] - tab[j][0])
        
        for r in e_rows:
            if(tab[i][0] > tab[j][0]):
                if r in range(tab[j][0],tab[i][0]):
                    count+=scale
            else:
                if r in range(tab[i][0],tab[j][0]):
                    count+=scale
            
        for c in e_cols:
            if(tab[i][1] > tab[j][1]):
                if c in range(tab[j][1],tab[i][1]):
                    count+=scale
            else:
                if c in range(tab[i][1],tab[j][1]):
                    count+=scale
print(count)

from collections import Counter, defaultdict
data = open("data.txt").read().splitlines()

data = [i.split() for i in data]

#stren = ["A", "K", "Q", "J", "T"] #five - 7, four - 6 itd

def check(hand):
    hand = hand.replace("A", "E")
    hand = hand.replace("K", "D")
    hand = hand.replace("Q", "C")
    hand = hand.replace("J", "B")
    hand = hand.replace("T", "A")
    counter = dict(Counter(hand).most_common())
    maks = max(counter, key=counter.get)
    indices = {(k,v) for k,v in counter.items() if v == counter.get(maks)}
    
    if(counter.get(maks) == 5):
        return (7,hand)
    elif(counter.get(maks) == 4):
        return (6,hand)
    elif(len(counter) == 2):
        return (5,hand)
    elif(counter.get(maks) == 3):
        return (4,hand)
    elif(len(indices) == 2):
        return (3,hand)
    elif(counter.get(maks) == 2):
        return (2,hand)
    else:
        return (1, hand)
    
dic = {}

for i in data:
    dic[i[0]] = i[1]

dic =  dict(sorted(dic.items(), key = lambda x:check(x[0])))
count = 0
for ind, (k,v) in enumerate(dic.items()):
    count += (ind+1) * int(v)
print(count)
    

    
    
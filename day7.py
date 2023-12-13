with open('puzzleInput.txt') as f:
    y = f.read()
y,yy=y.splitlines(),[]
for i in range(len(y)):
    y[i]=y[i].split(" ")

'''
part one
def check(x):
    if x[0]==x[1]==x[2]==x[3]==x[4]:
        return 0
    elif x[0]==x[1]==x[2]==x[3] or x[1]==x[2]==x[3]==x[4]:
        return 1
    elif (x[0]==x[1]==x[2] and x[3]==x[4]) or (x[2]==x[3]==x[4] and x[0]==x[1]):
        return 2
    elif x[0]==x[1]==x[2] or x[1]==x[2]==x[3] or x[2]==x[3]==x[4]:
        return 3
    elif (x[0]==x[1] and x[2]==x[3]) or (x[0]==x[1] and x[3]==x[4]) or (x[2]==x[1] and x[4]==x[3]):
        return 4
    elif x[0]==x[1] or x[2]==x[1] or x[2]==x[3] or x[3]==x[4]:
        return 5
    else:
        return 6
rank = ("A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2")
for i,j in enumerate(y):
    temp=[]
    for k,l in enumerate(j[0]):
        temp.append(rank.index(y[i][0][k]))
        temp.sort()
    y[i].append(check(temp))
for i,j in enumerate(y):
    temp=[]
    for k,l in enumerate(j[0]):
        temp.append(rank.index(y[i][0][k]))
        temp.sort
    y[i][0]=temp
for i,j in enumerate(y):
    temp=[]
    for k,l in enumerate(y[i]):
        if k == 0:
            for m, n in enumerate(y[i][0]):
                temp.append(int(n))
        else:
            temp.append(int(y[i][k]))
    yy.append(temp)

y = sorted(yy, key=lambda x: (x[6], x[0], x[1], x[2], x[3], x[4]), reverse=True)
ans=0
for i,j in enumerate(y):
    ans+=j[5]*(i+1)
print(ans)
'''

'''
part two
rank = ("A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J")
def check2(x):
    if x[0]==x[1]==x[2]==x[3]==x[4]:
        return 0
    elif x[0]==x[1]==x[2]==x[3] or x[1]==x[2]==x[3]==x[4]:
        if 12 in x:
            return 0
        else:
            return 1
    elif (x[0]==x[1]==x[2] and x[3]==x[4]) or (x[2]==x[3]==x[4] and x[0]==x[1]):
        if 12 in x:
            return 0
        else:
            return 2
    elif x[0]==x[1]==x[2] or x[1]==x[2]==x[3] or x[2]==x[3]==x[4]:
        if 12 in x:
            return 1
        else:
            return 3
    elif (x[0]==x[1] and x[2]==x[3]) or (x[0]==x[1] and x[3]==x[4]) or (x[2]==x[1] and x[4]==x[3]):
        if x.count(12)==2:
            return 1
        elif x.count(12)==1:
            return 2
        else:
            return 4
    elif x[0]==x[1] or x[2]==x[1] or x[2]==x[3] or x[3]==x[4]:
        if 12 in x:
            return 3
        else:
            return 5
    else:
        if 12 in x:
            return 5
        else:
            return 6
for i,j in enumerate(y):
    temp=[]
    for k,l in enumerate(j[0]):
        temp.append(rank.index(y[i][0][k]))
        temp.sort()
    y[i].append(check2(temp))
for i,j in enumerate(y):
    temp=[]
    for k,l in enumerate(j[0]):
        temp.append(rank.index(y[i][0][k]))
        temp.sort
    y[i][0]=temp
for i,j in enumerate(y):
    temp=[]
    for k,l in enumerate(y[i]):
        if k == 0:
            for m, n in enumerate(y[i][0]):
                temp.append(int(n))
        else:
            temp.append(int(y[i][k]))
    yy.append(temp)
y = sorted(yy, key=lambda x: (x[6], x[0], x[1], x[2], x[3], x[4]), reverse=True)
ans=0
for i,j in enumerate(y):
    print(j,j[5],i+1)
    ans+=j[5]*(i+1)
print(ans)
'''
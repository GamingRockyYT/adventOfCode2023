with open('puzzleInput.txt') as f:
    y = f.read()
y=y.splitlines()

for i,j in enumerate(y):
    y[i]=j[8::].replace("  "," ").split(" | ")
    for k,l in enumerate(y[i]):
        y[i][k]=l.split(" ")
for i,j in enumerate(y):
    for k,l in enumerate(j):
        for m,n in enumerate(l):
            if n=="":
                y[i][k].pop(m)


'''
part 1
score=0
for i,j in enumerate(y):
    temp=0
    for k in j[1]:
        if k in j[0]:
            if temp==0:
                temp+=1
            else:
                temp*=2
    score+=temp
print(score)
'''

'''
part 2

for i,j in enumerate(y):
    y[i].append(i)

score=0
for i,j in enumerate(y):
    count=0
    for k in y[i][1]:
        if k in y[i][0]:
            count+=1
    score+=count
    if count!=0:
        for l in range(y[i][2]+1,y[i][2]+1+count):
            y.append(y[l])
print(len(y))
'''
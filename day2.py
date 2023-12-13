with open('puzzleInput.txt') as f:
    y=f.read()
y=y.splitlines()
color=["red","green","blue"]
num=["0","1","2","3","4","5","6","7","8","9"]
temp=[]
caseMax=[0,0,0]
finalCaseMax=[]
caseMin,finalCaseMin=[100,100,100],[]
'''
part One
for i in range(len(y)):
    y[i]=y[i].replace("Game "+str(i+1)+": ","")
    y[i]=y[i].replace(",","")
for i in range(len(y)):
    y[i]=y[i].split(";")
for i,j in enumerate(y):
    for k,l in enumerate(j):
        for m in color:
            if m not in l:
                y[i][k]+=" 0 "+m
            y[i][k] = y[i][k].replace(" ", "")
for i,j in enumerate(y):
    for k,l in enumerate(j):
        for m,n in enumerate(l):
            if m==0:
                continue
            elif n in num and l[m-1] not in num:
                temp.append(int(m))
        y[i][k]=y[i][k][0:temp[0]]+" "+y[i][k][temp[0]:temp[1]]+" "+y[i][k][temp[1]:len(y[i][k])]
        temp=[]
for i,j in enumerate(y):
    for k,l in enumerate(j):
        y[i][k]=y[i][k].split(" ")
for i,j in enumerate(y):
    for k,l in enumerate(j):
        for m,n in enumerate(l):
            if "red" in n:
                n=n.replace("red","")
                if int(n)>int(caseMax[0]):
                    caseMax[0]=n
            elif "green" in n:
                n=n.replace("green", "")
                if int(n)>int(caseMax[1]):
                    caseMax[1]=n
            elif "blue" in n:
                n=n.replace("blue", "")
                if int(n)>int(caseMax[2]):
                    caseMax[2]=n
    finalCaseMax.append(caseMax)
    caseMax=[0,0,0]
ans=0
for i,j in enumerate(finalCaseMax):
    if int(j[0])<=12 and int(j[1])<=13 and int(j[2])<=14:
        ans+=i+1
print(ans)
'''

'''
part Two
for i in range(len(y)):
    y[i]=y[i].replace("Game "+str(i+1)+": ","")
    y[i]=y[i].replace(",","")
for i in range(len(y)):
    y[i]=y[i].split(";")
for i,j in enumerate(y):
    for k,l in enumerate(j):
        for m in color:
            if m not in l:
                y[i][k]+=" 0 "+m
            y[i][k] = y[i][k].replace(" ", "")
for i,j in enumerate(y):
    for k,l in enumerate(j):
        for m,n in enumerate(l):
            if m==0:
                continue
            elif n in num and l[m-1] not in num:
                temp.append(int(m))
        y[i][k]=y[i][k][0:temp[0]]+" "+y[i][k][temp[0]:temp[1]]+" "+y[i][k][temp[1]:len(y[i][k])]
        temp=[]
for i,j in enumerate(y):
    for k,l in enumerate(j):
        y[i][k]=y[i][k].split(" ")
for i,j in enumerate(y):
    for k,l in enumerate(j):
        for m,n in enumerate(l):
            if "red" in n:
                n=n.replace("red","")
                if int(n)>int(caseMax[0]):
                    caseMax[0]=n
            elif "green" in n:
                n=n.replace("green", "")
                if int(n)>int(caseMax[1]):
                    caseMax[1]=n
            elif "blue" in n:
                n=n.replace("blue", "")
                if int(n)>int(caseMax[2]):
                    caseMax[2]=n
    finalCaseMax.append(caseMax)
    caseMax=[0,0,0]
ans=0
power=1
for i,j in enumerate(finalCaseMax):
    for k in range(len(j)):
        power*=int(j[k])
    ans+=power
    power=1
print(ans)
'''

with open('puzzleInput.txt') as f:
    y=f.read()
y=y.split("""

""")
yy=[]
for i,j in enumerate(y):
    for k,l in enumerate(j):
        if l==":":
            y[i]=y[i][k+1::]
y[0]=y[0][1::]
for i in y:
    yy.append(i)
for i,j in enumerate(yy):
    yy[i]=yy[i].splitlines()
    if yy[i][0]=="":
        yy[i].pop(0)
    for k,l in enumerate(yy[i]):
        yy[i][k]=yy[i][k].split(" ")
        for m,n in enumerate(yy[i][k]):
            yy[i][k][m]=int(n)

'''
part one
loc=[]
for i in yy[0][0]:
    num=i
    for j,k in enumerate(yy):
        iterated = False
        if j==0:
            continue
        else:
            for l,m in enumerate(k):
                if m[1]<=num<=m[2]+m[1]-1 and not iterated:
                    num=num+(m[0]-m[1])
                    iterated=True
    loc.append(num)
print(min(loc))
'''

yyy=[]
for i in range(0,len(yy[0][0]),2):
    yyy.append([yy[0][0][i],yy[0][0][i]+yy[0][0][i+1]-1])
yy.pop(0)
for i,j in enumerate(yy):
    for k,l in enumerate(yy[i]):
        yy[i][k][2]=l[2]+l[1]-1
print(yyy)
for i,j in enumerate(yy):
    temp=[]
    for k,l in enumerate(yyy):
        its=False
        for m,n in enumerate(j):
            if its:
                break
            if n[1] <= l[0] <= l[1] <= n[2]:
                temp.append([n[0], n[2] + n[0] - n[1]])
                its=True
            elif l[0]<n[1] and n[1]<=l[1]<=n[2]:
                temp.append([l[0],n[1]-1])
                temp.append([n[0],l[1]+n[0]-n[1]])
                its=True
            elif n[1]<=l[0]<=n[2] and l[1]>n[2]:
                temp.append([l[0]+n[0]-n[1],n[2]+n[0]-n[1]])
                temp.append([n[2]+1,l[1]])
                its=True
            elif l[0]<n[1] and l[1]>n[2]:
                temp.append([l[0],n[1]-1])
                temp.append([n[0], n[2] + n[0] - n[1]])
                temp.append([n[2] + 1, l[1]])
                its=True
    yyy=temp
    print(yyy)






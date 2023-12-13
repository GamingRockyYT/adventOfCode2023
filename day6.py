import math as m
with open('puzzleInput.txt') as f:
    y = f.read()
y=y.splitlines()
num=["0","1","2","3","4","5","6","7","8","9"]
for i in range(len(y)):
    y[i]=y[i][11::].split(" ")
    while "" in y[i]:
        for j in range(len(y[i])):
            try:
                if y[i][j]=="":
                    y[i]=y[i][0:j]+y[i][j+1::]
            except IndexError:
                pass

'''
part one
ans=1
for i in range(len(y[0])):
    tmp=0
    for j in range(int(y[0][i])+1):
        if j*(int(y[0][i])-j)>int(y[1][i]):
            tmp+=1
    ans*=tmp
print(ans)
'''

'''
part two
for i in range(len(y)):
    tmp = ""
    for j in y[i]:
        tmp=tmp+j
    y[i]=int(tmp)

yy=[((y[0]-m.sqrt(y[0]**2-4*y[1]))/2)//1+1,((y[0]+m.sqrt(y[0]**2-4*y[1]))/2)//1]
print((yy[1]-yy[0]+1))
'''
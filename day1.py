with open('puzzleInput.txt') as f:
    y = f.read()

'''
part one
x,y,num="",y.splitlines(),["0","1","2","3","4","5","6","7","8","9"]
for i,j in enumerate(y):
    for k,l in enumerate(j):
        if l in num:
            x+=l
    y.pop(i)
    y.insert(i,x)
    x=""
ans=0
for i in y:
    ans+=int(i[0]+i[-1])
print(ans)
'''

'''
part two
x,y,num,num2,ans="",y.splitlines(),["0","1","2","3","4","5","6","7","8","9"],["zero","one","two","three","four","five","six","seven","eight","nine"],0
for i in range(len(y)):
    for k,l in enumerate(num2):
        y[i]=y[i].replace(l,l[0]+str(k)+l[-1])

for i,j in enumerate(y):
    for l in j:
        print(j,l,l in num)
        if l in num:
            x+=l
    y.pop(i)
    y.insert(i,x)
    x=""
for i in y:
    ans+=int(i[0]+i[-1])
print(ans)
'''

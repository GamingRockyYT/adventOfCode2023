from math import lcm

with open('puzzleInput.txt') as f:
    y=f.read()
y=y.splitlines()
y.pop(1)
arr=y[0].replace("L","0").replace("R","1")
y.pop(0)
for i in range(len(y)):
    y[i]=y[i].replace(" = ("," ").replace(", "," ").replace(")","").split(" ")
dict={
}
for i in y:
    dict[i[0]]=[i[1],i[2]]

'''
part one
curr,cnt="AAA",0
while curr!="ZZZ":
    for i in arr:
        curr=dict[curr][int(i)]
        cnt+=1
print(cnt)
'''

'''
part two
curr,cnt=[i[0] for i in y if i[0][-1]=="A"],0
for i,j in enumerate(curr):
    curr2,cnt=j,0
    while curr2[-1]!="Z":
        for k in arr:
            curr2 = dict[curr2][int(k)]
            cnt += 1
    curr[i]=cnt
print(lcm(curr[0],curr[1],curr[2],curr[3],curr[4],curr[5]))
'''





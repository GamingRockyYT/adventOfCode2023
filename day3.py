with open('puzzleInput.txt') as f:
    y = f.read()
y=y.splitlines()
for i,j in enumerate(y):
    y[i]=[k for k in j]
ignore=["0","1","2","3","4","5","6","7","8","9","."]
fsum=0

'''
part one

for i,j in enumerate(y):
    for k,l in enumerate(j):
        inc,kp,psum=False,k, ""
        if l in ignore[0:10]:
            try:
                if y[i-1][k-1] not in ignore:
                    inc=True
            except IndexError:
                pass
            try:
                if y[i-1][k] not in ignore:
                    inc=True
            except IndexError:
                pass
            try:
                if y[i-1][k+1] not in ignore:
                    inc=True
            except IndexError:
                pass
            try:
                if y[i][k-1] not in ignore:
                    inc=True
            except IndexError:
                pass
            try:
                if y[i][k+1] not in ignore:
                    inc=True
            except IndexError:
                pass
            try:
                if y[i+1][k-1] not in ignore:
                    inc=True
            except IndexError:
                pass
            try:
                if y[i+1][k] not in ignore:
                    inc=True
            except IndexError:
                pass
            try:
                if y[i+1][k+1] not in ignore:
                    inc=True
            except IndexError:
                pass
            if inc:
                while y[i][kp] in ignore[0:10] and kp<=len(j):
                    psum= psum + y[i][kp]
                    y[i][kp] = "."
                    kp+=1
                    if kp==len(j):
                        break
                kp=k-1
                while y[i][kp] in ignore[0:10] and kp>=0:
                    psum= y[i][kp] + psum
                    y[i][kp] = "."
                    kp-=1
                    if kp<0:
                        break
                fsum+=int(psum)
print(fsum)
'''

'''
part 2
for i,j in enumerate(y):
    for k,l in enumerate(j):
        if l=="*":
            psum, numarr = "", []
            try:
                if y[i - 1][k - 1] in ignore[0:10]:
                    ip, kp = i - 1, k - 1
                    while y[ip][kp] in ignore[0:10] and kp <= len(j):
                        psum = psum + y[ip][kp]
                        y[ip][kp] = "."
                        kp += 1
                        if kp == len(j):
                            break
                    kp = k - 2
                    while y[ip][kp] in ignore[0:10] and kp >= 0:
                        psum = y[ip][kp] + psum
                        y[ip][kp] = "."
                        kp -= 1
                        if kp < 0:
                            break
                    numarr.append(psum)
                    psum = ""
            except IndexError:
                pass
            try:
                if y[i - 1][k] in ignore[0:10]:
                    ip, kp = i - 1, k
                    while y[ip][kp] in ignore[0:10] and kp <= len(j):
                        psum = psum + y[ip][kp]
                        y[ip][kp] = "."
                        kp += 1
                        if kp == len(j):
                            break
                    kp = k - 1
                    while y[ip][kp] in ignore[0:10] and kp >= 0:
                        psum = y[ip][kp] + psum
                        y[ip][kp] = "."
                        kp -= 1
                        if kp < 0:
                            break
                    numarr.append(psum)
                    psum = ""
            except IndexError:
                pass
            try:
                if y[i - 1][k + 1] in ignore[0:10]:
                    ip, kp = i - 1, k + 1
                    while y[ip][kp] in ignore[0:10] and kp <= len(j):
                        psum = psum + y[ip][kp]
                        y[ip][kp] = "."
                        kp += 1
                        if kp == len(j):
                            break
                    kp = k
                    while y[ip][kp] in ignore[0:10] and kp >= 0:
                        psum = y[ip][kp] + psum
                        y[ip][kp] = "."
                        kp -= 1
                        if kp < 0:
                            break
                    numarr.append(psum)
                    psum = ""
            except IndexError:
                pass
            try:
                if y[i][k - 1] in ignore[0:10]:
                    ip, kp = i, k - 1
                    while y[ip][kp] in ignore[0:10] and kp <= len(j):
                        psum = psum + y[ip][kp]
                        y[ip][kp] = "."
                        kp += 1
                        if kp == len(j):
                            break
                    kp = k - 2
                    while y[ip][kp] in ignore[0:10] and kp >= 0:
                        psum = y[ip][kp] + psum
                        y[ip][kp] = "."
                        kp -= 1
                        if kp < 0:
                            break
                    numarr.append(psum)
                    psum = ""
            except IndexError:
                pass
            try:
                if y[i][k + 1] in ignore[0:10]:
                    ip, kp = i, k + 1
                    while y[ip][kp] in ignore[0:10] and kp <= len(j):
                        psum = psum + y[ip][kp]
                        y[ip][kp] = "."
                        kp += 1
                        if kp == len(j):
                            break
                    kp = k
                    while y[ip][kp] in ignore[0:10] and kp >= 0:
                        psum = y[ip][kp] + psum
                        y[ip][kp] = "."
                        kp -= 1
                        if kp < 0:
                            break
                    numarr.append(psum)
                    psum = ""
            except IndexError:
                pass
            try:
                if y[i + 1][k - 1] in ignore[0:10]:
                    ip, kp = i + 1, k - 1
                    while y[ip][kp] in ignore[0:10] and kp <= len(j):
                        psum = psum + y[ip][kp]
                        y[ip][kp] = "."
                        kp += 1
                        if kp == len(j):
                            break
                    kp = k - 2
                    while y[ip][kp] in ignore[0:10] and kp >= 0:
                        psum = y[ip][kp] + psum
                        y[ip][kp] = "."
                        kp -= 1
                        if kp < 0:
                            break
                    numarr.append(psum)
                    psum = ""
            except IndexError:
                pass
            try:
                if y[i + 1][k] in ignore[0:10]:
                    ip, kp = i + 1, k
                    while y[ip][kp] in ignore[0:10] and kp <= len(j):
                        psum = psum + y[ip][kp]
                        y[ip][kp] = "."
                        kp += 1
                        if kp == len(j):
                            break
                    kp = k - 1
                    while y[ip][kp] in ignore[0:10] and kp >= 0:
                        psum = y[ip][kp] + psum
                        y[ip][kp] = "."
                        kp -= 1
                        if kp < 0:
                            break
                    numarr.append(psum)
                    psum = ""
            except IndexError:
                pass
            try:
                if y[i + 1][k + 1] in ignore[0:10]:
                    ip, kp = i + 1, k + 1
                    while y[ip][kp] in ignore[0:10] and kp <= len(j):
                        psum = psum + y[ip][kp]
                        y[ip][kp] = "."
                        kp += 1
                        if kp == len(j):
                            break
                    kp = k
                    while y[ip][kp] in ignore[0:10] and kp >= 0:
                        psum = y[ip][kp] + psum
                        y[ip][kp] = "."
                        kp -= 1
                        if kp < 0:
                            break
                    numarr.append(psum)
                    psum = ""
            except IndexError:
                pass
            if len(numarr)==2:
                fsum+=int(numarr[0])*int(numarr[1])

print(fsum)
'''
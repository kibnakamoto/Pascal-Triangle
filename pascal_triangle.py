#n = 20
#tmp = []
#prev = []
#for i in range(1,n):
#    print((n-i)*" ", end='')
#    for j in range(i):
#        if j == i-1:
#            print(1, end='')
#            tmp.append(1)
#
#            prev = tmp[:]
#            tmp = []
#        elif j != 0:
#            print(prev[j-1] + prev[j], end=' ')
#            tmp.append(prev[j-1] + prev[j])
#
#        else:
#            print(1, end=' ')
#            tmp.append(1)
#
#    print()
n = 25
tmp = []
prev = []
prevs = []
for i in range(1,n):
    for j in range(i):
        if j == i-1:
            tmp.append(1)

            prev = tmp[:]
            tmp = []
            prevs.append(prev)
        elif j != 0:
            tmp.append(prev[j-1] + prev[j])

        else:
            tmp.append(1)

mul = n//10+1
for i in range(len(prevs)):
    print((n*mul-i*mul)*" ", end='')
    for j in range(len(prevs[i])):
        #print(str(prevs[i][j]).zfill(len(str(max(prevs[-1])))), end=' ')
        print(str(prevs[i][j]), end=(len(str(max(prevs[-1])))-len(str(prevs[i][j]))+1)*' ')
    print()

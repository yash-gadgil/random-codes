
###
'''
m,n = eval(input("Enter m and n: "))
li = [[[] for k in range(n)] for i in range(m)]
li[0][0].append(1)
for a,i in enumerate(li):
    for b in range(len(i)): [exec('try:li[j[0]][j[1]].extend(li[a][b])\nexcept:pass') for j in [(a+1,b),(a,b+1)]]
print(len(li[a][b]))
'''

'''
m,n = eval(input("Enter m and n: "))
li = [[[] for k in range(n)] for i in range(m)]
li[0][0].append(1)
#for a,i in enumerate(li):
#    for b in range(len(i)):
[[[print(j[0],j[1]) for j in [(a+1,b),(a,b+1)]] for b in range(len(i))] for a,i in enumerate(li)]
print(len(li[m-1][n-1]))
'''

###

m,n = eval(input("Enter m and n: "))
li = [[0 for k in range(n)] for i in range(m)]
li[0][0] = 1
for a,i in enumerate(li):
    for b in range(len(i)): [exec('try:li[j[0]][j[1]] += li[a][b]\nexcept:pass') for j in [(a+1,b),(a,b+1)]]
print(li[a][b])


'''
m,n = eval(input("Enter m and n: "))
li = [[0 for k in range(n)] for i in range(m)]
li[0][0] = 1
for a,i in enumerate(li):
    [[[exec("try: li[j[0]][j[1]] += li[a][b]\nexcept: pass\nprint(1)")] for j in [(a+1,b),(a,b+1)]] for b in range(len(i))] #exec('try:li[j[0]][j[1]] += li[a][b]\nexcept:pass')
print(li)
print(li[m-1][n-1])
'''

'''
m,n = eval(input("Enter m and n: "))
li = [[[] for k in range(n)] for i in range(m)]
li[0][0].append(1)

[exec("for b in range(len(i)): [exec('try:li[j[0]][j[1]].extend(li[a][b])\nexcept:pass') for j in [(a+1,b),(a,b+1)]]") for a,i in enumerate(li)]
print(len(li[a][b]))
'''



#from pickle import *
#with open('savefile.txt','r') as f:
    #f.write("[1,2,3,4,5]")
    #f.write("\n[123, 624, 662, 136]")
    #li = [eval(i) for i in f.readlines()]
#from random import *
#n = [3,4,6,8,1,2]
#scores = []
'''
    x = randint(0,len(n)-1)
    x = n.pop(x)
    y = randint(0,len(n)-1)
    y = n.pop(y)
'''
'''
for i in n:
    for k in n:

        if i == n: continue
        
        scores.append(i*gcd(x,y))
'''       
'''
for i in range(0,len(n)//2,2):

    x, y = n[i], n[i+1]

    scores.append(i*gcd(x,y))

print('max-',sum(scores))
'''
'''
for i in range(len(n)//2):
    s = []
'''
'''
l = [7,1,4,10,5,8,12]
temp = l.copy()
temp.sort()
sum1 = sum([l[i]-temp[i] if l[i] > temp[i] else temp[i]-l[i] for i in range(0,len(l))])
print("YES",sum1) if sum1 <= i else print("NO")
'''
'''
[7, 1, 4, 10, 5, 8, 12]
[1, 4, 5, 7, 8, 10, 12]
'''
'''
li, kp, d = eval(input("li~")), input("kp~"), {}
d[kp[0]], g = li[0], (0,0)
for i in range(1,len(li)): 
    if kp[i] not in d: d[kp[i]] = li[i] - li[i-1]
    elif li[i] - li[i-1] > d[kp[i]]: d[kp[i]] = li[i] - li[i-1]
    if d[kp[i]] > g[0]:
        g = d[kp[i]],kp[i]
print(g[1])
'''
'''
li, kp, d = eval(input("li~")), input("kp~"), {}
d[li[0]] = kp[0]
for i in range(1,len(li)): 
    if kp[i] not in d:
        d[li[i] - li[i-1]] = kp[i]
    elif li[i] - li[i-1] > d[kp[i]]:
        d[li[i] - li[i-1]] = kp[i]
'''
'''
    s = set([tuple(sorted((a,b))) for a,k in enumerate(l) for b,i in enumerate(l) if (i + k)%60 == 0 and a != b])

    print(s)

    return len(s)
'''
'''
d = {'f':40, 'g': d_inv}
globals().update(d)
'''
#def unq_p_no(l,t): return len(set([tuple(sorted((i,k))) for k in l for i in l if i + k == t]))
#print(dist_p_no([60,60,60]))
#d = {1: '1', 2: '2', 3:'3'}
#print(d_inv(d))


def decoder(s):
    li = [0]*26
    for i in range(len(s)):
        if s[i] == '#': continue
        try:
            if s[i + 1] == '#': continue
            if s[i + 2] == "#":
                try:
                    if s[i + 3] == "(":
                        g, g1 = "", 0
                        while s[i + 4 + g1] != ")":
                            g += s[i + 4 + g1]
                            g1 += 1
                        li[int(s[i] + s[i + 1]) - 1] += 1*int(g)
                    else: li[int(s[i] + s[i + 1]) - 1] += 1
                except: li[int(s[i] + s[i + 1]) - 1] += 1
            else:
                try: 
                    if s[i + 1] == "(":
                        g, g1 = "", 0
                        while s[i + 1 + g1] != ")":
                            g += s[i + 4 + g1]
                            g1 += 1
                        li[int(s[i]) - 1] += 1*int(g)
                    else: li[int(s[i]) - 1] += 1
                except: pass
        except: pass
    return li

def gcd(x,y):
    f = max([k for k in [i for i in range(1,y) if y%i==0] if k in [i for i in range(1,x) if x%i==0]])
    return f if f != [] else 0

def unq_p_no(l,t):
    return len({tuple(sorted((i,k))) for k in l for i in l if i + k == t})

def dist_p_no(l):
    return len({tuple(sorted((a,b))) for a,k in enumerate(l) for b,i in enumerate(l) if (i + k)%60 == 0 and a != b})
    
def d_inv(d):
    return dict([(d[i],i) for i in d])


print(unq_p_no([7,3,14,15,1,13,6,9],21))

li = [[0]*5]*3
















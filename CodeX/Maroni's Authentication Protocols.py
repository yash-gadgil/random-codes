


#First 2 no.'s printed are the no. of numbers and no. of lists respectively
#The no.'s in the encrypted list printed first are the no. of no.'s in
#other lists that are smaller than it

from random import *
while 1:
    n, k, = randint(11,21), randint(3,10)
    li, lenc, flist = [i for i in range(1,n+1)], n//k, [[] for i in range(k)]
    for i in range(len(flist)):
        if i == k-1:
            flist[i] = li
            break
        for cout in range(lenc):
            flist[i].append(li.pop(randint(0,len(li)-1)))
    li, fflist = [i for i in range(1,n+1)], [[] for i in range(k)]
    for i,ele in enumerate(flist):
        for ele1 in ele: li.remove(ele1)
        for ele1 in ele:
            fe = 0
            for ele2 in li:
                if ele2 < ele1: fe += 1
            fflist[i].append(fe)
        for ele1 in ele: li.append(ele1)            
    print(n,k)
    print(fflist)
    f = input("~")
    print(flist)

    cc = input("\n~~ ")


'''
n,k = eval(input("Enter n and k: "))
decoded, li, ele, flist = False, [list(eval(input("~ "))) for i in range(k)], 1, [[] for i in range(k)]
while not decoded:
    for elef in range(ele):
        for a,i in enumerate(li):
            lisT = flist.copy()
            tt, s, size1, runin = len(lisT[a]), lisT.remove(lisT[a]), sum([len(row) for row in lisT]), True
            if elef in i and size1 == elef:
                while runin: ele, s, s, runin = ele + 1, flist[a].append(ele), i.remove(elef), False if elef not in i else True
    if ele > n: decoded, s = True, print(flist)
'''

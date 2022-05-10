

n, li1, li2, out = int(input("Enter no. of weeks: ")), list(eval(input("~"))), list(eval(input("~"))), []
for i in range(len(li1)):
    for k in range(len(li2)):
        tli1, tli2 = li1.copy(), li2.copy()
        tli1[i], tli2[k] = tli2[k], tli1[i]
        if sum(tli1) == sum(tli2): out.append((li1[i],li2[k]))
print(out)




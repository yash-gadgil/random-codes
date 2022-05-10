
while 1:

    n = int(input("\n\nEnter the number to be achieved: "))
    li = [i for i in list(eval(input("Enter the numbers to be used in the sum: "))) if i <= n]
    d = {}
    
    for i in li:
        a = 0
        while 1:
            if i * a <= n:
                d[i] = a
                a += 1
            else:
                break
            
    #dict d of i gives the last of the multipliers of i not the multiples themselves
    #sets = set()
    li1 = [ 0 for i in li ]
    end = False
    while not end:
        for i in range(len(li1)):
            if li1[i] == d[li[i]]:
                li1[i] = 0
                try: li1[i + 1] = li1[i + 1] + 1
                except: pass
                '''
                for ele in range(len(li1)):
                    if li1[ele] != d[li[ele]]:
                        break
                else:
                    end = True
                '''
                if li1[len(li1) - 1] == d[li[len(li1) - 1]]: ## have to make sure every element in li1 is at its limit
                    end = True
                
        
        y = 0
        sums = ""
        #set_i = () #to make every sum unique using set
        for i in range(len(li1)):
            y += li1[i]*li[i]
            if li1[i] != 0:
                if sums != "" :
                    sums += " + "
                sums += str(li[i]) + " x " + str(li1[i])
                #set_i += (li[i] * li1[i],)
        sums += " = " + str(n)
        
        if y == n:# and set_i not in sets:
            print(sums)
            #sets.add(set_i)
        li1[0] += 1
        
## error: for n = 25 and x1,x2 = 5,6

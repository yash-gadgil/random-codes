
'''
var_holder = {}
 
for i in range(10):
    var_holder['my_var_' + str(i)] = "iterationNumber=="+str(i)
 
locals().update(var_holder)
 
print(my_var_4)


else:
        pos1=func.find("+")
        if pos1==-1:
            part1=func.partition("-")
            oper=oper+"p"
            xdegree1st=part1[0]
        elif pos1<neg1:
            part1=func.partition("+")
            oper=oper+"p"
            xdegree1st=part1[0]
        else:
            part1=func.partition("-")
            oper=oper+"p"
            xdegree1st=part1[0]
            
'''

import turtle

func=input("Enter a polynomial function: ")

var_holder = {}

neg1=func.find("-")
if neg1==0:
    coef1neg=func.partition("-")
    posfunc=coef1neg[2]
    numb1=posfunc.count("+")
    numb2=posfunc.count("-")
    terms=numb1+numb2+1
else:
    numb1=func.count("+")
    numb2=func.count("-")
    terms=numb1+numb2+1
    
dfunc=func
oper="0"
    
for i in range(terms):
    neg1=func.find("-")
    pos1=func.find("+")
    if neg1==0:
        coef1neg=func.partition("-")
        posfunc=coef1neg[2]
        neg_a_pos1=posfunc.find("+")
        neg_a_neg1=posfunc.find("-")
        if neg_a_neg1==-1:
            if neg_a_pos1==-1:
                oper=oper+"n"
                xdegree1st="-"+posfunc
            else:
                part1=posfunc.partition("+")
                oper=oper+"n"
                xdegree1st="-"+part1[0]
        elif neg_a_pos1==-1:
            part1=posfunc.partition("-")
            oper=oper+"n"
            xdegree1st="-"+part1[0]
        elif neg_a_pos1<neg_a_neg1:
            part1=posfunc.partition("+")
            oper=oper+"n"
            xdegree1st="-"+part1[0]
        else:
            part1=posfunc.partition("-")
            oper=oper+"n"
            xdegree1st="-"+part1[0]
    elif neg1==-1:
        if pos1==-1:
            oper=oper+"p"
            xdegree1st=func
        else:
            part1=func.partition("+")
            oper=oper+"p"
            xdegree1st=part1[0]
    elif pos1==0:
        coef1pos=func.partition("-")
        negfunc=coef1pos[2]
        pos_a_pos1=negfunc.find("+")
        pos_a_neg1=negfunc.find("-")
        if pos_a_neg1==-1:
            if pos_a_pos1==-1:
                oper=oper+"p"
                xdegree1st=negfunc
            else:
                part1=negfunc.partition("+")
                oper=oper+"p"
                xdegree1st=part1[0]
        elif pos_a_pos1==-1:
            part1=negfunc.partition("-")
            oper=oper+"p"
            xdegree1st=part1[0]
        elif pos_a_pos1<pos_a_neg1:
            part1=negfunc.partition("+")
            oper=oper+"p"
            xdegree1st=part1[0]
        else:
            part1=negfunc.partition("-")
            oper=oper+"p"
            xdegree1st=part1[0]
    else:
        if pos1==-1:
            part1=func.partition("-")
            oper=oper+"p"
            xdegree1st=part1[0]
        elif pos1<neg1:
            part1=func.partition("+")
            oper=oper+"p"
            xdegree1st=part1[0]
        else:
            part1=func.partition("-")
            oper=oper+"p"
            nextneg=True
            xdegree1st=part1[0]
    var_holder['term_no_' + str(i)] = xdegree1st
    if terms!=1 and i<terms:
        func=part1[1]+part1[2]
    elif i==terms:
        if nextneg==True:
            func="-"+part[2]
    else:
        break
locals().update(var_holder)

print(term_no_1)
print(oper)
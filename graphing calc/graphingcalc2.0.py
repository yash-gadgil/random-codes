
from turtle import *

func = input("Enter a polynomial function: ")

nums, terms = "1234567890", 0
exps, termcoeffs = [], []

for i in range(len(func)):

    if "x" in func:

        if func[i] == "x":

            try:

                if func[i + 1] == "^":

                    count = 2
                    exp = ""

                    while True:

                        try:

                            if func[i + count] in nums:

                                exp += func[i + count]

                                count += 1

                            else:

                                break
                    
                            exps.append(int(exp))

                        except:

                            exps.append(int(exp))

            except:

                print("y")
            
            termcoeff = func.partition("x")[0]

            if termcoeff != "":

                try:

                    termcoeffs.append(float(termcoeff))

                except:

                    print("Please enter numbers as the coefficients")
                    break
                
            else:

                termcoeffs.append(None)
                
            terms += 1
print(exps)

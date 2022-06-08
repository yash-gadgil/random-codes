
from turtle import *


func = input("\nEnter a polynomial function: ")

nums, redo = "1234567890", False
exps, termcoeffs = [], []

for i in range(len(func)):

    if "x" in func:

        if func[i] == "x":

            try:

                if func[i + 1] == "^":

                    count, exp = 2, ""

                    while True:

                        try:

                            if func[i + count] in nums:

                                exp += func[i + count]
                                count += 1

                            elif func[i + count] == ".":

                                print("Please enter exponents as integers")
                                redo = True
                                break

                            else:

                                try:

                                    exps.append(int(exp))
                                    break

                                except:

                                    exps.append("")
                                    break

                        except:

                             exps.append(int(exp))
                             break
                            
                else:

                    exps.append("")

            except:

                pass

            count, termcoeff = -1, ""

            while True:

                try:

                    if i + count < 0:

                        termcoeff = termcoeff[::-1]
                        termcoeffs.append(float(termcoeff))
                        break

                    if func[i + count] in nums or func[i + count] == ".":

                        termcoeff += func[i + count]
                        count -= 1

                    else:

                        termcoeff = termcoeff[::-1]
                        termcoeffs.append(float(termcoeff))
                        break

                except:

                    termcoeff = termcoeff[::-1]
                    termcoeffs.append(float(termcoeff))
                    break
                
        
            
print(termcoeffs)

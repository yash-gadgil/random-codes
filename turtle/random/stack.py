 

class stack:

    def __init__(self,li):
        self.li = li

    def push(self,ele):
        self.li.append(ele)

    def pop(self):
        return self.li.pop(-1)

    def display(self):
        print(self.li)

#f = stack([1,2,3,4,5])

f = stack(list('[' + input("Enter a list: ") + ']'))


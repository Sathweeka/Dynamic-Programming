'''
Implement two stacks uing one array
[]
s1.push(10)
s2.push(20)
'''
class Stack:
    def __init__(self,size):
        self.size = size
        self.top_1 = 0
        self.top_2 = self.size//2
        self.elements = [None]*size
    
    def push(self,stack,ele):
        if stack == 'one':
            if self.isfull('one')==False:
                self.elements[self.top_1] = ele
                self.top_1+=1
            elif self.isfull('one')==True and self.isfull('two')==False:
                self.elements[self.top_2] = ele
                self.top_2+=1
            else:
                return "Both Stacks Full"
        elif stack == 'two':
            if self.isfull('two')==False:
                self.elements[self.top_2] = ele
                self.top_2+=1
            elif self.isfull('two')==True and self.isfull('one')==False:
                self.elements[self.top_1] = ele
                self.top_1+=1
            else:
                return "Both Stacks Full"
    
    def isfull(self,stack):
        if stack=='one':
            if self.top_1>=(self.size//2):
                return True
            return False
        elif stack=='two':
            if self.top_2>=self.size:
                return True
            return False
    
    def isempty(self,stack):
        if stack == 'one':
            if self.top_1==0:
                return True
            return False
        elif stack == 'two':
            if self.top_2==len(self.elements)//2:
                return True
            return False
    
    def pop(self,stack):
        if stack=='one':
            if self.isempty('one')==True:
                return "Stack 1 Empty"
            else:
                ele = self.elements[self.top_1]
                self.top_1-=1
                return ele
        elif stack=='two':
            if self.isempty('two')==True:
                return "Stack 2 Empty"
            else:
                ele = self.elements[self.top_2]
                self.top_2-=1
                return ele
    def printstack(self,stack):
        if stack == 'one':
            return self.elements[:self.top_1]
        elif stack=='two':
            return self.elements[(self.size//2):self.top_2]
s = Stack(12)

s.push('one',1)
s.push('two',2)

s.printstack('one')

s.printstack('two')

s.push('one',4)
s.push('one',5)
s.push('one',6)
s.printstack('one')

s.pop('one')

s.printstack('one')

s.pop('two')

s.pop('two')

s.printstack('two')

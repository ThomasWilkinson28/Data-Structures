#I confirm that this submission is my own work and is consistent with the Queen's regulations on Academic Integrity

#Recursive function:
# def F(n):
#     if n >= 6:
#             F(n//3)
#             F(2*n//3)       
#     print (n, end=' ')

# data = [7, 18, 19, 22, 43]

# print("Using Recursive Function:")
# for n in data:
#     print("\nn = " + str(n) + ":")
#     F(n)

class Stack: 
    def __init__(self):
        self.data = [] * 10
        self.num_elements = 0

    def push(self, value) -> None:
        if len(self.data) > self.num_elements:
            self.data.append(value)
            self.num_elements += 1
        else:
            self.data = self.data + ([] * len(self.data))
            self.data.append(value)
            self.num_elements += 1
    
    def pop(self) -> int:
        self.num_elements =- 1
        return self.data.pop()

    def isEmpty(self) -> bool:
        return len(self.data) == 0

if __name__ == '__main__':
    data = [7, 18, 19, 22, 43]
    print("Using Non-Recursive Function")
    for n in data:
        print("\nn = " + str(n) + ":")

        s = Stack()
        s.push(n) 
        popped = [True]
        x = n


        while(not s.isEmpty()):
            temp = s.pop()
            x = temp
            s.push(temp)
            if x >= 6 and popped[-1]:
                popped[-1] = False
                s.push((x*2)//3)
                popped.append(True)
                s.push(x//3)
                popped.append(True)
            else:
                print(x, end = ' ')
                popped.pop()
                s.pop()
        




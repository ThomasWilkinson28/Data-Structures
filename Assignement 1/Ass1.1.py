#I confirm that this submission is my own work and is consistent with the Queen's regulations on Academic Integrity

#Recursive Function:
# def F(n):
#     if n > 1:
#         if n % 2 == 0:
#             F(n//2)
#         else:
#             F((3*n) + 1)       
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

        while(n > 1):
            if n % 2 == 0:
                n = n//2
                s.push(n)
            else:
                n = (n*3) + 1
                s.push(n)

        while(not s.isEmpty()):
            print(s.pop(), end = ' ')

        


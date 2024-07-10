#I confirm that this submission is my own work and is consistent with the Queen's regulations on Academic Integrity

#Recursive Function:
# def F(a,b):
#     if (a<=b):
#         m = (a+b)//2
#         F(a, m-1)
#         print (m, end = ' ')
#         F(m + 1, b)

# data = [(0,7), (1,18), (4,19), (-1,22)]

# print("Using Recursive Function:")
# for n in data:
#     print("\nn = " + str(n) + ":")
#     F(n[0], n[1])


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
    data = [(0,7), (1,18), (4,19), (-1,22)]
    print("Using Non-Recursive Function")
    for n in data:
        print("\nn = " + str(n) + ":")
        s = Stack()
        Popped = True
        s.push(n)    

        while(not s.isEmpty()):
            temp = s.pop()
            a = temp[0]
            if len(temp) > 1:
                b = temp[1]
                if a <= b:
                    m = (a + b)//2
                    s.push([m+1, b])
                    s.push([m])  
                    s.push([a, m-1])             
            elif len(temp) == 1:
                print(a, end = ' ')
 


        # while (not s.isEmpty()):
        #     if Popped == True:    
        #         temp = s.pop()
        #         a = temp[0]
        #         b = temp[1]
        #         s.push(temp)

        #         if a <= b:
        #             s.push((a, ((a + b)//2) - 1)) 
        #         else:
        #             s.pop() 
        #             Popped = False
        #             temp = s.pop()
        #             b = temp[1]
        #             a = temp[0]
        #             s.push(temp)
        #             print((a + b)//2, end = ' ')
        #             s.push((((a + b)//2) + 1, b))
                    
        #     else:
        #         temp = s.pop()
        #         b = temp[1]
        #         a = temp[0]
        #         s.push(temp)
        #         if a <= b:
        #             r = s.pop()
        #             s.pop()
        #             s.push(r)
        #             s.push((a, ((a + b)//2) - 1))
        #             Popped = True
        #         else:
        #             s.pop() 
        #             s.pop()
        #             temp = s.pop()
        #             b = temp[1]
        #             a = temp[0]
        #             print((a + b)//2, end = ' ')
        #             s.push((((a + b)//2) + 1, b))
        #             Popped = True

                


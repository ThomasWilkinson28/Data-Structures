#Thomas Wilkinson 20269155
#I confirm that this submission is my own work and is consistent with the Queen's regulations on Academic Integrity.

#Quadratic Hash Table
class QuadHashTable:
    def __init__(self):
        #Initialize Size of the table
        self.MAX = 2061
        #Create Array 
        self.arr = ['empty'] * self.MAX
        #Initialize Constants
        self.c1 = 3.25
        self.c2 = 1.5
        #Initialize Variables to count comparisons and inserted codenames
        self.totalComp = 0
        self.insertedCodenames = 0
    
    #h function which returns k modulus m
    def h(self, k):
        index = k % self.MAX
        return index
    
    #Converting the 7-8 letter words into a number using their ASCII codes
    def code_conv(self, code):
        c = 29
        code_count = 0
        for letter in code:
            code_count = ord(letter) + c*code_count
        return code_count
    
    #Insert function for the quad hash table
    def insert(self, codeword):
        i = 0
        comp = 0
        codeNum = self.code_conv(codeword)
        index = self.h(codeNum)
        while i < self.MAX:
            a = int((index + self.c1*i + self.c2*(i**2)) % self.MAX)
            if self.arr[a] == 'empty' or self.arr[a] == 'deleted': 
                self.arr[a] = codeword
                comp += 1
                self.insertedCodenames += 1
                self.totalComp += comp
                break
            elif self.arr[a] == codeword:
                print ("Attempt to insert duplicate key")
                comp += 1
                break
            else:
                i += 1
                comp += 1
        if (i == self.MAX):
            print("Table full, insert failed")

    #search function for the quad hash table
    def search(self, codeword):
        i = 0
        comp = 0
        codeNum = self.code_conv(codeword)
        index = self.h(codeNum)
        while i < self.MAX:
            a = int((index + self.c1*i + self.c2*i^2) % self.MAX)
            if self.arr[a] == 'empty':
                print("Codeword not found")
                comp += 1
                break
            elif self.arr[a] == codeword:
                comp += 1
                print(a)
                break
            else:
                i += 1
                comp += 1
        if (i == self.MAX):
            print("Codeword not found")    
    
    #delete function for the quad hash table
    def delete(self, codeword):
        i = 0
        comp = 0
        codeNum = self.code_conv(codeword)
        index = self.h(codeNum)
        while i < self.MAX:
            a = int((index + self.c1*i + self.c2*i^2) % self.MAX)
            if self.arr[a] == codeword:  
                self.arr[a] = "deleted"
                comp += 1
                break
            elif self.arr[a] == 'empty':
                print ("Codeword Not Found")
                comp += 1
                break
            else:
                i += 1
                comp += 1
        if (i == self.MAX):
            print("Delete failed, codeword not found")

#Double Hashing Hash Table
class DoubleHashTable:
    def __init__(self):
        #Initialize size of the table and create an array for it
        self.MAX = 2053
        self.arr = ['empty'] * self.MAX
        #Initialize variables for the total comparisons and total inserted codenames
        self.totalComp = 0
        self.insertedCodenames = 0
    
    #First hash function which returns k modulus of m
    def h1(self, k):
        index = k % self.MAX
        return index
    
    #Second hash function which uses the Multiplication Method
    def h2(self, k):
        v = 0.61803398875
        offset = self.MAX*((v*k) % 1)
        return int(offset)
    
    #Second hash function which uses the Linear Probing Method
    def h3(self, k):
        offset = (k + 1)% self.MAX
        return offset
    
    #Second hash function which uses the Mid-Square method
    def h4(self, k):
        offset = (k^2) % self.MAX
        return offset
     
    def code_conv(self, code):
        c = 2
        code_count = 0
        for letter in code:
            code_count = ord(letter) + c*code_count
        return code_count

    #Insert function for Double Hashing 
    def insert(self, codeword):
        i = 0
        comp = 0
        codeNum = self.code_conv(codeword)
        index = self.h1(codeNum)
        offset = self.h4(codeNum)
        while i < self.MAX:
            a = int((index + offset*i) % self.MAX)
            if self.arr[a] == 'empty' or self.arr[a] == 'deleted': 
                self.arr[a] = codeword
                comp += 1
                self.insertedCodenames += 1
                self.totalComp += comp
                break
            elif self.arr[a] == codeword:
                print ("Attempt to insert duplicate key")
                comp += 1
                break
            else:
                i += 1
                comp += 1
        if (i == self.MAX):
            i = 0
            print("Table full, insert failed")
            print(self.insertedCodenames) 

    #Search function for double hashing
    def search(self, codeword):
        i = 0
        comp = 0
        codeNum = self.code_conv(codeword)
        index = self.h1(codeNum)
        offset = self.h2(codeNum)
        while i < self.MAX:
            a = int((index + offset*i) % self.MAX)
            if self.arr[a] == 'empty':
                print("Codeword not found")
                comp += 1
                break
            elif self.arr[a] == codeword:
                comp += 1
                print(a)
                break
            else:
                i += 1
                comp += 1
        if (i == self.MAX):
            print("Codeword not found")    
    
    #Delete function for double hashing
    def delete(self, codeword):
        i = 0
        comp = 0
        codeNum = self.code_conv(codeword)
        index = self.h1(codeNum)
        offset = self.h2(codeNum)
        while i < self.MAX:
            a = int((index + offset*i) % self.MAX)
            if self.arr[a] == codeword:  
                self.arr[a] = "deleted"
                comp += 1
                break
            elif self.arr[a] == 'empty':
                print ("Codeword Not Found")
                comp += 1
                break
            else:
                i += 1
                comp += 1
        if (i == self.MAX):
            print("Delete failed, codeword not found")
    

import random
import string

#Function which creates random 7-8 letter "words"
def generate_codenames(num_codenames):
    codenames = []
    for _ in range(num_codenames):
        length = random.randint(7, 8)  # Random length between 7 and 8
        codename = ''.join(random.choices(string.ascii_uppercase, k=length))  # Random uppercase letters
        codenames.append(codename)
    return codenames

if __name__ == '__main__':
    num_codenames = 2000
    QH = QuadHashTable()
    DH = DoubleHashTable()
    codenames = generate_codenames(num_codenames)
    '''
    #For loop for double hashing
 for codename in codenames:
        DH.insert(codename)
    print("Table Size:", DH.MAX)
    print("Second Hash Function Used: Mid-Square Method")
    print(f"Number of Insertions: {DH.insertedCodenames}")
    print(f"Average Comparisons per Insertion: {(DH.totalComp/DH.insertedCodenames):.2f}")
    '''
    #For loop for quadratic probing
    for codename in codenames:
        QH.insert(codename)
    print("Table Size:", QH.MAX)
    print("C1 value=", QH.c1, ", C2 value=", QH.c2)
    print(f"Number of Insertions: {QH.insertedCodenames:.2f}")
    print(f"Average Comparisons per Insertion: {(QH.totalComp/QH.insertedCodenames):.2f}")
    

        

        

    
    
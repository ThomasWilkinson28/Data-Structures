#“I confirm that this submission is my own work and is consistent with the Queen's regulations on Academic Integrity.”

import random

class BST_Vertex():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Bin_Search_Tree():
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root is None:
            self.root = BST_Vertex(value)
        else:
            self.recursive_insert(self.root, value)

    def recursive_insert(self, vertex, value):    
        if value < vertex.value:
            if vertex.left is None:
                vertex.left = BST_Vertex(value)
            else:
                self.recursive_insert(vertex.left, value)
        elif value > vertex.value:
            if vertex.right is None:
                vertex.right = BST_Vertex(value)
            else:
                self.recursive_insert(vertex.right, value)
    
    def height(self):
        return self.recursive_height(self.root)
    
    def recursive_height(self, vertex):
        if vertex is None:
            return 0
        height_left = self.recursive_height(vertex.left)
        height_right = self.recursive_height(vertex.right)
        return 1 + max(height_left, height_right)
    
def random_permutation(n):
    permutation = list(range(1, n + 1))
    random.shuffle(permutation)
    return permutation

def average_height(n_values, num_trials):
    for n in n_values:
        total_heights = 0
        for _ in range(num_trials):
            permutation = random_permutation(n)
            bst = Bin_Search_Tree()
            for num in permutation:
                bst.insert(num)
            total_heights += bst.height()
        average_height = total_heights / num_trials
        print(f"When n = {n}, Average Height of Tree: {average_height:.2f}")

n_values = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
num_trials = 500

average_height(n_values, num_trials)

from collections import deque 

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self, idx):
        return  self.container[idx]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
    
    def get_index(self, char = str):
        for idx in range(0, len(self.container), 1):
            if char == self.container[idx]:
                return idx
            else: return False
    
if __name__ == "__main__":
    def reverse_string(str = str):
        str_stack = Stack()
        for letter in str:
            str_stack.push(letter)
        output = ""
        for letter in str: #while str_stack.size() != 0: 
            output += str_stack.pop()
        print(output)
    
    def is_balanced(str = str):
        stack = Stack()
        charset = [")", "]", "}", "(", "[", "{" ]
        closing_bracket_count = 0
        opening_bracket_count = 0
        for char in str:
            stack.push(char)
        while stack.size() != 0:
            popped_char = stack.pop()
            if popped_char == charset[0] or popped_char == charset[1] or popped_char == charset[2]: 
                closing_bracket_count+=1
            if popped_char == charset[3] or popped_char == charset[4] or popped_char == charset[5]:
                opening_bracket_count+=1 
        if closing_bracket_count == opening_bracket_count:
            return True 
        else: 
            return False
    
        




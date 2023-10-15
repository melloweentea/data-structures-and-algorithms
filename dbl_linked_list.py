# in progress 
class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Node(data, self.head, None) #next node is the old head
        self.head = new_node 

    def append(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return
        
        current = self.head
        while current.next: #while current is not null
            current = current.next
    
        current.next = Node(data, None, current) #since it is at the end of the list, next node is None 

    def print_forward(self):
        if self.head is None:
            print("linked list is empty")
            return
        
        current = self.head
        output = ""
        while current:
            output += str(current.data) + " --> "
            current = current.next
        
        output += "null"
        print(output)

    def print_backward(self):
        if self.head is None:
            print("linked list is empty")
            return
        current = self.head
        while current.next:
            current = current.next
        while current:
            output += str(current.data) + " --> "
            current = current.prev

        output += "null"
        print(output)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.append(data)

    def get_length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        
        return count 
    
    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("invalid index")
        
        if index==0:
            self.head = self.head.next #python automatically removes prev self.head

        count = 0
        current = self.head
        while current:
            if count == index - 1:
                current.next = current.next.next
                break 
            current = current.next
            count += 1
    
    def insert_at(self, index, data):
        if index<0 or index>=self.get_length():
            raise Exception("invalid index")
        
        if index==0:
            self.prepend(data)
            return 
        
        count = 0
        current = self.head
        while current:
            if count == index - 1:
                node = Node(data, current.next, current.prev)
                current.next = node
            current = current.next
            count += 1

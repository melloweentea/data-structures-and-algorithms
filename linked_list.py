class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next #pointer to the next element in the linked list

class LinkedList:
    def __init__(self):
        self.head = None #refers to the head of the linked list
        
    def prepend(self, data):
        new_node = Node(data, self.head) #next node is the old head
        self.head = new_node 

    def append(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        current = self.head
        while current.next: #while current is not null
            current = current.next
    
        current.next = Node(data, None) #since it is at the end of the list, next node is None 

    def print_list(self):
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
                node = Node(data, current.next)
                current.next = node
            current = current.next
            count += 1

    #exercise
    def insert_after_value(self, data_after, data_to_insert):
        count = 0 
        current = self.head
        while current:
            if current.data == data_after: #rmb to call attribute data 
                node = Node(data_to_insert, current.next)
                current.next = node
            current = current.next
            count += 1

    def remove_by_value(self, data):
        count = 0
        current = self.head
        while current:
            last_node = current 
            if current.data == data and count == 0:
                self.head = self.head.next 
                break 
            elif current.data == data:
                last_node.next = last_node.next.next
                break 
            current = current.next
            count += 1
        
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_values(["banana", "mango", "grapes", "oranges"])
    ll.print_list()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print_list()
    ll.remove_by_value("banana")
    ll.print_list()
    ll.remove_by_value("grapes")
    ll.print_list()


class Node:
    def __init__(self, data=None):
            self.data = data
            self.next_node = None
            
class LinkedList:
    def __init__(self):
        self.head = None
        self.num_of_head = 0
        
    def insert(self, data=None):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            tail = self.get_last()
            tail.next_node = new_node
        self.num_of_head += 1
        
    def delete(self, data):
        current = self.head
        pre_node = self.head
        while(current != None ):
            if current.data == data:
                if current == self.head:
                    self.head = current.next_node
            else:
                pre_node.next_node = current.next_node
                
            pre_node = current 
            current = current.next_node
        self.num_of_head -= 1
        
    def search(self, data):
        current = self.head
        while(current != None):
            if current.data == data:
                return current
            else:
                current = current.next_node
    
    def get_last(self):
        current = self.head
        if self.head == None:
            return None
        else:
            while(current.next_node != None):
                current = current.next_node
            return current
    
link = LinkedList()
link.insert(1)
link.insert(2)
link.insert(3)
link.search(2).data
link.delete(3)
link.search(3).data

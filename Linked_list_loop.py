class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None
class LinkedList:
    def __init__(self):
        self.start_node = None
    def traverse_list(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item , " ")
                n = n.ref
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n=self.start_node
        while n.ref is not None:
            n = n.ref
        n.ref = new_node
    def FindCyclePresentOrNot(self):
        ptr1 = self.start_node
        ptr2 = self.start_node
        
        while ptr2.ref.ref is not None:
            ptr2 = ptr2.ref.ref
            ptr1 = ptr1.ref
            if(ptr2 == ptr1):
                print("Cycle found at", ptr1.item)
                return ptr1
        return None
    
    def findMeetingPoint(self, ptr):
        if(ptr == None):
            print("No cycle Found!")
            return
        start = self.start_node
        while start!=ptr:
            ptr = ptr.ref
            start = start.ref
        print("Cycle started At", ptr.item)
        
    def removeCycle(self, ptr):
        if(ptr == None):
            print("No cycle Found!")
            return
        start = self.start_node
        while start.ref!=ptr.ref:
            ptr = ptr.ref
            start = start.ref
        ptr.ref = None
        print("Cycle Removed!")
new_linked_list = LinkedList()
new_linked_list.insert_at_end(1)
new_linked_list.insert_at_end(2)
new_linked_list.insert_at_end(3)
new_linked_list.insert_at_end(4)
new_linked_list.insert_at_end(5)
new_linked_list.insert_at_end(8)
new_linked_list.insert_at_end(7)
new_linked_list.insert_at_end(6)
new_linked_list.start_node.ref.ref.ref.ref.ref.ref.ref = new_linked_list.start_node.ref.ref
ptr = new_linked_list.FindCyclePresentOrNot()
new_linked_list.findMeetingPoint(ptr)
print()
new_linked_list.removeCycle(ptr)
print()
new_linked_list.traverse_list()

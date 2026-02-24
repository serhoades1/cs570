class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        
        new_node.next = self.head
        self.head = new_node

    def delete_with_value(self, data):
        if not self.head:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node:
            elems.append(cur_node.data)
            cur_node = cur_node.next
        print(" -> ".join(map(str, elems)))

if __name__ == "__main__":
    ll = LinkedList()
    
    ll.append(10)
    ll.append(20)
    ll.append(30)
    print("Initial list:")
    ll.display()

    ll.prepend(5)
    print("After prepending 5:")
    ll.display()

    ll.delete_with_value(20)
    print("After deleting 20:")
    ll.display()
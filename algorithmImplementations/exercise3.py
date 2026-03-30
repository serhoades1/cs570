class List:
    def __init__(self, data):
        self.data = data
        self.next = None

def listLen(head, List): # Helper function to get the length of the list
    temp = List.head
    index = 0

    while(temp):
        index += 1
        temp = temp.next
    return index
    
def swapNodes(head, List):
    curNode = head
    temp = List(5)

    for i in range (0, listLen(node1, List) - 1):
        if (i % 2 == 0 and i < listLen(node1, List) - 2): # Checks even nodes that have a valid note succeeding it

            temp = curNode # Swaps the current node and its following node
            curNode = curNode.next
            curNode.next = temp

        curNode = curNode.next # Skips both nodes that were just swapped
        curNode = curNode.next
        i += 1 # Acts as an index to make sure swaps are still possible
    return List

    
# node1 = List(1)
# node2 = List(2)
# node3 = List(3)
# node4 = List(4)

node1 = List(3)
node2 = List(1)
node3 = List(4)
node4 = List(1)
node5 = List(5)

print(swapNodes(node1, List))
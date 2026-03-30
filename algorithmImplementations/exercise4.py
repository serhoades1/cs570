class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        newAdd = ListNode(data)

        if not self.head: #If no node exists, make it the head
            self.head = newAdd
            return
        
        finNode = self.head
        while finNode.next: #While the following node exists (checks to see if final node)
            finNode = finNode.next

        finNode.next = newAdd
    
    def printList(self):
        totList = []
        current = self.head
        while current:
            totList.append(current.val) #Concatenates entire list
            current = current.next

        print(", ".join(map(str, totList)))

    def insertionSort(self):
        sorted = LinkedList() #New list created
        current = self.head
        newList = sorted.head

        while current: #Continues until the unsorted list has reached its end
            while newList:
                if newList.next > current: #Runs until it finds the first node with a value greater than itself and places itself right before it
                    temp = newList.next
                    newList.next = current
                    newList.next = temp

            current = current.next
        return sorted



newList = LinkedList()
# newList.append(4)
# newList.append(2)
# newList.append(1)
# newList.append(3)

newList.append(4)
newList.append(7)
newList.append(3)
newList.append(9)

newList.printList()

newList.insertionSort()
newList.printList()
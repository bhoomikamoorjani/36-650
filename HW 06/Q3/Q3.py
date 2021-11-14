#Question 3 and 5 

class linkedListNode:
    def __init__(self, value, nextNode = None):
        self.value = value
        self.nextNode = nextNode

class linkedList:
    def __init__(self, head = None):
        self.head = head 
        
    def insert(self, value):
        node = linkedListNode(value)
        if self.head is None:
            self.ad = node
            return
        else:
            currentNode = self.head
            while True:
                if currentNode.nextNode is None:
                    currentNode.nextNode = node
                    break
                currentNode = currentNode.nextNode 
                
    def printlinkedList(self):
        currentNode = self.head
        while currentNode is not None:
            print (currentNode.value, "->", end = " ")
            currentNode = currentNode.nextNode
        print ("None")
        
    def sortlinkedList(self):
        temp = []
        currentNode = self.head
        while currentNode is not None:
            temp.append(currentNode.value)
            currentNode = currentNode.nextNode
        final_list = self.selection_sort(temp)
        currentNode = self.head
        i=0
        while currentNode is not None:
            currentNode.value = temp[i]
            currentNode = currentNode.nextNode
            i=i+1
        
     
    def selection_sort(self, list_to_be_sorted):
        for i in range(len(list_to_be_sorted)):
            min_idx = i
            for j in range(i+1, len(list_to_be_sorted)):
                if list_to_be_sorted[min_idx] > list_to_be_sorted[j]:
                    min_idx = j
            tmp = list_to_be_sorted[i]
            list_to_be_sorted[i] = list_to_be_sorted[min_idx] 
            list_to_be_sorted[min_idx] = tmp
        return list_to_be_sorted
    
    def removeDuplicates(self):
        self.sortlinkedList()
        temp = self.head
        while temp.nextNode.nextNode:
            if temp.nextNode.value == temp.value:
                temp.nextNode = temp.nextNode.nextNode
            temp = temp.nextNode
        if temp.nextNode.nextNode is None:
            if temp.nextNode.value == temp.value:
                temp.nextNode = None

#Test Case - Q3 

first_node = linkedListNode(11)
linked_list = linkedList(first_node)
linked_list.insert(3)
linked_list.insert(6)
linked_list.printlinkedList()

linked_list.sortlinkedList()
linked_list.printlinkedList()


#Test Case - Q5

first_node = linkedListNode(11)
linked_list = linkedList(first_node)
linked_list.insert(3)
linked_list.insert(6)
linked_list.insert(3)
linked_list.insert(11)
linked_list.insert(6)
linked_list.insert(5)
linked_list.insert(7)
linked_list.insert(5)
linked_list.printlinkedList()

linked_list.removeDuplicates()

linked_list.printlinkedList()


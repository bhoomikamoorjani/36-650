#Question 6 

class ReversedLinkedListNode(object):
    def __init__(self, value, previousNode = None):
        self.value = value 
        self.previousNode = previousNode
        
class ReversedLinkedList(object):
    def __init__(self, tail = None):
        self.tail = tail
    
    def insert(self, value):
        new_node = ReversedLinkedListNode(value)
        old_tail = self.tail 
        self.tail = new_node
        self.tail.previousNode = old_tail
            
    def printReversedLinkedList(self):
        currentNode = self.tail
        while currentNode is not None:
            print(currentNode.value, "->", end = " ")
            currentNode = currentNode.previousNode
        print ("None")
    
    def delete(self,value):
        if not self.tail:
            return 
        
        temp = self.tail 
        
        if self.tail.value == value:
            print(str(self.tail.value))
            return
        
        while temp.previousNode is not None:
            if temp.previousNode.value == value:
                print(str(temp.previousNode.value))
                temp.previousNode = temp.previousNode.previousNode 
                return
            temp = temp.previousNode
        return
    
    def search(self, value):
        temp = self.tail 
        while temp is not None:
            if temp.value == value:
                return True
            return False
            temp = temp.previousNode 

#Test Case

first_node = ReversedLinkedListNode(11)
linked_list = ReversedLinkedList(first_node)
linked_list.insert(3)
linked_list.insert(6)
linked_list.insert(5)

linked_list.printReversedLinkedList()
linked_list.delete(6)
linked_list.printReversedLinkedList()

print(linked_list.search(5))

print(linked_list.search(17))

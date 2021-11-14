class Node:
    def __init__(self, data):
        self.data = data 
        self.small = None
        self.big = None 
        self.toobig = None
        
    def insert(self, data):
        if self.data:
            if data-self.data <0:
                if self.small is None:
                    self.small = Node(data)
                else:
                    self.small.insert(data)
            elif data-self.data <10 and data-self.data>=0:
                if self.big is None:
                    self.big = Node(data)
                else:
                    self.big.insert(data)
            elif data-self.data >= 10:
                if self.toobig is None:
                    self.toobig = Node(data)
                else:
                    self.toobig.insert(data)
        else:
            self.data = data
            
    def traversal_print(self):
        if self.small:
            self.small.traversal_print()
        print(self.data)
        if self.big:
            self.big.traversal_print()
        if self.toobig:
            self.toobig.traversal_print()
            
    def traversal_list(self,temp):
        if self.small:
            self.small.traversal_list(temp)
        temp.append(self.data)
        if self.big:
            self.big.traversal_list(temp)
        if self.toobig:
            self.toobig.traversal_list(temp)
        return temp
    
    def delete(self, data):
        temp2 = []
        temp2 = self.traversal_list(temp2)
        temp2.remove(data)
        self.samll = None
        self.big = None
        self.toobig = None
        self.data = None
        
        for x in temp2:
            self.insert(x)

#Test Case

root = Node(20)
root.insert(40)
root.insert(45)
root.insert(32)

root.traversal_print()

root.delete(45)

root.traversal_print()


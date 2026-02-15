class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# original list
n1 = Node(5)
n2 = Node(15)
n3 = Node(25)
n4 = Node(35)

n1.next = n2
n2.next = n3
n3.next = n4

head = n1


new = Node(1)
new.next = head
head = new


end = Node(50)
temp = head

while temp.next != None:
    temp = temp.next

temp.next = end  

a=None
temp = head
while temp != None:
     if temp.data==15:
         a.next=temp.next
         break
     
     print(temp.data)
     temp = temp.next
    

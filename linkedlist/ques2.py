class Node:
    def __init__(self,data):
        
     self.data=data
     self.next=next
     
n1=Node(50)
n2=Node(100)
n3=Node(150)

n1.next=n2
n2.next=n3    
n=100
head=n1
temp=head
prev=None
while(temp!=None):
    if(temp.data>n):
        prev=temp.next
        break
    print(temp.data,end="->") 
    prev=temp
    temp=temp.next
     
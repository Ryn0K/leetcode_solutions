class Node:
    "Define constructor"
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

class Solution:
    def printList(self,l):
        "Define function to print Linked List"
        value = []
        while(l):
            value.append(l.val)
            l=l.next
        print(list((value)))

    def addTwoNumbers(self, l1, l2):
        sum = l1.val + l2.val
        carry = int(sum / 10)
    
        l3 = Node(sum%10)
        p1 = l1.next
        p2 = l2.next
        p3 = l3
        while(p1 != None or p2 != None):
            sum = carry + ( p1.val if p1 else 0) + ( p2.val if p2 else 0)
            carry = int(sum/10)
            p3.next = Node(sum % 10)
            p3 = p3.next
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
    
        if(carry > 0):
            p3.next = Node(carry)
    
        return l3


if __name__ == "__main__":
    s=Solution()
    l1 = Node(2,Node(4,Node(3)))
    l2 = Node(5,Node(6,Node(4)))
    #print("This is 1st Linked List.")
    #s.printList(l1)
    #print("This is 2nd Linked List")
    #s.printList(l2)
    s.printList(s.addTwoNumbers(l1,l2))


        
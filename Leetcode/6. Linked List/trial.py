class Node:
    def __init__(self, val=None, next=None) -> None:
        self.val = val
        self.next = None


n1 = Node(100)
n2 = Node(200)
n3 = Node(50)
n1.next = n2
n2.next = n3
print(n1.val)
print(n1.next.val)
print(n1.next.next.val)

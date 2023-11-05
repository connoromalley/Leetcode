@dataclass
class ListNode:
    val: int
    next: Optional['ListNode'] = None

# Create individual nodes
node1 = ListNode(2)
node2 = ListNode(4)
node3 = ListNode(3)

# Link the nodes together to form a linked list
node1.next = node2
node2.next = node3

# Now, node1 represents the head of the linked list
head = node1

# To access the elements of the linked list, you can iterate through it
current = head
while current is not None:
    print(current.val)
    current = current.next

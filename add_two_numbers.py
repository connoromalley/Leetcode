from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummyHead = ListNode(0)
    tail = dummyHead
    carry = 0

    while l1 is not None or l2 is not None or carry != 0:
        digit1 = l1.val if l1 is not None else 0
        digit2 = l2.val

        sum = digit1 + digit2 + carry
        digit = sum % 10
        carry = sum // 10

        newNode = ListNode(digit)
        tail.next = newNode
        tail = tail.next

        l1 = l1.next if l1 is not None else None
        l2 = l2.next if l2 is not None else None

    result = dummyHead.next
    dummyHead.next = None
    return result
    
# see the code work using sample data

l1 = ListNode(3)
l1.next = ListNode(5)
l1.next.next = ListNode(2)

l2 = ListNode(8)
l2.next = ListNode(3)
l2.next.next = ListNode(1)

result = addTwoNumbers(l1, l2)

# Print the result (linked list)
while result is not None:
    print(result.val, end=" -> ")
    result = result.next

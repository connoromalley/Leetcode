from typing import Optional
from dataclasses import dataclass

@dataclass
class ListNode:
    val: int
    next: Optional['ListNode'] = None

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)
    cur = dummy
    carry = 0
    
    while l1 is not None or l2 is not None or carry:
        v1 = l1.val if l1 is not None else 0
        v2 = l2.val if l2 is not None else 0

        val = v1 + v2 + carry
        carry = val // 10
        val = val % 10

        cur.next = ListNode(val)
        cur = cur.next

        if l1 is not None:
            l1 = l1.next
        if l2 is not None:
            l2 = l2.next
    
    return dummy.next

# Define the ListNode class and addTwoNumbers function here (as in your previous code).

# Helper function to convert a list to a linked list of ListNode instances
def list_to_linked_list(lst):
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper function to convert a linked list to a list
def linked_list_to_list(head):
    result = []
    while head is not None:
        result.append(head.val)
        head = head.next
    return result

# Example usage and testing
l1 = list_to_linked_list([2, 4, 3])
l2 = list_to_linked_list([5, 6, 4])

result = addTwoNumbers(l1, l2)
print("Input List 1:", linked_list_to_list(l1))
print("Input List 2:", linked_list_to_list(l2))
print("Result:", linked_list_to_list(result))

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node to handle edge cases where the head needs to be removed
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy

        # Move the first pointer ahead by n nodes
        for _ in range(n + 1):
            first = first.next

        # Move both pointers until the first pointer reaches the end
        while first is not None:
            first = first.next
            second = second.next

        # Remove the nth node from the end
        second.next = second.next.next

        return dummy.next

# Helper function to print the linked list
def printList(head: ListNode):
    curr = head
    while curr is not None:
        print(curr.val, end=" ")
        curr = curr.next
    print()

# Example usage
if __name__ == "__main__":
    # Create the linked list: [1,2,3,4,5]
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    sol = Solution()
    n = 2
    new_head = sol.removeNthFromEnd(head, n)

    # Print the modified linked list
    printList(new_head)  # Output: [1,2,3,5]

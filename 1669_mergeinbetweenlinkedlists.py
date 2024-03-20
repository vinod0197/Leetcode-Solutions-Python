# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = list1
        prev_a = dummy
        for _ in range(a):
            prev_a = prev_a.next
        node_b = prev_a.next
        for _ in range(a, b+1):
            node_b = node_b.next

        prev_a.next = list2
        list2_end = list2
        while list2_end.next is not None:
            list2_end = list2_end.next
        list2_end.next = node_b

        return dummy.next

# Helper function to print the linked list
def print_list(head: ListNode):
    curr = head
    while curr is not None:
        print(curr.val, end=" ")
        curr = curr.next
    print()

# Example usage
if __name__ == "__main__":
    # Create list1: [10,1,13,6,9,5]
    list1 = ListNode(10)
    list1.next = ListNode(1)
    list1.next.next = ListNode(13)
    list1.next.next.next = ListNode(6)
    list1.next.next.next.next = ListNode(9)
    list1.next.next.next.next.next = ListNode(5)

    # Create list2: [1000000,1000001,1000002]
    list2 = ListNode(1000000)
    list2.next = ListNode(1000001)
    list2.next.next = ListNode(1000002)

    sol = Solution()
    merged_list = sol.mergeInBetween(list1, 3, 4, list2)

    # Print the merged list
    print_list(merged_list)

# Definition for singly-linked list.
# class ListNode:
#     def _init_(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # Create a dummy node to serve as the head of the result linked list
        current = dummy  # Pointer to traverse the result linked list
        carry = 0  # Variable to store the carry
        # Iterate through both linked lists
        while l1 or l2 or carry:
            # Calculate the sum of current digits and the carry
            sum_val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = sum_val // 10  # Update the carry
            # Create a new node with the sum value
            current.next = ListNode(sum_val % 10)
            current = current.next  # Move the pointer to the next node
            # Move to the next nodes in both linked lists if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next  # Return the head of the result linked list

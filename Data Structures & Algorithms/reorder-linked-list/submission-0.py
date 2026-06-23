# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
        #find the midpoint
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #slow pointer to null and uppdate the head2
        head2 = slow.next
        slow.next = None

        #reverse the head2 part
        Dummy = ListNode()
        prev,tail = None,head2
        while tail:
            nxt = tail.next
            tail.next = prev
            prev = tail
            tail = nxt

        #similar to sorting 2 LL, pick one from each and connect it
        #one side we have head and another side we have prev
        curr = head
        flag = True
        
        while curr and prev:
            # Save BOTH next states at the start so we never lose them when altering links
            nxt1 = curr.next
            nxt2 = prev.next
            
            if flag:
                curr.next = prev
                curr = nxt1       # Move curr to its next structural position
                flag = False      # Switch to the other list
            else:
                prev.next = curr  # Link the second half node back to the active first half node
                prev = nxt2       # Move prev to its next structural position
                flag = True       # Switch back to the first list


        # curr = head
        # while prev:  # The right half (prev) is always shorter or equal in length
        #     # Save the next nodes for both halves before mutating links
        #     nxt1 = curr.next
        #     nxt2 = prev.next
            
        #     # Connect left node to right node
        #     curr.next = prev
        #     # Connect right node to the saved next left node
        #     prev.next = nxt1
            
        #     # Step both pointers forward to their saved tracking states
        #     curr = nxt1
        #     prev = nxt2


        
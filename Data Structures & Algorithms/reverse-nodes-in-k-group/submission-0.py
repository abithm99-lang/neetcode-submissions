# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]: 
        #iterate that many times and each iteration has 3 nodes
        #get the prev of node0 and next of nodek once reversed connect it
        Dummy = ListNode(0,head)
        groupPrev = Dummy
        while True:
            kth = self.getKthnode(groupPrev,k)
            if not kth:
                break

            groupNxt = kth.next

            curr = groupPrev.next
            new_head,new_tail = self.reverseNode(curr,k)

            groupPrev.next, new_tail.next = new_head , groupNxt

            groupPrev = new_tail

        return Dummy.next

    def reverseNode(self, head: Optional[ListNode], k: int):

        prev = None
        curr = head
        
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev, head

        
    
    def getKthnode(self, head: Optional[ListNode], k: int):
        while head and k > 0:
            head = head.next
            k -= 1
        return head

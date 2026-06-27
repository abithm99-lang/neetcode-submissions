# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        while len(lists) > 1:
            
            next_round_list = []
            n = len(lists)
            for i in range(n - 1, -1, -2):
                list1 = lists[i]
                list2 = lists[i-1] if (i - 1) >= 0 else None

                merged = self.merge2List(list1,list2)
                next_round_list.append(merged)

            lists = next_round_list
        
        return lists[0]



    def merge2List(self, l1: ListNode = None, l2: ListNode = None):
        if not l1: return l2
        if not l2: return l1
        Dummy = ListNode()
        curr = Dummy

        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next 
        
        curr.next = l1 if l1 else l2

        return Dummy.next
        
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: [ListNode]) -> ListNode:
        if not lists:
            return None
        span = 1
        while span < len(lists):
            for i in range(0, len(lists) - span, span * 2):
                lists[i] = self.mergeTwoLists(lists[i], lists[i + span])
            span *= 2
        return lists[0]

    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        result_list = current_result = ListNode(0)   # 结果链头节点

        while bool(list1) and bool(list2):
            if list1.val <= list2.val:
                current_result.next = list1
                list1 = list1.next
            else:
                current_result.next = list2
                list2 = list2.next
            current_result = current_result.next
        if bool(list1):
            current_result.next = list1
        if bool(list2):
            current_result.next = list2

        return result_list.next

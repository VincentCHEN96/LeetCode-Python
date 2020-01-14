# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 处理空链情况或确定结果链头节点
        if not l1:
            return l2
        elif not l2:
            return l1
        elif l1.val <= l2.val:
            result = l1 # 结果链头节点
            l1 = l1.next
        else:
            result = l2 # 结果链头节点
            l2 = l2.next
        result.next = None
        current_node = result

        # 完成结果链
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                current_node.next = l1
                l1 = l1.next
            else:
                current_node.next = l2
                l2 = l2.next
            current_node = current_node.next
        if l1 != None:
            current_node.next = l1
        if l2 != None:
            current_node.next = l2

        return result

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = current_node = ListNode(-1)
        carry = 0

        while l1 != None or l2 != None:
            bit_num_1 = bit_num_2 = 0
            if l1 != None:
                bit_num_1 = l1.val
            if l2 != None:
                bit_num_2 = l2.val
            bit_sum = bit_num_1 + bit_num_2 + carry
            carry = int(bit_sum / 10)
            current_node.next = ListNode(bit_sum % 10)
            current_node = current_node.next
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
        if carry != 0:
            current_node.next = ListNode(carry)

        return result.next

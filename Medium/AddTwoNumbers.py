from typing import List





class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        "Deneme"
# def list_to_node(l: List[int]) -> ListNode:
#     if not l:
#         return None
#     head = ListNode(l[0])
#     curr = head
#     for val in l[1:]:
#         curr.next = ListNode(val)
#         curr = curr.next
#     return head

# class Solution:
#     def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
#         results=[]
#         l1_reverse=l1.reverse()
#         l2_reverse=l2.reverse()
#         str_l1=""
#         str_l2=""
#         for i in l1:
#             str_l1=str_l1+str(i)
#         for i in l2:
#             str_l2=str_l2+str(i)
#         result=str(int(str_l1)+int(str_l2))
#         for i in result:
#             results.append(i)
#         results.reverse()
#         return print(results)
"İlkel çözüm xd"


class Solution:
    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            digit_sum = x + y + carry
            carry = digit_sum // 10
            current.next = ListNode(digit_sum % 10)
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next










# l1 = [9,9,9,9,9,9,9]
# l2 = [9,9,9,9]
# l1_node=list_to_node(l1)
# l2_node=list_to_node(l2)
#
# solu=Solution()
# solu.addTwoNumbers(l1_node,l2_node)
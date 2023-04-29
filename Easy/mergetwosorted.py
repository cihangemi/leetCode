from typing import List


class Solution:
    def mergeTwoLists(self, list1: List[int], list2: List[int]) -> List[int]:
        output=[]
        for i in list1:
            output.append(i)
        for j in list2:
            if len(list2) == len(output)-len(list1):
                pass
            else:
                output.append(j)
        output.sort()
        return print(output)


list1 = [1,2,4]
list2 = [1,3,4]

y=Solution()
y.mergeTwoLists(list1,list2)

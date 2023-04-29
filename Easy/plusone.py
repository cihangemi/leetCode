from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        y=""
        list = []
        for i in  digits:
            a=str(i)
            y=y+a
        t=str(int(y)+1)
        for i in t:
            list.append(i)
        return    print(list)


digits = [9]
sev=Solution()
sev.plusOne(digits)
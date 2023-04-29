from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        for i in range(len(nums)):
            if val in nums:
                nums.remove(val)
        k=len(nums)

        return print(k,nums)



nums=[3,3]
val= 3
d=Solution()
d.removeElement(nums,val)


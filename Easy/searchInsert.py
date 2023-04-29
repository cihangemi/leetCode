from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        self.nums=nums
        self.target=target
        for i in nums:
            if target == i:
                print(i)

            for i in nums:
                if target != i:
                    nums.append(target)
                    nums.sort()

                    break
            break
        return print(self.nums.index(target))



nums=[1 ,3 ,5 ,6]
target =int(5)

a=Solution()
a.searchInsert(nums,target)


# for i in nums:
#     if target <i:
#         nums.append(target)
#         nums.sort()
#         print(nums)
#         break

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            prev_1 = 1
            prev_2 = 2
            for i in range(3, n+1):
                current = prev_1 + prev_2
                prev_1 = prev_2
                prev_2 = current
            return current


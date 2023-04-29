class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        j=int

        y=s.strip()
        y=" ".join(y.split())
        i=y.rfind(" ")
        j=len(y)-1
        return  print( j-i)


s = "luffy is still joyboy"
a=Solution()
a.lengthOfLastWord(s)







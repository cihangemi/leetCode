class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        if len(a) > len(b):
            b = b.ljust(len(a), '0')
        else:
            a = a.ljust(len(b), '0')

        carry = 0
        result = ""
        for i in range(len(a)):
            bit_sum = int(a[i]) + int(b[i]) + carry
            result += str(bit_sum % 2)
            carry = bit_sum // 2

        if carry == 1:
            result += '1'

        return result[::-1]
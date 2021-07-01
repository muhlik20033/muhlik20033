class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = str(n)
        a = 0
        b = 1
        for i in s:
            a += int(i)
            b *= int(i)
            
        return b-a

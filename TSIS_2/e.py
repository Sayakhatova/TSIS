class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum=0
        mult=1
        for i in str(n):
            sum+=int(i)
            mult*=int(i)
        return mult-sum
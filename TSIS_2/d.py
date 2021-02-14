#https://leetcode.com/problems/find-the-highest-altitude/submissions/
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res=0
        height=0
        for i in gain:
            height += i
            if height>res:
                res=height
        return res
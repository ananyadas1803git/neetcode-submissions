class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            d[i]=d.get(i,0)+1 #count for value of i appearing in nums
        for key,val in d.items():
            if val == 1:
                return key
        return -1
        
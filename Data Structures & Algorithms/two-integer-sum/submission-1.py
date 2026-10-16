class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list_c =[(nums[indx],indx) for indx in range(len(nums))]
        list_c.sort()
        i = 0
        j = len(list_c)-1
        while i<j:
            sum = list_c[i][0]+list_c[j][0]
            if sum < target:
                i+=1
            elif sum > target:
                j-=1
            else:
                return sorted([list_c[i][1],list_c[j][1]])
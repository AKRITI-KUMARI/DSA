class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        d = {}
        for i in range(len(nums)):
            second = target - nums[i]
            if second in d:
                ans.append(i) 
                ans.append(d[second])
                break
            else:
                d[nums[i]] = i
        return ans
  
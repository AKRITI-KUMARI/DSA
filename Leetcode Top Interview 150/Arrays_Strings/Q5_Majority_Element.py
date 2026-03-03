class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        majority_count = 0
        majority_element = nums[0]

        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1
            
            if d[nums[i]] > majority_count:
                majority_count = d[nums[i]]
                majority_element = nums[i]
        
        return majority_element
  
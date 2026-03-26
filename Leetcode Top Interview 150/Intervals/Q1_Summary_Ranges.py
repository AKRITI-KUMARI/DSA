class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return nums
        ans = []
        a = b = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]+1:
                b = nums[i]
            else:
                if a == b:
                    ans.append(str(a))
                else:
                    s = str(a)+"->"+str(b)
                    ans.append(s)
                a = b = nums[i]
        if a == b:
            ans.append(str(a))
        else:
            s = str(a)+"->"+str(b)
            ans.append(s)
        return ans
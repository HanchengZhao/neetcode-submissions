class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # use hashset
        used = set()

        if len(nums) <= 1:
            return False
        for n in nums:
            if n not in used:
                used.add(n)
            else:
                return True
        return False


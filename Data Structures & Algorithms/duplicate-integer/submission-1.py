class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for i in nums:
            if i in hashmap:
                # If we find it, it's a duplicate. Stop and return True.
                return True
            else:
                # If we don't find it, record it. The value (1) doesn't matter.
                hashmap[i] = 1
                
        # If the loop finishes without returning, no duplicates were found.
        return False
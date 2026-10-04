class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        
        for item in nums:
            # Are we at the start of a sequence?
            if (item - 1) not in num_set:
                current_num = item
                current_streak = 1  
                # Look ahead to see how far the chain goes
                while (current_num + 1) in num_set:
                    current_num += 1
                    current_streak += 1 
                # Save the maximum length we've found so far
                longest = max(longest, current_streak)
        return longest

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0 
        # 1. XOR all the numbers currently in the array
        for num in nums:
            ans ^= num
        # 2. XOR all the numbers from 0 up to n (where n is len(nums))
        for i in range(len(nums) + 1):
            ans ^= i
        return ans
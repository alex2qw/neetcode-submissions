class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}

        # 1. Count frequencies safely using .get()
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
            
        # 2. Sort the dictionary items by 
        #their counts (values) in descending   order
        sorted_nums = sorted(seen.items(), key=lambda x: x[1], reverse=True)
        
        # 3. Grab just the keys (the numbers) for the top 'k' elements
        return [item[0] for item in sorted_nums[:k]]

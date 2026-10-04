class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
        seen = {}
        for item in strs:
            sort = "".join(sorted(item))
            if sort not in seen:
                seen[sort] = [item]   # Create a new list with this word
            else:
                seen[sort].append(item) # Add it to the existing group
        return list(seen.values())

                
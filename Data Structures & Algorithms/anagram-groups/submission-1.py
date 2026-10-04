class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
        seen = {}
        for i in strs:
            sort = "".join(sorted(i))
            if sort not in seen:
                seen[sort] = [i]   # Create a new list with this word
            else:
                seen[sort].append(i) # Add it to the existing group
        return list(seen.values())

                
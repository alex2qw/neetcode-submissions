class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
        seen = {}
        for i in range(len(strs)):
            sort = "".join(sorted(strs[i]))
            if sort not in seen:
                seen[sort] = [strs[i]]   # Create a new list with this word
            else:
                seen[sort].append(strs[i]) # Add it to the existing group
        return list(seen.values())

                
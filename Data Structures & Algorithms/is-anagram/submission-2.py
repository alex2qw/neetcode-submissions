class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        frequency1={}
        for i in s:
            if i in frequency1:
                frequency1[i] +=1
            else:
                frequency1[i] = 1

        
        frequency2={}
        for i in t:
            if i in frequency2:
                frequency2[i]+=1
            else:
                frequency2[i]=1

           
        return frequency1 == frequency2
    
        return False

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashMap = { 
            ")" : "(", 
            "]" : "[",
            "}" : "{"
        }

        for character in s:
            if character in hashMap:
                if stack and stack[-1] == hashMap[character]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(character)
                
        return True if not stack else False

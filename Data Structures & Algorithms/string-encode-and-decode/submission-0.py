class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = [] 
        for s in strs:
            # Format it as length#word and append it straight to our list
            encodedString.append(f"{len(s)}#{s}")
        # Glue all the pieces back together into one single string
        return "".join(encodedString)
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 # Our pointer
        while i < len(s):
            j = s.find("#", i) #Find the '#' starting from pointer i
            length = int(s[i:j]) # Extract the length number between i and j
            word = s[j + 1 : j + 1 + length] # Slice out the word
            res.append(word) 
            i = j + 1 + length # Jump pointer i forward past the word
        return res

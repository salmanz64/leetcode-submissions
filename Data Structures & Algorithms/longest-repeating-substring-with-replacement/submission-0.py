class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        maxChars = 1
        hashMap = {}
        while right < len(s):
            if s[right] in hashMap:
                hashMap[s[right]] +=1
            else:
                hashMap[s[right]] = 1
            if (right -left + 1) - max(hashMap.values()) <=k:
                maxChars = max(maxChars,right-left+1)
            else:
                
                hashMap[s[left]] -=1
                left +=1
            right+=1
        return maxChars



        
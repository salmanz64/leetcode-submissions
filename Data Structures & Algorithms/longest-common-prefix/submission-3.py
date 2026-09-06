class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        minString = min(strs,key=len)
        print(minString)
        for i in range(len(minString)):
            for j in range(len(strs)):
                if minString[i] != strs[j][i]:
                    return result
            result+=minString[i] 
        return result

        
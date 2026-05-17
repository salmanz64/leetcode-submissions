class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        op = ""
        minstr = min(strs)
        for i in range(len(minstr)):
            for j in range(len(strs)):
                if strs[j][i] != minstr[i]:
                    return op
            op+=minstr[i]

        return op

        
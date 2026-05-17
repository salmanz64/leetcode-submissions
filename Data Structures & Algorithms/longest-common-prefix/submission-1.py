class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        op = ""
        # to make sure min is done on numerical len not lexical order
        minstr = min(strs,key=len)
        for i in range(len(minstr)):
            for j in range(len(strs)):
                if strs[j][i] != minstr[i]:
                    return op
            op+=minstr[i]

        return op

        
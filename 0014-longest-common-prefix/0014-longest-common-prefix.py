class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = []
        for chars in zip(*strs):          
            if len(set(chars)) == 1:      
                prefix.append(chars[0])
            else:
                break
        return "".join(prefix)
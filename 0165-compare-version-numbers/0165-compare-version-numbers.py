class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1  = version1.split('.')
        ver2  = version2.split('.')
        ver1_len = len(ver1)
        ver2_len = len(ver2)
        for i in range(max(ver1_len, ver2_len)):
            v1 = int(ver1[i]) if i < ver1_len else 0 
            v2 = int(ver2[i]) if i < ver2_len else 0
            if v1 > v2:
                return 1
            if v1 < v2:
                return -1
        return 0
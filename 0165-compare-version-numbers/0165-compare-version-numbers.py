class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        splitarr1=version1.split(".")
        splitarr2=version2.split(".")
        i=0
        while i<len(splitarr1)and  i<len(splitarr2):
            if int(splitarr1[i])<int(splitarr2[i]) :
                return -1
            if int(splitarr1[i])>int(splitarr2[i]):
                return 1
            i+=1
        while i<len(splitarr1):
            if int(splitarr1[i])>0:
                return 1
            i+=1
        while i<len(splitarr2):
            if int(splitarr2[i])>0:
                return -1
            i+=1
        return 0
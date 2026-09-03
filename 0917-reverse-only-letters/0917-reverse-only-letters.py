class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters=[]
        #extracting all the letters 
        for ch in s:
            if ch.isalpha():
                letters.append(ch)
        #reverse the letters 
        letters.reverse()
        result=''
        index=0
        #put reverse letters back 
        for ch in s:
            if ch.isalpha():
                result+=letters[index]
                index+=1
            else:
                result+=ch
        return result 
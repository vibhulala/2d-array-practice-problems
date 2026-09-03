class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        '''brute force appraoch 
        :- is approach mein hm diye gaye mixed string me se sare characters ko pic kar rhe hain after that picking process hmne  sare characters ko revrese kar diya aur letters nam ke ek list mein dal diya and then hmne ek result empt stirng banayi ab s ko fir se traverse kkuiiya agar alphbet hua to to letters mein ke index mein usko dal denge and result mein add kar deneg agra alphabet nhi ahua to as it is use result mein add kar denege 
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
        tc-o(n)
        sc-o(n)
        '''
        chars=list(s)
        left=0
        right=len(chars)-1
        while left<right:
            #find a letter from left 
            if not chars[left].isalpha():
                left+=1
            #find a letter from right 
            elif not chars[right].isalpha():
                right-=1
            else:
                #both are letters than sidha swap 
                chars[left],chars[right]=chars[right],chars[left]
                left+=1
                right-=1
        return "".join(chars)
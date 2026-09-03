class Solution:
    def maxDepth(self, s: str) -> int:
        '''
        brute force:- is approach mein hm har opening paranthesis ke liye dekh skte hain ki uska closing paranthesis kaha hai 
        and uske andar kitne pranthseis nested hain basically matching praenthesis count karke depth claculate krenge 
        but probelm -  repeted scanning hai but fir bhi isksa code dekh lete hain 
        code :-
        
        max_depth=0
        #check every opening parantheseis 
        for i in range(len(s)):
            if s[i]=='(':
                depth=1
                max_depth = max(max_depth, depth)
                #find its matching closing paraenthseis 
                for j in range(i+1,len(s)):
                    if s[j]=='(':
                        depth+=1
                        max_depth = max(max_depth, depth)
                    elif s[j]==')':
                        depth-=1
                        if depth==0:
                            break
        return max_depth
        #tc o(n^2)
        #sc o(n)
        '''
        depth=0
        max_depth=0
        for c in s:
            if c=='(':
                depth+=1
            elif c==')':
                depth-=1
            max_depth=max(max_depth,depth)
        return max_depth


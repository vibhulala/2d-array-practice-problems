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
        '''
        brute force :- isme hamen kya kiy ana dekho ek depth nam ka counter liya usko set kiya ki ag ropening aya to ek badhoge badhne ke bad tb tk badhna jab oepning ate rhe fir maximum mein sabse bahd gaye abb closing jaise hi ana shuru hua hm depthwa ek ek karke ghataynege aur maximum rhegag wahi kyuki max() funtion ka use kiya hain to wahi rhega end mein max_depth return kar denge 

        '''
#bascially optimized bhi yahi hai bas kya karneeg ki max ko (  yh oepning jab check karneeg tb hi max_depth update kar denge poora karke krne ki jarurat nahi ahi 
        depth=0
        max_depth=0
        for c in s:
            if c=='(':
                depth+=1
                max_depth=max(max_depth,depth)
            elif c==')':
                depth-=1
            
        return max_depth
        tc-o(n)
        sc-o(1)
        



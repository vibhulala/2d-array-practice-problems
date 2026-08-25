class Solution {
public:
    int longestPalindrome(string s) {
        int n=s.length();
        unordered_set<char> st;
        int result=0;
        for (int i=0;i<n;i++){
            char ch=s[i];
            if(st.count(ch)){
                result+=2;
                st.erase(ch);
            }
            else{
                st.insert(ch);
            }
        }
        if(!st.empty()){
            result++;//makinig odd length palindrome jiska pair bana //hi nahi aur abcha reh gya usko end me add akr denge 
        }
        return result;
    }
};  
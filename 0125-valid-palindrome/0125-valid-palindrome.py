class Solution:
    def isPalindrome(self, s: str) -> bool:
        flag= True
        lis=[]
        lis_=[]
        for i in range(len(s)):
            if s[i].isupper() or s[i].islower() or s[i].isnumeric():
                lis.append(s[i].lower())
        for j in range(len(lis)-1,-1,-1):
            lis_.append(lis[j])
        return lis_ == lis    
        
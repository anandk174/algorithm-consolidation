class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        is_repeatable = False
        for window_size in range(1,int(len(s)/2)+1):

            if s[0:window_size] *(int(len(s)/window_size)) == s:
                is_repeatable = True
                break

        return(is_repeatable)

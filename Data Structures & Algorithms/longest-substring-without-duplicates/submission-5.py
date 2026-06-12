class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        mp = dict()
        max_seen = 0

        l = r = 0

        while r < len(s) and l < len(s):


            if s[r] in mp:
                l = max(l, mp[s[r]] + 1)
                mp[s[r]]=r
            else:
                mp[s[r]]=r

            
            max_seen = max(max_seen, r-l+1)
            r+=1


        return max_seen
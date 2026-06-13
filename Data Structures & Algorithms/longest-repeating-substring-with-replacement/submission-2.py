class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = r = 0
        mp = dict()
        maxf = 0
        res = 0

        while r < len(s):

            mp[s[r]] = 1 + mp.get(s[r], 0)
            maxf = max(mp.values())

            while (r-l+1) - maxf > k:

                mp[s[l]] -=1
                l+=1
            
            res = max(res, r-l+1)

            r+=1

        return res
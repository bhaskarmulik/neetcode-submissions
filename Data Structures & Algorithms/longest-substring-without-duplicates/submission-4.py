class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        mp = dict()
        max_seen = 0

        l = r = 0

        while r < len(s) and l < len(s):

            print(f"R : {r}")
            print(f"L : {l}")

            if s[r] in mp:
                l = max(l, mp[s[r]] + 1)
                mp[s[r]]=r
                print(f"L : {l}")
            else:
                mp[s[r]]=r

            print(mp)
            print("-----------")
            
            max_seen = max(max_seen, r-l+1)
            r+=1


        print(mp)
        return max_seen
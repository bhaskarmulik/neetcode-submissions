class Solution:

    def letter_hash(self, string):

        temp = [0 for _ in range(26)]

        for s in string:
            temp[ord(s) - ord('a')] += 1
        
        return temp

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)

        for i, s in enumerate(strs):

            res[tuple(self.letter_hash(s))].append(s)
        
        return list(res.values())
            

                
            
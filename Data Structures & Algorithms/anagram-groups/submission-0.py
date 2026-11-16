class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #key is the sorted wor value is the actual word

        d = {}

        for word in range(len(strs)):
            key = "".join(sorted(strs[word]))
            if key not in d:
                d[key] = []
            d[key].append(strs[word])
        
        sol = []
        for i in d:
            sol.append(d[i])
        return sol
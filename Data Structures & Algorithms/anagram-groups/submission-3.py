class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for x in strs:
            key = "".join(sorted(x))
            groups.setdefault(key, []).append(x)
        return list(groups.values())

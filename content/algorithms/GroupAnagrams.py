class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        dic = {}
        for s in strs:
            sort = ''.join(sorted(s))
            if sort not in dic:
                dic[sort] = len(dic)
                answer.append([])
            answer[dic[sort]].append(s)
        return answer

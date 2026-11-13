class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        pathsDict = defaultdict(list)
        for path in paths:
            parts = path.split()  # [0]은 경로가됨
            for part in parts[1:]:
                i = part.find('(') + 1  # content의 시작 위치
                pathsDict[part[i:-1]].append(parts[0]+'/'+part[:i-1])
        
        answer = []
        for val in pathsDict.values():
            if len(val) > 1:
                answer.append(val)
        return answer

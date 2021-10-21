class Solution:
    def isSubsequence(self, str: str, t: str) -> bool:
        length = len(str)
        idxs = 0
        idxList = [-1]
        for s in str:
            idx = t.find(s)
            idxList.append(idx + idxs)
            t = t[idx + 1:]  # str=ab t=baab 같은 경우때문에 확인한 이전의 t는 잘라버림
            idxs += idx + 1  # 그땜에 인덱스가 변해버려서 버린 인덱스만큼 따로 저장해줌
        for i in range(length):
            if idxList[i] >= idxList[i + 1]:
                return False
        return True

    # 거지같이 짰군... 나중에 다시 풀어보자
    # str에 있는 문자들이 t에 몇번째에 위치하는지 저장.(없으면 -1)
    # 그 저장된 위치들을 확인해서 앞에보다 뒤에 글자 인덱스가 작다면 False반환
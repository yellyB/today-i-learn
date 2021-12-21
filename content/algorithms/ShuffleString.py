class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        # indices에서 i의 위치를 찾음
        # 그 인덱스를 s에서 글자로 반환함
        answer = ''
        for i in range(len(indices)):
            idx = indices.index(i)
            answer += s[idx]
        return answer
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        answer = []
        minNum = 0
        maxNum = len(s)
        for d in s:
            if d == 'I':
                answer.append(minNum)
                minNum += 1
            else:
                answer.append(maxNum)
                maxNum -= 1
        answer.append(minNum)
        return answer

    # I 를 만났을땐 앞에가 작아야함. -> 남은 숫자 중 가장 작은애 붙이자 / D일땐 반대
    # I 를 만나면 젤 작은 숫자를 붙이고 젤작은 숫자를 1증가
    # D 를 만나면 젤 큰 숫자 붙이고 젤큰숫자 1감소
    # 맨 마지막엔 젤 작= 젤 큰  임. 이걸 최종적으로 붙여줌
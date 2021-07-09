class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        operatorList = ['!', '&', '|']
        operator = []  # 연산자 저장될 stack
        isClose = []  # (괄호 열린 idx:열렸던 괄호 닫혔는지?)
        strList = list(expression)

        def strNot(idx1, idx2):
            if strList[idx1 + 1] == 't':
                return 'f'
            else:
                return 't'
            # return 't' if strList[idx1+1] == 'f' else 't'

        def strAnd(idx1, idx2):
            result = 't'
            for i in range(idx1 + 1, idx2):  # 괄호 안 t,f만 출력
                if strList[i] != ',':
                    if result == 't' and strList[i] == 't':
                        result = 't'
                    else:
                        result = 'f'
            return result

        def strOr(idx1, idx2):
            result = 'f'
            for i in range(idx1 + 1, idx2):
                if strList[i] != ',':
                    if result == 'f' and strList[i] == 'f':
                        result = 'f'
                    else:
                        result = 't'
            return result

        i = 0
        while 1 < len(strList):
            if strList[i] == '(':  # 연산이 시작된다면 그 위치와 연산 종료 여부 저장
                isClose.append(i)
            elif strList[i] == ')':  # 어떤 계산이 종료되었단 뜻. 열렸는데 안닫힌 마지막 괄호 위치 찾기
                notClosedLastIdx = isClose.pop()
                op = strList[notClosedLastIdx - 1]
                if op == '!':
                    result = strNot(notClosedLastIdx, i)  # ex (f,t,f)
                elif op == '&':
                    result = strAnd(notClosedLastIdx, i)
                elif op == '|':
                    result = strOr(notClosedLastIdx, i)
                strList[notClosedLastIdx - 1] = result
                del strList[notClosedLastIdx:i + 1]
                i = notClosedLastIdx - 1
            i += 1
            if i == len(strList):  # 끝까지 다 돌았으면 다시 처음으로 ㄱㄱ
                isClose = []
                i = 0

        if strList[0] == 't':
            return True
        else:
            return False

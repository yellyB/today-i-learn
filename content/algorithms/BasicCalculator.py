class Solution:
    def calculate(self, s: str) -> int:
        def calculater(calList):
            res = 0
            while calList:
                val = calList.pop()
                if val == '+':
                    res += int(calList.pop())
                elif val == '-':
                    res -= int(calList.pop())
                else:
                    res += int(val)
            return str(res)
        
        
        ans = 0
        stack = []
        tempNum = ''
        
        for ss in s:
            if ss == ')':
                stack.append(tempNum)  # 닫힌괄호 만나면 임시숫자문자열 먼저 넣음
                tempNum = ''
                
                cals = []  # 숫자와 연산자 담길 배열
                while stack[-1] != '(':
                    cals.append(stack.pop())
                
                stack.pop()  # 앞에 ( 제거
                tempNum = calculater(cals)
                
            elif ss == ' ':
                pass
            elif ss == '(':
                stack.append(ss)
            elif ss in ['+', '-']:  # 연산자 만나면 1.쌓아온 숫자 먼저 넣고, 2.연산자 넣음
                if tempNum == '':  # 맨앞 숫자 음수일경우 대비
                    # tempNum += ss
                    stack.append(ss)
                else:
                    stack.append(tempNum)
                    tempNum = ''
                    stack.append(ss)
            else:
                tempNum += ss  # 숫자 여러자리일 수 있으니 임시 문자열로 저장
                
        # 여기까지 하면 모든 괄호 계산은 완료
        while stack:
            val = stack.pop()
            if val == '+':
                ans += int(tempNum)
                tempNum = 0
            elif val == '-':
                ans -= int(tempNum)
                tempNum = 0
            else:
                tempNum += int(val)
                
        return ans + int(tempNum)  # 인풋이 0인경우 대비해서 int로

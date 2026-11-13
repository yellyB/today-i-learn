class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # left와 right는 괄호의 왼, 오 추가되어야할 남은 개수 뜻함
        def func(left, right, path):
            # 왼이 더 크면 열리지도 않은 괄호가 닫혔단뜻
            # 왜냐면 왼오는 남은 개수를 뜻하기때문에 오가 작다는건 오를 그만큼 많이 썼단것이기때문
            if left > right or left < 0 or right < 0:
                return
            if left == 0 and right == 0:  # 왼, 오 괄호를 다 썼다면 성공
                answer.append(path)
                return
            
            func(left-1, right, path+'(')
            func(left, right-1, path+')')
            return
        
        answer = []
        func(n, n, "")
        return answer

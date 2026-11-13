class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []
        res = [0] * len(heights)
        
        for i in range(len(heights)):
            # stack에 들어간 애가 나보다 작으면 날 볼수있음
            # 그리고 걔는 나땜에 내 다음애들을 보지 못함
            while stack and heights[stack[-1]] < heights[i]:
                res[stack.pop()] += 1
            
            # 위 while문에서 팝되지 않은 애들은 [i]보다 크기때문에 팝되지 않은것.
            # stack[-2]는 [-1]보다 크다. 왜냐면 [-1]보다 작았다면 그 당시에 팝됐을것이기때문
            # 그러므로 stack에는 밑으로 갈수록 큰애들이라는것.
            # 따라서 stack[-1]이 나보다 크니까 그 전에애들은 다 나보다 크긴해도 [-1]때문에 가려서 날 못봄
            # 걔네들은 자기보다 더 큰애가 나왔을때만 그 큰애를 볼 수 있을거임
            # 그럼 일단 여기서는 [-1]에 날 볼 수 있음을 체크해주자
            if stack:
                res[stack[-1]] += 1
            
            stack.append(i)
            
        return res
    
    # 내가 볼 수 있는 경우:
    #   1. 오른쪽 애들이 나보다 작다 (+ 걔와 나 사이에 걔보다 큰 애 없어야함)
    #   2. 오른쪽 애들중 가장 큰 애
    #   3. 오른쪽 애 중 나보다 큰 애

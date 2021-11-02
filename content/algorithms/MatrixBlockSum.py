class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        ilength = len(mat)
        jlength = len(mat[0])
        answer = [ [0] * jlength for i in range(ilength)]
        # 1 맨위,맨왼의 누적
        for n in range(1, ilength):
            mat[n][0] = mat[n-1][0] + mat[n][0]
        for n in range(1, jlength):
            mat[0][n] = mat[0][n-1] + mat[0][n]

        # 2 맨위,맨왼 제외 누적
        for i in range(1, ilength):
            for j in range(1, jlength):
                mat[i][j] = mat[i][j] + mat[i-1][j] + mat[i][j-1] - mat[i-1][j-1]
        # print(mat)

        # 3 누적값 이용한 계산
        for i in range(ilength):
            for j in range(jlength):
                iMin = min(ilength-1,i+k)
                jMin = min(jlength-1,j+k)
                answer[i][j] = mat[iMin][jMin]
                if i-k >= 1:
                    answer[i][j] -= mat[i-k-1][jMin]
                if j-k >= 1:
                    answer[i][j] -= mat[iMin][j-k-1]
                if i-k >= 1 and j-k >= 1:
                    answer[i][j] += mat[i-k-1][j-k-1]

        # print(answer)
        return answer


# mat = [[1,2,3],[4,5,6],[7,8,9]] 일 때

# 누적 합계 :  [[1, 3, 6], [5, 12, 21], [12, 27, 45]]
#    ㄴ> 맨위,맨왼 누적 구하고(1번for). 나머지는 위,왼,자기자신 다 더한거에 대각선 왼쪽위를 빼줌(2번 for)

# 다 구하고 (3번for)에서 최종답 구할건데
# row인덱스랑 col인덱스에서 k를 뺐을때 1 이상이면 빼줘야 하는 공간이 있는거

# 일단 지금 구해야하는 범위 전부의 합계를 구하고(이미 구한값 이용)
# 포함되지 않는 부분을 빼주면 됨
# 빼줘야하는 부분이 맨 윗줄만 있거나 맨 왼만 있으면 그냥 빼주면 됨
# 그러나 두 면 다 빼줘야 한다면 겹치는 부분인 [i-k-1][j-k-1]을 다시 한번 더해줌
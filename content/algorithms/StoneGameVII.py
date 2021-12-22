class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        score = {}
        def aliceTurn(sums, i, j):
            if i >= j:
                return 0
            key = str(i)+ ',' + str(j)
            if key in score:
                return score[key]
            sumsF = sums - stones[i]  # 첫번째 선택했을때 점수
            sumsL = sums - stones[j]
            result = max(sumsF-aliceTurn(sumsF, i+1, j), sumsL-aliceTurn(sumsL, i, j-1))
            score[key] = result
            return result

        sums = sum(stones)
        return aliceTurn(sums, 0, len(stones)-1)
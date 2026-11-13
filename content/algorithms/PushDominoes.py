class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        def updateDominoes(start, end):
            left, right = dominoes[start - 1], dominoes[min(length - 1, end + 1)]

            # 첫이거나 끝
            if start == 0:
                if right == 'L':
                    left = right  # 전부 쓰려뜨려야함
                elif right == 'R':
                    left = 'L'  # 쓰러뜨릴거 없으니까 밑에서 처리되게 left업뎃
            if end == length - 1:
                if left == 'R':
                    right = left
                elif left == 'L':
                    right = 'R'

            # 쓰러뜨릴게 없으면 걍 반환
            if left == 'L' and right == 'R': return dominoes[start:end + 1]

            # if start == 0: left = right  # 첫이거나 끝이면 어차피 한쪽으로 쓰러짐
            # if end == length-1: right = left

            tempList = list(dominoes[start:end + 1])
            i = -1
            for i in range((end - start + 1) // 2):
                tempList[i] = left
                tempList[-i - 1] = right
            if left == right:  # 가운데 처리
                tempList[i + 1] = left
            return ''.join(tempList)

        length = len(dominoes)
        start, end = 0, 0
        for i in range(length):
            dominoe = dominoes[i]
            if dominoe == '.' and dominoes[max(0, i - 1)] != '.':
                start = i
            if dominoe == '.' and dominoes[min(length - 1, i + 1)] != '.':
                end = i
                result = updateDominoes(start, end)
                dominoes = dominoes[:start] + result + dominoes[end + 1:]
        # 마지막 . 덩어리 처리
        if start > end:
            end = i
            result = updateDominoes(start, end)
            dominoes = dominoes[:start] + result + dominoes[end + 1:]
        return dominoes

# 연속되는 . 의 범위를 알아내서 걔네를 쓰러뜨릴거임
# 쓰러뜨릴때 반으로 나눠서 왼쪽은 왼쪽도미노의 상태, 오른쪽은 오른쪽도미노 상태로 만들면됨
#           (길이가 홀수면 가운데는 안쓰러지겠찌?) + 한쪽으로만 쓰러질경우는 가운데 남기면 안됨
#   ㄴ 여기서 왼쪽이나 오른쪽이 제일 끝일경우는 예외처리(끝이면 어차피 끝아닌쪽 방향으로 쓰러질거임)
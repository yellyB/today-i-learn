class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        targetLen = k  # 3
        targetNum = n  # 7
        answer = []

        def getNextElement(nums, target, i):
            for n in range(i, 10):
                temp = nums[:]
                rest = target - n
                length = len(temp)

                # len(temp)랑 타겟len이랑 같으면 내부 if문에서 하나 더 추가하고
                # answer에 붙이든 다시재귀돌리든 해야하는데 그럼 len넘어감
                # 그래서 타겟이 len - 1보다 작을때만 정상실행
                if rest == 0:
                    if length == targetLen - 1:
                        temp.append(n)
                        answer.append(temp)

                elif rest > 0:  # 아직 target에 도달 못했단 뜻
                    if length < targetLen:
                        temp.append(n)
                        getNextElement(temp, rest, n + 1)

                else:  # target 넘어가버림
                    return

        getNextElement([], targetNum, 1)

        return answer
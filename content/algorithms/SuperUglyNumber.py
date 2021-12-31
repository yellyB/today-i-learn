class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        uglys = [1]  # 결과들을 저장할곳
        idxs = [0] * len(primes)  # primes랑 곱한 각각의 마지막 uglys 위치가 어디?
        lastVals = primes[:]  # 곱셈 마지막 결과 저장한곳. 첨엔 1이랑 곱한상태니까 걍 primes그대로임

        i = 0
        while i < n - 1:
            # 1. 최소값 추가해주기
            minNum = min(lastVals)
            uglys.append(minNum)

            # 2. 걔를 갱신해줌
            for j in range(len(primes)):
                if lastVals[j] == minNum:
                    idxs[j] += 1  # 그 prime이 uglys에서 마지막으로 곱한 수의 위치를 1증가
                    lastVals[j] = primes[j] * uglys[idxs[j]]  # 마지막 계산 결과에 (그 prime * uglys의 새로 곱해줘야하는 애)
                # **index로 찾아서 하니까 timeout나서 방법 바꿔봄
            i += 1

        return uglys[-1]

    # primes에서 각 숫자들을 내가 구한 ugly 목록들하고 차례로 곱해 나갈거임
    # 곱한 primes 중 가장 작은 값을 다음 ugly 목록에 추가하고 방금 걔는 다음값으로 갱신해줌
    # https://leetcode.com/problems/ugly-number-ii/    264. Ugly Number II  얘랑 비슷...?


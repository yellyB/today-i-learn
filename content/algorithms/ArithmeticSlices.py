class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        minStart = len(nums) - 2  # 이 인덱스까지만 확인하면 됨(subarray길이가 최소 3이어야해서)
        if minStart < 1:
            return 0
        cnt = 0

        def isArithmetic(start, end, gap):
            for i in range(start + 1, end):
                if nums[i + 1] - nums[i] != gap:
                    return False
            return True

        for i in range(0, minStart):
            # 일단 [n,m,k]3개만 확인해서 맞다면 그 이후부턴 추가되는 애만 일정하게 증가하는지 확인하면 됨
            gap = nums[i + 1] - nums[i]
            last = nums[i + 2]
            if isArithmetic(i, i + 2, gap):
                cnt += 1
                for j in range(i + 3, len(nums)):
                    if nums[j] - last == gap:
                        cnt += 1
                        last = nums[j]
                    else:
                        break
            else:
                continue

        return cnt

    # subarray는 최소 3개 요소
    #   => subarray 의 시작점은 nums의 마지막 -2 까지만 보면 됨
    #      (마지막-1 마지막-2는 어차피 len=3이 안나오기땜에 볼필요x)
    # 이중반복문으로 subarray의 시작점, 끝점을 정해서 순열판별함수로 보내줌
    # 결과에 따라 cnt +1함

    # 넘 오래 걸려서 다시 짬
    # 시작점을 설정할때 len-2로 하는건 똑같
    # 근데 그 시작점부터 3개까지만 일단 확인해서 맞으면 다음으로 ㄱㄱ 아니라면 다음 시작점으로
    # 위에서 순열이 맞았다면 그 3개 이후는 추가되는 것만 하나씩 일정하게 증가하는지 확인하면 됨

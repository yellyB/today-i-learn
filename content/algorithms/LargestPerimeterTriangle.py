class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        sort = sorted(nums, reverse = True)
        print(sort)
        for i in range(len(sort) - 2):
            if sort[i] < sort[i+1] + sort[i+2]:
                return sum(sort[i:i+3])
        return 0
    
    # 삼각형이 될 수 있는 조건을 생각해보면 됨
    # 만약 10, 5, 2짜리 직선이 있으면 얘는 만들 수 없음.
    # 왜냐? 한 변은 10짜리일텐데 나머지 5랑 2가 10보다 커야 각이 만들어지는데 그게 안됨
    # 5를 기준으로 놓고 봐도 마찬가지. 10이 5를 훨씬 넘기때문에 2가 그 갭을 못따라감.
    # 그래서 결론은 가장긴변<나머지두변합 이어야 함

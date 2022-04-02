class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * len(nums)
        front = 1
        back = 1
        for i in range(n):
            answer[i] *= front
            answer[n-1-i] *= back
            front *= nums[i]
            back *= nums[n-1-i]
        
        return answer
    
    # 자기 자신 빼고 모두 곱해야하니까
    # 나 기준으로 앞부분과 뒷부분 나눠서 곱해줄거임
    
    # [front]
    # i가 증가하면서 누적된 값을 가지고 있으면서 0 ~ i-1 을 i에 전부 곱해주면서 앞으로 나가면 됨
    # 예를들어 i=3이다. front변수에다가 0~2 인덱스의 곱을 누적해서 가지고 있다가 answer의 [3]에 곱해줌
    # [back]
    # 이번에는 걍 거꾸로 가주면됨
    # i는 증가하니까 len이용해서 i만큼의 뒷부분에 곱해줄거임. 여기까진 간단하지?
    # i=3이면 4~5 인덱스의 값들을 누적 곱해줘야 하는데
    # 앞에서 [0]이랑 [1]였을때 [5]랑 [4]의 값을 미리 back에 누적해뒀다가 answer의 [3]에 back을 곱해줌
    
    # 참고로 i가 오름차순으로 도는거니까 뒤쪽 인덱스들은 front가 곱해지기 전에 back이 먼저 곱해질거임
    # 뒷부분은 아무래도 back에 곱해지는 숫자들 개수가 적을테니까

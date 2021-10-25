class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        vali = values[0]
        valj = values[1] - 1
        answer = vali + valj
        for i in range(1, len(values)):
            val = values[i]
            tempValj = val - i  # [j]-j값이 갱신될 때에만 answer를 갱신함
            temp = vali + tempValj
            if temp >= answer:
                answer, valj = temp, tempValj
            vali = max(vali, val + i)
        return answer

    # values[i] + values[j] + i - j 의 max값을 구하려면
    # 1. values[i]+i는 최대로하고   2. values[j]-j는 최소로 해야함
    # 이 두 값을 각각 구해서 리스트로 저장
    # 두 리스트를 돌려서 최대가 되는 합을 구한다.
    #    => 이 방법은 len 5만개 있어서 타임아웃

    # 제일 큰 [i]+i값이 계산된 이후의 리스트에서 [j]-j를 계산해야함
    # => [j]-j가 갱신될때에만 [i]+i랑 계산한 값을 갱신해주자
    #       ([i]+i는 이 전에서의 최대 값이 저장되어 있을 테니까)
    # 1번 방법에서 실패한 테스트케이스때문에 실패.. 데이터 넘 길어서 확인도 힘듬 ㅅㅂ

    # 2번 방법 다시 성공함!! 실패했던 이유는 12번째 줄을 if문 안에 넣어서 그랬음
    # 왜냐믄 vali는 answer가 업뎃될때가 아니라 반복문을 반복하면서 계속 갱신해줘야함
    # 그래야 vali를 최대값으로 만드는 지점을 안놓침!
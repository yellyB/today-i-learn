class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        left = 0
        maxVal = 0
        for right in range(length):
            findIdx = s[left:right].find(s[right])
            if findIdx == -1:
                maxVal = max(maxVal, len(s[left:right]) + 1)
            else:
                left += findIdx + 1

        return maxVal

    # left랑 right 두개를 사용할거임
    # s의 길이만큼 돌린게 right이고
    # left는 지금까지의 서브리스트중에 새로 추가될 값이(right) 들어있지 않다면 left를 변화시키지 않고 maxVal을 갱신해줌
    #                                                     들어있다면 left를 그 중복값이 있는 그 다음 인덱스부터 새로 검사하기 위해
    #                                                     left + 중복값이 있는 인덱스 + 1 로 갱신 해줄거임
    # 예를들어 pwwkew를 보자면
    # 맨 첨에는 p에(0번) w(1번)가 없으니까 maxVal은 2가 됨.
    # 근데 그 다음 2번인덱스 w가 pw(s[0:1])에 있으니까 left = left+1(중복되는w의 인덱스)+1해줌
    # 그래서 left는 2이 되었음
    # 계속해서 left가 2이니까... 쓰기 귀찮
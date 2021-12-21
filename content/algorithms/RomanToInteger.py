class Solution:
    def romanToInt(self, str) -> int:
        symbolValue = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        answer = symbolValue[str[len(str)-1]]  # str의 마지막꺼 미리 더해줌
        lastVal = 0
        for i in range(len(str)-2, -1, -1):
            # 앞에꺼 value가 뒤 value보다 작으면 빼줌 / 아니면 더해줌
            if symbolValue[str[i]] < symbolValue[str[i+1]]:
                answer -= symbolValue[str[i]]
            else:
                answer += symbolValue[str[i]]
        return answer
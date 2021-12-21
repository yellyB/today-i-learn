class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        cnt = 0
        size = 0
        # 최대한 많이 싣기 위해 상자 당 갯수가 많은 순대로 정렬
        boxTypes.sort(reverse=True, key=lambda x: x[1])
        for box in boxTypes:
            if size + box[0] <= truckSize:  # 제한사이즈 안넘었다면
                size += box[0]
                cnt += box[0] * box[1]
            else:  # 제한 사이즈 넘으면 남은 공간만큼만 채우고 끝
                restSpace = truckSize - size
                cnt += restSpace * box[1]
                return cnt
        return cnt
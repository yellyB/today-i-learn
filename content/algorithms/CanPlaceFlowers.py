class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        if n == 0:
            return True
        if len(flowerbed) == 1:
            if flowerbed[0] == 0 and n == 1:
                return True
            else:
                return False
        if flowerbed[i] != 1 and flowerbed[i+1] == 0:  # you can plant
            flowerbed[i] = 1
            n -= 1
        i += 1
        while i < len(flowerbed)-1 and n > 0:
            if flowerbed[i-1] == 0 and flowerbed[i] != 1 and flowerbed[i+1] == 0:  # you can plant
                flowerbed[i] = 1
                n -= 1  # 씨앗갯수 -1씩
            i += 1
        if n > 0 and flowerbed[i] != 1 and flowerbed[i-1] == 0:
            flowerbed[i] = 1
            n -= 1  # 씨앗갯수 -1씩
        return n == 0
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def changeValue(sr, sc):
            if 0 <= sr < len(image) and 0 <= sc < len(image[0]):
                if image[sr][sc] == flood:
                    image[sr][sc] = newColor
                    changeValue(sr + 1, sc)
                    changeValue(sr - 1, sc)
                    changeValue(sr, sc + 1)
                    changeValue(sr, sc - 1)

        flood = image[sr][sc]  # 맨 처음 타겟된 숫자, 앞으로 이 숫자랑 같으면 바꿔줄거임
        if flood == newColor:
            return image

        changeValue(sr, sc)

        return image
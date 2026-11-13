class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        colLen = len(image[0])
        for i in range(len(image)):
            image[i].reverse()  # 좌우반전
            for j in range(colLen):  # 값 반전
                image[i][j] = 1 if image[i][j] == 0 else 0
        return image
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            colLen = len(image[0])
            # 좌우반전
            for j in range(colLen//2):
                image[i][j], image[i][colLen-j-1] = image[i][colLen-j-1], image[i][j]
            # 값 반전
            for j in range(len(image[0])):
                # image[i][j] = 1 if image[i][j] == 0 else 1
                if image[i][j] == 0: image[i][j] = 1
                else: image[i][j] = 0
        return image
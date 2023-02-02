class LUPrefix:

    def find(self, x):
        self.uploaded.setdefault(x,x)
        if x != self.uploaded[x]:
            self.uploaded[x] = self.find(self.uploaded[x])
        return self.uploaded[x]

    def union(self, x, y):
        if x not in self.uploaded:
            return
        rootX = self.find(x)  # 니네 대표 데려와
        rootY = self.find(y)  # 니네 대표도 데려와
        self.uploaded[rootX] = self.uploaded[rootY] = max(rootX, rootY)  # 두 대표 중 더 쎈애로 교체!
        
    def __init__(self, n: int):
        self.uploaded = {}  # 연결된 애들 중 가장 긴 비디오 길이 갖고있을거임
        self.uploaded[0] = 0

    def upload(self, video: int) -> None:
        self.uploaded[video] = video
        
        self.union(video-1, video)
        self.union(video+1, video)
        
        
    def longest(self) -> int:
        return self.find(0)
        


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()

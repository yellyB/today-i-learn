class FreqStack:

    def __init__(self):
        self.maxFreq = 0
        self.freq = {}  # val별 freq 저장
        self.vals = {}  # freq(1~)별로 해당하는 val 목록 리스트로 갖고있기

    def push(self, val: int) -> None:
        if val in self.freq:
            self.freq[val] += 1
        else:
            self.freq[val] = 1
            
        occ = self.freq[val]  # val에 해당하는 빈도수 가져와서
        self.maxFreq = max(self.maxFreq, occ)  # maxFreq는 가장 많은 빈도수를 저장해야함
        
        # vals 는 freq에 해당하는 vals를 모두 가지고 있어야함. 추가해주기
        if occ not in self.vals:
            self.vals[occ] = []
        self.vals[occ].append(val)

    def pop(self) -> int:
        remove = (self.vals[self.maxFreq]).pop()  # 가장 많은 빈도의 가장 끝 요소
        self.freq[remove] = self.maxFreq - 1  # 빈도 수 줄여주고
        if len(self.vals[self.maxFreq]) == 0:  # maxFreq인 리스트 다 꺼냈으면
            self.maxFreq -= 1
        return remove


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()

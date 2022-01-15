class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        cnts = collections.Counter(arr1)
        answer = []
        for n in arr2:
            answer.extend([n] * cnts.pop(n))  # 개수를 팝해서 그 개수만큼 반복해서 붙여줌
        for key, val in sorted(cnts.items()):  # arr2에 없는것들도 붙여줌
            answer.extend([key] * val)
        
        return answer

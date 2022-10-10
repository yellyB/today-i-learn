class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        '''
        뒤에서부터 차곡차곡 정렬해야함:
        젤 뒤로 보낼애를 찾았으면 맨앞으로 가져와야
        걔가 원래 있던곳에서 플립했을때 맨 뒤로 보내짐
        '''
        
        res = []
        i = len(arr)
        while i > 0:
            idx = arr.index(i) + 1
            if i != idx:  # 인덱스랑 같지 않단건 정렬 필요하단 뜻
                
                # 1. 앞으로 가져옴
                res.append(idx)
                arr[:idx] = arr[:idx][::-1]
                
                # 2. 맨 뒤로
                res.append(i)
                arr[:i] = arr[:i][::-1]
                
            i -= 1
        return res
    
    
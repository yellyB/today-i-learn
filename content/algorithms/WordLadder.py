class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        L = len(beginWord)
        allStaredWord = defaultdict(list)  # {*ot:[hot, dot, lot]} 형태로 모든 wordList 저장
        for word in wordList:
            for i in range(L):
                allStaredWord[word[:i] + "*" + word[i+1:]].append(word) 
        
        queue = deque([(beginWord, 1)])
        visited = set()
        visited.add(beginWord)
        while queue:
            currWord, level = queue.popleft()
            for i in range(L):
                staredWord = currWord[:i] + '*' + currWord[i+1:]  # *로 변환한 단어
                for word in allStaredWord[staredWord]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited.add(word)
                        queue.append((word, level+1))
                        
        return 0
        
        
        
        # wordList의 모든 단어들을 딕셔너리에 한글자씩 *로 바꾼걸 키로하여 밸류에 리스트로 추가해줌
        # ex) {*ot:'hot', 'dot', lot'}
        
        # beginWord를 큐에 담아서 이걸 앞에서부터 하나씩 꺼내면서 검사할건데
        # 큐에 넣을때 level이란걸 같이 담을거임
        # level은 몇번 체인이 걸렸는지 저장하는 값임
        
        # while문 안에서 큐에서 꺼낸 값을
        # 처음에 한거처럼 각 단어 하나씩을 *로 바꿔서, 이걸 딕셔너리 키로 찾음
        # 그 키에 저장되어있는 리스트를 검사하면 큐에서 꺼낸 그 단어를 *로 바꾼거랑 똑같은 단어들만 볼 수 있음
        # 무슨말이냐면 begin=hit 이면 h*t라고해봐. 얘를 키로 저장되어있는 dict는 {h*t:'hot'}일거임
        
        # 그럼 요 리스트인 밸류를 또 반복문돌려서 찾으려는 endWord랑 같으면 level+1해서 리턴하면됨
        
        # 근데 hit->hot->dog->hot 같이 이미 검사한 hot을 또 검사할 위험 있으니까
        # visited 만들어서 검사한애는 더 검사안하도록.

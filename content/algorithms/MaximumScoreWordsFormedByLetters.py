class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def dfs(idx, counter):
            if idx == len(words): return 0
            
            wordCounter = collections.Counter(words[idx])  # 알파벳별 카운터
            
            totalScore = 0
            if all(counter[key] >= wordCounter[key] for key in wordCounter):
                wordScore = sum( score[ord(w)-97] for w in words[idx] )
                totalScore = max(   wordScore + dfs(idx+1, counter-wordCounter) , dfs(idx+1, counter)   )
            else:
                totalScore = dfs(idx+1, counter)
            
            return totalScore
        
        return dfs(0, collections.Counter(letters))
        
    
        
        # dfs 함수에는 인덱스랑 letters의 카운트를 전달할거임
        # [dfs함수]
        # 1. words[idx]의 각 알파벳별 카운트를 구함 ex) {d:1, o:1, g:1}
        # 2. 1에서 구한 카운트의 모든 숫자가 letters의 카운트 이하여야함(letters카운트를 넘어갈 수 없다)
        #       ㄴ 최고 점수 구해서 누적하기( 현재문자 선택 / 선택안하고 다음꺼 선택 ) 중 선택
        # 3. 2에서 실패했다면 현재 문자는 안된다는거니까 다음 문자로 넘겨줌
        
        
        
# 아래처럼 풀다가 for문 3중으로 돌아야해서(for문 하나는 아직 안짬) 알아서 포기        
#         def dp(letters, currScore):
#             for word in words:
#                 flag = True   # 문자열의 알파벳이 letters에 한번이라도 없다면 False로 실패할예정
#                 temp = 0  # 현재 단어의 점수. flag가 F면 추가 안해야 하기 때문에 임시변수 사용
#                 for w in word:
#                     if w in letters:
#                         temp += score[ord(w)-97]  # 점수 추가
#                         idx = letters.index(w)
#                         letters[idx] = '*'  # 사용한건 없애기
#                     else:
#                         flag = False
#                         break
#                 if not flag:
#                     return currScore
#                 else:
#                     currScore += temp
                    
#         dp(letters[:], 0)
        
#         return

class Solution:
    def decodeString(self, s: str) -> str:
        num = 0
        strs = ''
        numStack = []
        strStack = []
        for ss in s:
            # 여는 괄호 만나면 숫자와 문자를 스택에 각각 쌓고 초기화
            if ss == '[':
                numStack.append(num)
                strStack.append(strs)
                num = 0
                strs = ''
                continue
            if ss== ']':
                strs = strStack.pop() + (strs * numStack.pop())  # (이전에 모은 str)이랑 (현재괄호의 str)x반복  을 합침
                continue
                
            # 문자와 숫자 구분해서 누적
            if 97<=ord(ss)<=122:
                strs += ss
            else:
                num = (num)*10 + int(ss)
        
        return strs
        
        
        
        
        # 밑은 recursion으로 하다가 걷잡을 수 없어져서 일단 포기한거...
        """
        # "100[leetcode]" 일 경우 숫자가 3자리인데 이거 처리 안한상태
        def recursion(start):
            i = start
            curr = ''
            repeat = ''
            while i<len(s):
                # 닫히는 괄호 만나면 앞에 숫자만큼 repeat부분을 반복해줘서 리턴
                # i를 리턴하는건 상위 스코프로 돌아갔을 때 여기 스코프의 end부터 시작하기 위해(건너뛴단뜻)
                if s[i] == ']':
                    ret = repeat * int(s[start-2])
                    return [ret, i]
                # 시작괄호면 재귀 돌리기. 돌린 결과를 repeat에 추가
                if s[i] == '[':
                    res = recursion(i+1)
                    curr += res[0]
                    repeat += res[0]
                    i = res[1]
                # 숫자도 괄호도 아니면 반복되어야 하는 부분. repeat에 누적
                if 97<=ord(s[i])<=122: #and s[i]!='[' and s[i]!=']':
                    repeat += s[i]
                i += 1
            return curr
        
        # 앞에 괄호 없는 부분 그냥 추가해주기 위해
        i=0
        while i<len(s) and 97<=ord(s[i])<=122:
            i += 1
        if(i == len(s)): return s  # i가 끝까지 돌았다면 괄호 없단뜻. 그냥 리턴
                
        # 뒤에 괄호 없는 부분 그냥 추가해주기 위해
        for j in range(len(s)-1, -1, -1):
            if s[j] == ']': break
                
        return s[:i] + recursion(0) + s[j+1:]
        """

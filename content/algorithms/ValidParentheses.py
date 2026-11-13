class Solution:
    def isValid(self, s: str) -> bool:
        lists=[]
        pair = {'(':')','[':']','{':'}'}
        for i in s:
            if i in pair:
                lists.append(i)
            else:
                # 닫힌거 만나면 저장해둔 앞 괄호 꺼내서 그거의 짝이랑 일치하는지?
                if len(lists) == 0:  # 닫힌거 만났는데 len=0이란건 열린괄호 없단거
                    return False
                closeParenthese = lists.pop()
                if pair[closeParenthese] != i:
                    return False
        # 남아있는 애 있으면 false
        if len(lists) != 0:
            return False
        return True
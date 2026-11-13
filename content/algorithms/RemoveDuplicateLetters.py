class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        lastIdxs = collections.defaultdict(int)
        stack = []
        checked = set()

        # 문자들의 마지막 위치만 저장
        for i in range(len(s)):
            lastIdxs[s[i]] = i


        for i, ss in enumerate(s):
            if ss in checked:
                continue
            
            # 스택 마지막 애가 현재 문자보다 크면 이 마지막애를 제거하는게 좋은데
            # 근데 그 애가 현재애 뒤에 또 나와야지 적어도 한번 등장하기 때문에
            # lastIdxs 에 저장해놓은 마지막 등장 위치를 확인해서
            # 현재애보다 뒤에 나오는지 확인하고 제거함
            # set 에서 제거해놓으면 다음번 등장했을때 윗줄 if 문에서 안걸릴거고
            # 그러면 이 마지막이었던 애를 다시 검사해서 스택에 넣어줄 수 있음
            while stack and ss < stack[-1] and lastIdxs[stack[-1]] > i:
                checked.remove(stack.pop())

            stack.append(ss)
            checked.add(ss)

        return "".join(stack)

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1 = len(s1)
        list1 = [0] * 26
        list2 = [0] * 26

        for s in s1:
            list1[ord(s) - 97] += 1

        for i, s in enumerate(s2):
            list2[ord(s) - 97] += 1
            if i >= len1:
                list2[ord(s2[i - len1]) - 97] -= 1
            if list1 == list2:
                return True
        return False

# slide window 이용
# 1) s1과 s2에 각 알파벳만큼 0으로 초기화 한 리스트를 만듦(list1, list2)
# 2) list1에다가 아스키코드를 이용해 무슨 알파벳이 몇번 나오는지 체크
# 3) 이번엔 list2에 2번 과정을 할 건데
#    만약 지금 i가 s1의 길이보다 같.크면 윈도우를 한칸씩 오른쪽 이동 할거임
#    이게 무슨말이냐~
#    딱 s1의 길이만큼만 체크해서 알파벳freq값이 lis1과 list2이 서로 같으면 된단 뜻
#    그래서 s1의 len을 초과하는 만큼 젤 앞의 알파벳은 검사대상에서 빼줌

#    permutation을 구하라 했으니까 순서는 상관없고 떨어져있지만 않음 됨
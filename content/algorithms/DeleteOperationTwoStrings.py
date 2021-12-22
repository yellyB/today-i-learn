class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def getMaxVal(idx):  # 인덱스 받아서 그 이전것들중 최고값 돌려줌
            if common[:idx]:
                return max(common[:idx])
            else:
                return 0

        common = [0] * len(word2)
        for i in range(len(word1)):
            maxVal = 0
            temp = common.copy()  # 만약 word2의 뒤에 word1[i]랑 똑같은게 있다면 maxVal을 계산할때 앞에나온 알파벳때문에 common에 값이 업뎃된 후기 때문에 임시로 리스트 만들어서 비교할때는 원본인 common과 비교하는 방식
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    maxVal = max(getMaxVal(j), maxVal)
                    temp[j] = maxVal + 1
            common = temp.copy()
        print(common)

        commonMax = max(common)  # 공통되는 가장 긴 단어(연속되지 않을수도)
        return abs(commonMax - len(word1)) + abs(commonMax - len(word2))

    # 아래 방식으로 하다가 중복체크가 도저히 안돼갖고 수정함.
    # 아래방식은 : word1에는 한개고 word2에는 두개면 그 둘중 어떤걸 선택하는게 베스트선택인지 알려면 복잡해짐
    # 그래서 word1에 각 알파벳과 word2의 각 알파벳을 전부 매치해서 검사.

# 두 단어에서 공통되는 알파벳 갯수를 찾음. 그 외의 알파벳들은 모두 조작을 해줘야 서로 같아진다는 뜻임
# word1에 길이가 작은걸 놓고 word2만큼 [0]리스트(common)를 만듬
# word1에서 돌아가면서 그 알파벳이 word2에 있나, 있으면 몇번째 있나 찾음
# 찾은 인덱스 위치보다 작은 인덱스인 알파벳을 찾았을 때 있었는지? 봄
#       (지금보다 작은애중에 같은걸 찾아야 하는데 word1은 어차피 차례로 도는데 word2는 아니니까)
# 그 앞 리스트중에 가장 큰 값을 찾아서 거기에 +1해줌
# ex)
# dabc를 abcdd에서 찾기
# d는 3번째. [0,0,0,1,0]
# a는 0번째. [1,0,0,1,0]
# b는 1번째. [1,2,0,1,0]
# c는 2번째. [1,2,3,1,0]
# 그래서 가장 큰 값은 3임. 이거는 공통된(연속되지 않을수도)알파벳중 가장 긴 단어임
# word1이랑 word2에서 각각 공통되는 부분만큼 빼주면 얼마나 조작해야 하는지 알수있음


# word1 = "algorithm"
# word2 = "altruistic"  # 9
# alrit

# word1 = 'intention'
# word2 = 'execution'  # 8

# word1 = "kitten"
# word2 = "sitting"  # 5

# word1 = "dinitrophenylhydrazine"
# word2 = "acetylphenylhydrazine"  # 11

# word1 = "food"
# word2 = "money"  # 7

# word1 = "leetcode"
# word2 = "etco"  # 4
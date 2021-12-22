class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '': return []
        keyPad = ['','','abc','def', "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        combinations = ['']
        for digit in digits:
            canPush = keyPad[int(digit)]
            temp = []
            for combination in combinations:
                # print(combination)
                for item in canPush:
                    # print(combination+item)
                    temp.append(combination+item)
            combinations = temp


        return combinations
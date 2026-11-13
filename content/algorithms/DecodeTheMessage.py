class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        dict = {' ':' '}
        asci_a = 97
        i = 0
        for _, k in enumerate(key):
            if k != ' ' and k not in dict:
                dict[k] = chr(asci_a+i)
                i += 1

        res = ''
        for m in message:
            res += dict[m]
        
        return res

class Solution:
    def pow(self, n):
        result = 1
        for i in range(1,n):
            result = result * 10
        return result

    def multiply(self, num1, num2):
        sum = 0

        for i in range(len(num1)-1,-1,-1):
            for j in range(len(num2)-1,-1,-1):
                numberPosition1 = self.pow(len(num2)-j)
                numberPosition2 = self.pow(len(num1)-i)
                sum += (ord(num1[i])-ord('0'))*(ord(num2[j])-ord('0'))*numberPosition1*numberPosition2
        return str(sum)
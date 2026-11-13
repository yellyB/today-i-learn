class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisfied = 0
        unsatisfied = 0
        ownerTechnique = 0  # owner 테크닉을 써서 얻은 만족도 
        
        for i, customer in enumerate(customers):
            if not grumpy[i]:
                satisfied += customer
            else:
                unsatisfied += customer
            
            if minutes <= i:
                unsatisfied -= customers[i-minutes] * grumpy[i-minutes]
            
            ownerTechnique = max(ownerTechnique, unsatisfied)
        
        return satisfied + ownerTechnique

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        pocket = []
        for bill in bills:
            if bill == 5:
                pocket.append(bill)
            elif bill == 10:
                if 5 in pocket:
                    pocket.remove(5)
                    pocket.append(bill)
                else:
                    return False
            elif bill == 20:
                if 10 in pocket:
                    if 5 in pocket:
                        pocket.remove(10)
                        pocket.remove(5)
                    else:
                        return False
                elif 5 in pocket:
                    pocket.remove(5)
                    if 5 in pocket:
                        pocket.remove(5)
                        if 5 in pocket:
                            pocket.remove(5)
                        else:
                            return False
                    else:
                        pocket.append(5)
                        return False

                else:
                    return False

        return True
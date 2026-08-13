class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = tens = 0
        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                if not fives:
                    return False
                fives -= 1
                tens += 1
            else: # $20 bill
                if not fives:
                    return False
                if tens: # fives and tens
                    fives -= 1
                    tens -= 1
                else:
                    if fives < 3:
                        return False
                    fives -= 3

        
        return True
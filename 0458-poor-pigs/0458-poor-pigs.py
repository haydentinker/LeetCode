class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        testAttempts=minutesToTest/minutesToDie+1
        pigs=0
        while(testAttempts**pigs<buckets):
            pigs+=1

        return pigs
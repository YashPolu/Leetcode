class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost):
            return -1
        
        curr,index = 0,0
        c = 0
        for i,ii in zip(gas,cost):
            curr+= i-ii
            if curr < 0:
                index = c+1
                curr = 0
            c+=1
        
        return index
            
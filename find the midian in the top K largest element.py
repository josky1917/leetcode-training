import heapq

class Solution:

    def __init__(self, k):
        self.k_largest_number = []
        self.remain_number = []
        self.size = k
    
    def add_number(self, num):
        heapq.heappush(self.k_largest_number, -heapq.heappushpop(self.remain_number, -num))
        if len(self.k_largest_number) > self.size:
            temp = heapq.heappop(self.k_largest_number)
            heapq.heappush(self.remain_number, -temp)
    
    def output_klargest_number(self):
        return self.k_largest_number[0]

x = Solution(3)
x.add_number(2)
x.add_number(3)
x.add_number(4)
x.add_number(8)
x.add_number(1)
print(x.output_klargest_number())
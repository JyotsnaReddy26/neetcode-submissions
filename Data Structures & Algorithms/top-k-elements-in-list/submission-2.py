class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dicto = {}

        for num in nums:
            if num in dicto:
                dicto[num] += 1
            else:
                dicto[num] = 1

        sorted_items = sorted(dicto.items(), key=lambda x: x[1], reverse=True)

        arr = []
        for i in range(k):
            arr.append(sorted_items[i][0])

        return arr
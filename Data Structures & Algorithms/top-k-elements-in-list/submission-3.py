class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts: dict[int,int] = {}
        max_count: int = 0
        for num in nums:
            temp: int = counts.get(num,0)+1
            counts[num] = temp
            max_count = max(max_count, temp)

        bucket_sort: list[list[int]] = [[] for _ in range(max_count + 1)]
        for key, value in counts.items():
            bucket_sort[value].append(key)
        
        result: list[int] = []
        for i in reversed(range(len(bucket_sort))):
            if(len(bucket_sort[i]) > 0):
                for num in bucket_sort[i]:
                    result.append(num)
                if(len(result) == k):
                    break
        return result
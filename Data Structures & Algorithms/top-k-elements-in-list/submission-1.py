class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # frequency map
        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1

        # buckets
        freq = [[] for _ in range(len(nums) + 1)]

        # place numbers into buckets
        for n, c in count.items():
            freq[c].append(n)

        res = []

        # traverse buckets backwards
        for i in range(len(freq) - 1, 0, -1):

            for n in freq[i]:
                res.append(n)

                if len(res) == k:
                    return res
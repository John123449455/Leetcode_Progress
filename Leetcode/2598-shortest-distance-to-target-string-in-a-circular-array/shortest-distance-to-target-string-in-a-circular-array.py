class Solution(object):
    def closestTarget(self, words, target, startIndex):
        """
        :type words: List[str]
        :type target: str
        :type startIndex: int
        :rtype: int
        """
        ans = float('inf')
        for i in range(len(words)):
            if words[i] == target:
                distance = min(abs(i - startIndex), len(words) - abs(i - startIndex))
                ans = min(ans, distance)

        if ans != float('inf'): 
            return ans
        else: 
            return -1


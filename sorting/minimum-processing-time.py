class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort()
        processorTime.reverse()
        result = []
        for i in range(len(processorTime)):
            result.append(processorTime[i] + tasks[4 * (i + 1) - 1])
        return max(result)
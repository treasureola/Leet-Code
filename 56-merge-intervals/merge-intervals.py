class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        ret = [intervals[0]]
        
        for i in range(1, len(intervals)):
            # Compare current interval end with next interval start
            if ret[-1][1] >= intervals[i][0]:
                # Merge by updating the end of the last interval in result
                ret[-1][1] = max(ret[-1][1], intervals[i][1])
            else:
                # No overlap, add as new interval
                ret.append(intervals[i])
        return ret
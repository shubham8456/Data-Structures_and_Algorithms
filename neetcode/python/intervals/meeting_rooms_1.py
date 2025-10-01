# https://leetcode.com/problems/meeting-rooms/description/
# https://neetcode.io/problems/meeting-schedule?list=blind75

from typing import List

# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)

        itr = 1
        while itr < len(intervals):
            if intervals[itr].start < intervals[itr-1].end:
                return False
            itr += 1
        return True


# Usage
intervals = [Interval(5, 10), Interval(0, 4)]
result = Solution().canAttendMeetings(intervals)
print(result)

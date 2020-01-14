class Solution:
    def minTimeToVisitAllPoints(self, points: [[int]]) -> int:
        min_time = 0;
        x = points[0][0]
        y = points[0][1]

        for i in range(1, len(points)):
            next_x = points[i][0]
            next_y = points[i][1]
            min_time += max(abs(next_x - x), abs(next_y - y))
            x = next_x
            y = next_y

        return min_time

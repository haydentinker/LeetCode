from bisect import bisect_left

class Solution:
    def maxDistance(self, side, points, k):
        def convert_point_to_1d(x, y):
            if x == 0:
                return y
            elif y == side:
                return side + x
            elif x == side:
                return 3 * side - y
            else:
                return 4 * side - x

        arr = [convert_point_to_1d(x, y) for x, y in points]
        arr.sort()

        def check_for_valid(distance):
            perimeter = side * 4
            for start in arr:
                end = start + perimeter - distance
                cur = start
                for _ in range(k - 1):
                    idx = bisect_left(arr, cur + distance)
                    if idx == len(arr) or arr[idx] > end:
                        cur = -1
                        break
                    cur = arr[idx]
                if cur >= 0:
                    return True
            return False

        left, right = 0, side
        ans = 0

        while left <= right:
            mid = (left + right) // 2

            if check_for_valid(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
        
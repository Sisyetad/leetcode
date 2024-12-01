class Solution:
    from typing import List

    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Find the maximum height to determine the range of the counting array
        max_height = max(heights)
        min_height = min(heights)
        range_of_heights = max_height - min_height + 1

        # Create the count array and initialize it to zero
        count = [0] * range_of_heights

        # Create an array for sorted heights and names
        sorted_heights = [0] * len(heights)
        sorted_names = [None] * len(names)

        # Populate the count array
        for height in heights:
            count[height - min_height] += 1

        # Accumulate the counts
        for i in range(1, len(count)):
            count[i] += count[i - 1]

        # Build the sorted heights and names arrays in reverse order (to handle stability)
        for i in range(len(heights) - 1, -1, -1):
            height = heights[i]
            index = count[height - min_height] - 1
            sorted_heights[index] = height
            sorted_names[index] = names[i]
            count[height - min_height] -= 1

        # Reverse the arrays to get the descending order of heights
        return sorted_names[::-1]

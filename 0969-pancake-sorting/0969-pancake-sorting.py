class Solution:
    def pancakeSort(self, arr):
        flip = []
        n = len(arr)

        while n > 1:
            # Find the maximum value and its index in the current range
            max_value = max(arr[:n])
            max_index = arr.index(max_value)

            # If the maximum value is not already at its correct position
            if max_index != n - 1:
                # Flip the maximum value to the front
                if max_index > 0:
                    arr[:max_index + 1] = arr[:max_index + 1][::-1]
                    flip.append(max_index + 1)
                
                # Flip the maximum value to its correct position
                arr[:n] = arr[:n][::-1]
                flip.append(n)
            
            # Reduce the range of the array to process
            n -= 1

        return flip
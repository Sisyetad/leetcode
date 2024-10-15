class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Function to build a max heap
        def heapify(nums, n, i):
            largest = i  # Initialize largest as root
            left = 2 * i + 1  # Left child
            right = 2 * i + 2  # Right child

            # If left child is larger than root
            if left < n and nums[left] > nums[largest]:
                largest = left

            # If right child is larger than largest so far
            if right < n and nums[right] > nums[largest]:
                largest = right

            # If largest is not root, swap and continue heapifying
            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]
                # Recursively heapify the affected sub-tree
                heapify(nums, n, largest)

        # Build a maxheap
        for i in range(n // 2 - 1, -1, -1):
            heapify(nums, n, i)

        # Extract elements one by one from the heap
        for i in range(n - 1, 0, -1):
            # Move current root (largest) to the end
            nums[i], nums[0] = nums[0], nums[i]
            # Call heapify on the reduced heap
            heapify(nums, i, 0)

        return nums

public class Solution {
    public int splitArray(int[] nums, int m) {
        int start = 0;
        int end = 0;
        
        // Determine the range of possible answers
        for (int i = 0; i < nums.length; i++) {
            start = Math.max(start, nums[i]); // Max single element in the array
            end += nums[i]; // Sum of all elements in the array
        }
        
        // Binary search to find the minimum largest subarray sum
        while (start < end) {
            int mid = start + (end - start) / 2;
            int sum = 0;
            int pieces = 1;
            
            for (int num : nums) {
                if (sum + num > mid) {
                    // Create a new subarray if the current sum exceeds mid
                    sum = num;
                    pieces++;
                } else {
                    sum += num;
                }
            }
            
            if (pieces > m) {
                start = mid + 1; // Increase the allowed subarray sum
            } else {
                end = mid; // Try for a smaller allowed subarray sum
            }
        }
        
        return end; // Or return start, since start == end
    }
}

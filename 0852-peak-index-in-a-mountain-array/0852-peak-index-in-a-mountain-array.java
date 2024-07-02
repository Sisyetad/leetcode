import static java.lang.Integer.MIN_VALUE;

class Solution {
    public int peakIndexInMountainArray(int[] arr) {
        int start = 0;
        int end = arr.length - 1;
        
        while (start < end) {
            int mid = start + (end - start) / 2;
            if (arr[mid] < arr[mid + 1]) {
                // We are ascending, peak lies to the right
                start = mid + 1;
            } else {
                // We are descending, peak lies to the left
                end = mid;
            }
        }
        
        // At the end of the loop, start and end will be equal and point to the peak element
        return start;
    }
}

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        # Helper function for backtracking
        def backtrack(start, seen_substrings):
            # If we have reached the end of the string, return the number of unique substrings
            if start == len(s):
                return len(seen_substrings)
            
            max_splits = 0
            # Try splitting the string at every possible position
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                
                # If the substring is unique, add it to the set and recurse
                if substring not in seen_substrings:
                    seen_substrings.add(substring)
                    # Recurse to find the number of unique substrings from the current split
                    max_splits = max(max_splits, backtrack(end, seen_substrings))
                    # Backtrack: remove the substring to try other splits
                    seen_substrings.remove(substring)
            
            return max_splits
        
        # Start the backtracking from the first character with an empty set of seen substrings
        return backtrack(0, set())

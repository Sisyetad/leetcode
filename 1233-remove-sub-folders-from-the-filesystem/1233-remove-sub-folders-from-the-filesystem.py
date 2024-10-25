from typing import List

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # Sort the folders lexicographically
        folder.sort()
        
        # Initialize the result list with the first folder
        result = []
        
        for f in folder:
            # Check if current folder is a sub-folder of the last added folder
            if not result or not f.startswith(result[-1] + '/'):
                result.append(f)
        
        return result

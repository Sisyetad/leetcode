class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        n=len(heights)
        #l=1
        #r=n-1
        #while(l<=r):
         # //  if(heights[l-1]<=heights[l]):
          #  //    l+=1
           # //else:
            #  //  if(heights[r]<heights[l-1]):
             #  //     tem=heights[l-1]
              #    //  heights[l-1]=heights[r]
               #     //heights[r]=tem
                #//r-=1
       
    
    
    
        expected = sorted(heights)
        count = 0
        for i in range(n):
            if heights[i] != expected[i]:
                count += 1
        return count

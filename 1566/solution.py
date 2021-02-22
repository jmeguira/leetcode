class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        
        #sanity check for problem constraints
        if (k*m > len(arr)) or (k > len(arr)) or (m > len(arr)):
            return(False)
        
        for i in range(len(arr)):
            count = 1
            curr = []
            prev = []
            for j in range(i, len(arr), m):
                #check if available remaining integers at least one sequence long
                if (len(arr) - j < m):
                    break
                #current sequence slice
                curr = arr[j:j+m]
                #check against last sequence slice
                if (curr == prev):
                    count += 1
                #reset counter otherwise
                else:
                    count = 1
                if count >= k:
                    return(True)
                prev = curr

        return(False)
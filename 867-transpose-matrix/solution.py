class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ret = []
        
        i, j = 0, 0
        while j < len(matrix[0]):
            l = []
            while i < len(matrix):
                l.append(matrix[i][j])
                i += 1
                
            ret.append(l)
            j += 1
            i = 0
            
        return ret

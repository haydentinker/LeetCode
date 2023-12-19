class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n=len(img),len(img[0])
         
        result=[[0]*n for i in range(m)]

        for i in range(m):
            for j in range(n):
                count=0
                total=0
                for x in range(i-1,i+2):
                    for y in range(j-1,j+2):
                        print(x,y)
                        if 0<=x<m and 0<=y<n:
                            total+=img[x][y]
                            count+=1
                
                result[i][j]=total//count
        return result
        
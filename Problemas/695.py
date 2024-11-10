class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        Linhas, Colunas = len(grid) , len(grid[0])
        visit = set()
        
        def dfs(l,c):
            if(l < 0 or l == Linhas or c<0 or c == Colunas or grid[l][c] == 0 or (l,c) in visit):
                return 0
            visit.add((l,c))
            return (1 + dfs(l + 1 ,c) + dfs(l - 1 ,c) + dfs(l ,c +1 ) +dfs(l ,c - 1))
        area = 0
        for l in range(Linhas):
            for c in range(Colunas):
                area= max(area,dfs(l,c))
        return area 
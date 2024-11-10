class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def eh_valido(linha, coluna):
            return (0 <= linha < len(grid) and 
                    0 <= coluna < len(grid[0]) and 
                    grid[linha][coluna] == 1 and 
                    (linha, coluna) not in visitados)
        
        def dfs_iterativo(linha, coluna):
            pilha = [(linha, coluna)]
            area = 0
            
            while pilha:
                x, y = pilha.pop()
                if (x, y) in visitados:
                    continue
                
                visitados.add((x, y))
                area += 1
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nova_linha, nova_coluna = x + dx, y + dy
                    if eh_valido(nova_linha, nova_coluna):
                        pilha.append((nova_linha, nova_coluna))
            
            return area
        
        visitados = set()
        maior_area = 0
        
        for linha in range(len(grid)):
            for coluna in range(len(grid[0])):
                if grid[linha][coluna] == 1 and (linha, coluna) not in visitados:
                    maior_area = max(maior_area, dfs_iterativo(linha, coluna))
        
        return maior_area
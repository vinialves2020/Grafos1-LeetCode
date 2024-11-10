class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def calculaSoma(root):
            if not root:
                return 0
            
            somaEsquerda = max(calculaSoma(root.left), 0)
            somaDireita = max(calculaSoma(root.right), 0)
            
            somaAtual = root.val + somaEsquerda + somaDireita
            atualizaResultado(somaAtual)
            
            return root.val + max(somaEsquerda, somaDireita)
        
        def atualizaResultado(somaAtual):
            maiorSoma[0] = max(maiorSoma[0], somaAtual)
        
        maiorSoma = [float('-inf')]  
        calculaSoma(root)
        return maiorSoma[0]
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        conjunto_palavras = set(wordList)  
        if endWord not in conjunto_palavras:
            return 0
        
        fila = deque([(beginWord, 1)])  
        
        while fila:
            palavra_atual, comprimento = fila.popleft()
            
            for i in range(len(palavra_atual)):
                for letra in 'abcdefghijklmnopqrstuvwxyz':
                    nova_palavra = palavra_atual[:i] + letra + palavra_atual[i+1:]
                    
                    if nova_palavra == endWord:
                        return comprimento + 1
                    
                    if nova_palavra in conjunto_palavras:
                        conjunto_palavras.remove(nova_palavra)  
                        fila.append((nova_palavra, comprimento + 1))
        
        return 0
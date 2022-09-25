# A solucao deve estar implementada dentro da função abaixo.
# Dica: Você pode criar outras funções e classes se quiser mas esta é a função principal que será usada.


class MySolution:
    board = None
    def solution(self, board, word):  
        self.board = board
        
        if not len(word):
            return False
        
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                if self.board[x][y] == word[0]:
                    move = (x, y)
                    if self.deep_first_search(move, [move], word, 0):
                        return True

        return False       
    
    def deep_first_search(self, position, visited_position, word, index):   
        if index >= len(word) - 1:
            return True
        
        x, y = position
        
        possible_moves = [(x+1, y),  (x-1, y), (x, y+1), (x, y-1)]
        max_x = len(self.board)
        max_y = len(self.board[0])
        
        print(visited_position)
        print(possible_moves)
        for move_x, move_y in possible_moves:
            if move_x >= 0 and move_x < max_x and move_y >= 0 and move_y < max_y:
                if self.board[move_x][move_y] == word[index + 1]:
                    if (move_x, move_y) not in visited_position:
                        next_move = (move_x, move_y)
                        if self.deep_first_search(next_move, visited_position + [next_move], word, index+1):
                            return True
        return False                 
                
board = [
          ['A','B','C','E'],  
          ['S','F','C','S'],    
          ['A','D','E','E']
        ]
w = 'ABCCED'
c = MySolution().solution(board, w)
print(c)
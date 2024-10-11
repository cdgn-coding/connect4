class Connect4:
    def __init__(self):
        self.currentPlayer = 1
        self.grid = []
        for i in range(6):
            self.grid.append([0] * 6)
        self.lastPlayed = (None, None)

    def canPlaceToken(self, pos: int) -> bool:
        return self.grid[0][pos] == 0

    def placeToken(self, pos: int):
        i = 0
        while  i < 6 and self.grid[pos][i] == 0:
            i+=1

        self.grid[pos][i-1] = self.currentPlayer
        self.lastPlayed = (pos, i-1)
        
        print(self.lastPlayed)


    def render(self):
        # check vertical
        for i in range(6):
            for j in range(6):
                print(self.grid[j][i], end=' ')
            print()

    def horizontalConnected(self):
        x,y = self.lastPlayed

        connected = 1
        i = 1
        while x + i < 6 and self.grid[x+i][y] == self.currentPlayer:
            connected += 1
            i += 1
        i = 1
        while x - i >= 0 and self.grid[x-i][y] == self.currentPlayer:
            connected += 1
            i += 1
        return connected

    def verticalConnected(self):
        x,y = self.lastPlayed
        connected = 1
        i = 1
        while y + i < 6 and self.grid[x][y+i] == self.currentPlayer:
            connected += 1
            i += 1
        i = 1
        while y - i >= 0 and self.grid[x][y-i] == self.currentPlayer:
            connected += 1
            i -= 1
        return connected
    
    def diagonal(self):
        x,y = self.lastPlayed
        connected = 1
        i = 1
        while x - i >= 0 and y + i < 6 and self.grid[x-i][y+i] == self.currentPlayer:
            connected += 1
            i += 1
        i = 1
        while x + i < 6 and y - i >= 0 and self.grid[x+i][y-i] == self.currentPlayer:
            connected += 1
            i += 1
        return connected

    def finished(self):
        if self.isFirstTurn():
            return False
        return self.horizontalConnected() == 4 or self.verticalConnected() == 4 or self.diagonal() >= 4
    
    def isFirstTurn(self):
        return self.lastPlayed == (None, None)

    def winner(self):
        return self.currentPlayer

    def changePlayer(self):
        self.currentPlayer = 1 if self.currentPlayer == 2 else 2


game = Connect4()
game.render()
while True:
    print('turno del jugador', game.currentPlayer)
    pos = int(input('selecciona posicion: '))
    # leer posicion del jugador
    game.placeToken(pos)
    game.render()
    if game.finished():
        print('el ganador es', game.winner())
        break
    game.changePlayer()
    print()
    print()


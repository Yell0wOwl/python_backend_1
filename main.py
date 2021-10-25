import sys


class TicTac:
    global SIZE
    global WIN_SIZE
    global SECOND_NAME
    global FIRST_NAME
    global board
    
    def show_board(self):
        print('  ', end='')
        for i in range(self.SIZE):
            print(' ', i + 1, end='')
        for i in range(self.SIZE):
            print('\n', i + 1, end='')
            for j in range(self.SIZE):
                print(' ', self.board[i][j], end='')

    def turn(self, player):
        if player == 1:
            print('Ход игрока', self.FIRST_NAME, '\n')
            self.show_board()
            print('\nВведите номер строки и столбца, чтобы поставить туда X:')
            coordinates = self.paint()
            self.board[coordinates[0]][coordinates[1]] = 'X'
            self.check_winner(1, coordinates)
            self.turn(2)
        if player == 2:
            print('Ход игрока', self.SECOND_NAME, '\n')
            self.show_board()
            print('\nВведите номер строки и столбца, чтобы поставить туда O:')
            coordinates = self.paint()
            self.board[coordinates[0]][coordinates[1]] = 'O'
            self.check_winner(2, coordinates)
            self.turn(1)

    def start_game(self):
        print('Введите размер поля: ')
        try:
            self.SIZE = int(input())
        except ValueError:
            sys.exit('Необходимо ввести целое число!')
        print('Введите размер линии для победы: ')
        try:
            self.WIN_SIZE = int(input())
        except ValueError:
            sys.exit('Необходимо ввести целое число!')
        print('Введите имя первого игрока:')
        self.FIRST_NAME = input()
        print('Введите имя второго игрока:')
        self.SECOND_NAME = input()
        self.board = [['*' for i in range(self.SIZE)] for j in range(self.SIZE)]
        self.turn(1)

    def paint(self):
        is_valid = 0
        coordinates = [-1, -1]
        while is_valid == 0:
            try:
                print('Строка:', end='')
                coordinates[0] = int(input()) - 1
                print('Столбец:', end='')
                coordinates[1] = int(input()) - 1
                if(coordinates[0] >= self.SIZE or coordinates[1] >= self.SIZE):
                    print('Укажите клетку в пределах поля!')
                    continue
                is_valid = 1
            except ValueError:
                print('Необходимо ввести целые числа!')
                continue
        return coordinates

    def check_line(self, player, coordinates, dy, dx):
        def requisition(next_coord_y, next_coord_x):
            return next_coord_x < 0 or next_coord_x >= self.SIZE or next_coord_y < 0 or next_coord_y >= self.SIZE
        if player == 1:
            symbol = 'X'
        else:
            symbol = 'O'
        counter = 1
        next_coord_y = coordinates[0] + dy
        next_coord_x = coordinates[1] + dx
        if not requisition(next_coord_y, next_coord_x):
            while self.board[next_coord_y][next_coord_x] == symbol:
                counter += 1
                next_coord_y += dy
                next_coord_x += dx
                if requisition(next_coord_y, next_coord_x):
                    break
        next_coord_y = coordinates[0] - dy
        next_coord_x = coordinates[1] - dx
        if not requisition(next_coord_y, next_coord_x):
            while self.board[next_coord_y][next_coord_x] == symbol:
                counter += 1
                next_coord_y -= dy
                next_coord_x -= dx
                if requisition(next_coord_y, next_coord_x):
                    break
        if counter >= self.WIN_SIZE:
            if player == 1:
                print("Победил", self.FIRST_NAME)
            else:
                print("Победил", self.SECOND_NAME)
            sys.exit("Конец игры!")

    def check_winner(self, player, coordinates):
        self.check_line(player, coordinates, 1, 1)
        self.check_line(player, coordinates, 1, -1)
        self.check_line(player, coordinates, 1, 0)
        self.check_line(player, coordinates, 0, 1)


if __name__ == '__main__':
    game = TicTac()
    game.start_game()

import sys
import time


class TicTac:
    global SIZE
    global WIN_SIZE
    global SECOND_NAME
    global FIRST_NAME
    global turn_counter
    global board

    # Выводит в консоль игровую доску
    def show_board(self):
        print('  ', end='')
        for i in range(self.SIZE):
            print(' ', i + 1, end='')
        for i in range(self.SIZE):
            print('\n', i + 1, end='')
            for j in range(self.SIZE):
                print(' ', self.board[i][j], end='')

    # Ход игрока. Ставит символ в выбранном месте.
    def turn(self, player):
        if self.turn_counter == self.SIZE ** 2:
            self.show_board()
            time.sleep(0.5)
            sys.exit('\nНичья!')
        if player == 0:
            symbol = 'X'
            print('Ход игрока', self.FIRST_NAME, '\n')
        else:
            symbol = 'O'
            print('Ход игрока', self.SECOND_NAME, '\n')
        self.show_board()
        print(f'\nВведите номер строки и столбца, чтобы поставить туда {symbol}:')
        while True:
            coordinates = self.get_coordinates()
            if self.board[coordinates[0]][coordinates[1]] == '*':
                break
            print('Выберите свободное поле!')
        self.board[coordinates[0]][coordinates[1]] = symbol
        self.turn_counter += 1
        win = self.check_winner(player, coordinates)
        if not win:
            self.turn(not player)

    # Старт игры. Выбор размеров поля, необходимой
    # для победы длины линии, имен игроков.
    # Создание поля.
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
        self.turn_counter = 0
        self.turn(0)

    # Получения координат выбранной игроком точки.
    def get_coordinates(self):
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

    # Проверка одной из выигрышных комбинаций.
    def check_line(self, player, coordinates, dy, dx):
        def requisition(next_coord_y, next_coord_x):
            return next_coord_x < 0 or next_coord_x >= self.SIZE or next_coord_y < 0 or next_coord_y >= self.SIZE
        if player == 0:
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
            self.show_board()
            if player == 0:
                print("\nПобедил", self.FIRST_NAME)
            else:
                print("\nПобедил", self.SECOND_NAME)
            return 1
        return 0

    # Проверка условий победы. Ищет на поле все
    # возможные выигрышные комбинации.
    def check_winner(self, player, coordinates):
        win = 0
        win += self.check_line(player, coordinates, 1, 1)
        win += self.check_line(player, coordinates, 1, -1)
        win += self.check_line(player, coordinates, 1, 0)
        win += self.check_line(player, coordinates, 0, 1)
        return win


if __name__ == '__main__':
    game = TicTac()
    game.start_game()

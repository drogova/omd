import functools
from typing import Optional, Callable, List, Text, Any, NoReturn


def print_matrix(matrix: List[List[int]],
                 matrix_size: int,
                 matrix_axis: List[Text]) -> NoReturn:
    """Print playground field"""
    row_border = '  ' + ('----' * matrix_size)
    values_dict = {
        0: '   ',
        1: ' X ',
        -1: ' 0 '
    }
    print('   ' + '   '.join([str(i + 1) for i in range(matrix_size)]))
    for i in range(matrix_size):
        print(matrix_axis[i] + ' ' + '|'.join([str(values_dict[matrix[i][j]])
                                               for j in range(matrix_size)]))
        if i != matrix_size - 1:
            print(row_border)


def to_play_view(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator function to print playground field"""
    @functools.wraps(func)
    def decorated(*args, **kwargs) -> Any:
        print(f'Make your move Player {args[0].current_player}:')
        print_matrix(args[0].matrix, args[0]._matrix_size, args[0]._matrix_axis)
        return func(*args, **kwargs)
    return decorated


class TicTacToeGame:

    def __init__(self, matrix_size: Optional[int] = 3) -> NoReturn:
        """Initialize game parameters"""
        self._matrix_size = matrix_size
        self._matrix_axis = ['a', 'b', 'c', 'd', 'e'][:matrix_size]
        self.matrix = [[0 for i in range(matrix_size)] for i in range(matrix_size)]
        self.moves_left = matrix_size ** 2
        self._player_dict = {
            1: 1,
            2: -1
        }
        self.current_player = 1

    def check_input_index(self, input_index: Text) -> bool:
        """Validate input index"""
        input_index = input_index.lower()
        if (len(input_index) > 2
                or not input_index[0] in self._matrix_axis
                or not 0 < int(input_index[1]) <= self._matrix_size
                or self.matrix[self._matrix_axis.index(input_index[0])][int(input_index[1]) - 1] != 0):
            print(f'Invalid input "{input_index}", plz try again')
            return False
        return True

    def get_rows_sum(self) -> List[int]:
        """Return sum of each row elements of a matrix"""
        return [sum(self.matrix[i]) for i in range(self._matrix_size)]

    def get_cols_sum(self) -> List[int]:
        """Return sum of each column elements of a matrix"""
        return [sum(i) for i in zip(*self.matrix)]

    def get_main_diagonal_sum(self) -> int:
        """Return sum of main diagonal elements of a matrix"""
        return sum([self.matrix[i][i] for i in range(self._matrix_size)])

    def get_side_diagonal_sum(self) -> int:
        """Return sum of side diagonal elements of a matrix"""
        return sum([self.matrix[j][self._matrix_size - 1 - j]
                    for j in range(self._matrix_size)])

    def check_win(self) -> int:
        """Check for winning move"""
        if (self._matrix_size in self.get_rows_sum()
                or self._matrix_size in self.get_cols_sum()
                or self._matrix_size == self.get_main_diagonal_sum()
                or self._matrix_size == self.get_side_diagonal_sum()):
            return 1
        if (-1 * self._matrix_size in self.get_rows_sum()
                or -1 * self._matrix_size in self.get_cols_sum()
                or -1 * self._matrix_size == self.get_main_diagonal_sum()
                or -1 * self._matrix_size == self.get_side_diagonal_sum()):
            return 2
        return 0

    @to_play_view
    def make_move(self) -> int:
        """Make move in the game"""
        is_correct_input = False
        while not is_correct_input:
            input_index = input()
            is_correct_input = self.check_input_index(input_index)
        i_idx = self._matrix_axis.index(input_index[0])
        j_idx = int(input_index[1]) - 1
        value = self._player_dict[self.current_player]
        self.matrix[i_idx][j_idx] = value
        self.moves_left -= 1
        return self.check_win()

    def play(self) -> NoReturn:
        """Play the game"""
        is_win = 0
        while not is_win and self.moves_left != 0:
            is_win = self.make_move()
            if self.current_player == 1:
                self.current_player = 2
            else:
                self.current_player = 1
        print_matrix(self.matrix, self._matrix_size, self._matrix_axis)
        if is_win:
            print(f'\nPlayer {is_win} wins!')
        else:
            print('\nNo moves left, all lose. Game over.')


if __name__ == '__main__':
    matrix_size = 0
    while not 3 <= matrix_size <= 5:
        print('Plz enter matrix size between 3 and 5:')
        matrix_size = int(input())
    TicTacToeGame(matrix_size).play()

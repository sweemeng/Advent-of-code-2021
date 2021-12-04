from typing import List, Tuple, Callable


def parse(path: str) -> Tuple[List[str], List[List]]:
  game_input: List[str] = []
  boards: List[List] = []
  with open(path) as f:
    input_str = f.readline().replace("\n", "")
    game_input = input_str.split(",")
    temp_board = []
    for line in f:
      
      if line == "\n":
        boards.append(temp_board)
        temp_board = []
        continue
      board_line = line.replace("\n", "").split(" ")
      board_line = [i for i in board_line if i]
      boards[-1].extend(board_line)
  
  return game_input, boards


def get_horizontal_pos(line: int, row_size:int = 5) -> List[int]:
  first_item = line * row_size
  next_first = first_item + row_size
  return list(range(first_item, next_first))

def get_vertical_pos(line: int, col_size: int = 5, board_size: int=25) -> List[int]:
  # Step is the col size
  return list(range(line, board_size, col_size))


class Player:
  def __init__(self, board):
    self.board: List[str] = board
    self.marked: List[str] = []
    self.bingo = False
    self.last_number = None
  
  def check(self, item: str):
    if self.bingo:
      return
    if item in self.board:
      self.marked.append(item)
      if len(self.marked) >= 5:
        h_bingo = self.is_bingo(get_horizontal_pos)
        v_bingo = self.is_bingo(get_vertical_pos)
        if any((h_bingo,v_bingo)):
          self.bingo = True
          self.last_number = item
    
  def is_bingo(self, func: Callable):
    bingo = False
    for i in range(5):
      pos = func(i)
      check = [self.board[p] for p in pos if self.board[p] in self.marked]     
      if len(check) == 5:
        bingo = True
        break
    return bingo
  
  def print_result(self):
    unmarked = [int(i) for i in self.board if i not in self.marked]
    return sum(unmarked) * int(self.last_number)
      
      
  

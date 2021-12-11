from typing import List, Any
from itertools import product


def parse(path: str) -> List[str]:
  f = open(path)
  data = f.readlines()
  return [i.strip("\n") for i in data]


def is_minimum(height: int, adjuncts: List[int]) -> Any:
  check = lambda x: x > height 
  result = map(check, adjuncts)
  
  return all(result)


def make_map(data):
  result = {}
  row_size = len(data)
  col_size = len(data[0])
  for row, col in product(range(row_size), range(col_size)):
    result[(row,col)] = int(data[row][col])
  return result


def get_adjuncts_map(row, col, data_map):
  adjunct = [
    (-1, 0), 
    (0, -1),  (0, 1),
    (1, 0), 
  ]
  result = [(row+i, col+j) for i,j in adjunct]
  result = [i for i in result if i in data_map]
  
  return result
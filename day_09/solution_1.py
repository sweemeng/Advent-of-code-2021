from itertools import product
from day_09 import utils


def solution(path: str):
  data = utils.parse(path)
  row_size = len(data)
  col_size = len(data[0])
  total_risks = 0
  data_map = utils.make_map(data)
  for row, col in product(range(row_size), range(col_size)):
    target = data_map[(row, col)]
    adjunct_pos = utils.get_adjuncts_map(row, col, data_map)
    adjuncts = [data_map[(i, j)] for i, j in adjunct_pos]
    is_min = utils.is_minimum(target, adjuncts)
    if is_min:
      total_risks += target + 1
      print(target)
  print(total_risks)
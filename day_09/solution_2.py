from itertools import product
from day_09 import utils


def solution(path: str):
  data = utils.parse(path)
  row_size = len(data)
  col_size = len(data[0])
  results = []
  data_map = utils.make_map(data)
  for row, col in product(range(row_size), range(col_size)):
    target = data_map[(row, col)]
    adjunct_pos = utils.get_adjuncts_map(row, col, data_map)
    
    adjuncts = [data_map[(i,j)] for i, j in adjunct_pos]
    
    is_min = utils.is_minimum(target, adjuncts)
    
    if is_min:
      basin = grow_basin(row, col, data_map)
      results.append(len(basin))

  results.sort(reverse=True)
  print(results[0]*results[1]*results[2])

  
def grow_basin(row, col, data_map):
  neighbor = []
  adjuncts = climb_hill(row, col, data_map)
  neighbor += adjuncts
  working = neighbor
  length = len(working)
  floor = [(row, col)]
  while length != 0:
    neighbor = []
    for i, j in working:
      adjuncts = climb_hill(i, j, data_map)
      for a in adjuncts:
        if a not in floor:
          neighbor.append(a)
    for i in working:
      if i not in floor:
        floor.append(i)
    working = neighbor
    length = len(neighbor)
  return floor


def climb_hill(row, col, data_map):
  adjuncts = utils.get_adjuncts_map(row, col, data_map)
  value = data_map[(row, col)]
  
  adjuncts = [i for i in adjuncts if data_map[i] > value]
  adjuncts = [i for i in adjuncts if data_map[i] != 9]
  return adjuncts

  

  
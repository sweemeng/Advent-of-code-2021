from itertools import product

def make_map(data, size=10):
  result = {}
  row_size = size
  col_size = size
  for row, col in product(range(row_size), range(col_size)):
    result[(row,col)] = int(data[row][col])
  return result


def get_adjuncts_map(row, col, data_map):
  adjunct = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1),
  ]
  result = [(row+i, col+j) for i,j in adjunct]
  result = [i for i in result if i in data_map]
  
  return result


def print_data(data_map, size=10):
  
  count = 1
  for row, col in data_map:
    print(data_map[(row, col)], end=" ")
    count += 1
    if count > size:
      print("\n", end="")
      count = 1
  print("\n")


def flash(data_map):
  count = 0
  for row, col in data_map:
    value = data_map[(row, col)]
    if value > 9:
      count += 1
      data_map[(row, col)] = 0
  return count


def round(data_map):
  for row, col in data_map:
    steps(row, col, data_map)


def steps(row, col, data_map):
  # if it is 10, shine and spread
  # if it is > 10, it already shined
  value = data_map[(row, col)]
  if value >= 10:
    return
  value += 1
  data_map[(row, col)] = value
  if value >= 10:
    adjuncts = get_adjuncts_map(row, col, data_map)
    adjuncts = [adjunct for adjunct in adjuncts if data_map[adjunct] < 10]
    for arow, acol in adjuncts:
      steps(arow, acol, data_map)
    
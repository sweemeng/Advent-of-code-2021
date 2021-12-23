from day_13 import utils


def solution(path):
  instructions = utils.Instructions()
  instructions.parse(path)
  steps = instructions.step
  maps = instructions.maps
  for step in steps:
    direction, axis = step
    maps = instructions.fold_map(maps, direction, axis)

  utils.print_data(maps)

  
  
from day_13 import utils


def solution(path):
  instructions = utils.Instructions()
  instructions.parse(path)
  step = instructions.step[0]
  direction, axis = step
  maps = instructions.maps
  maps = instructions.fold_map(maps, direction, axis)
  print(len(maps))
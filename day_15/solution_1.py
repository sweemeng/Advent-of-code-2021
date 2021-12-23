from day_15 import utils

def solution(path):
  data, size = utils.parse(path)
  # utils.walk_simple(data, size)
  utils.dwalk_with_heap(data, size)
  
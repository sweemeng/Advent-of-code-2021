from day_three import utils
from copy import deepcopy
from typing import List, Callable


def solution(path):
  f = open(path)
  data = f.readlines()
  
  length = len(data[0])
  oxygen_rate = get_reading(data, length, max)
  co2_rate = get_reading(data, length, min)
  print(int(oxygen_rate, 2))
  print(int(co2_rate, 2))
  print(int(oxygen_rate, 2) * int(co2_rate, 2))

def get_reading(
  data: List, length: int, func: Callable
  ):
  working_data = deepcopy(data)
  for pos in range(length):
    count = utils.count_bytes(working_data)
    
    if count[pos]["0"] == count[pos]["1"]:
      selected_bit = str(func([0, 1]))
    else:
      selected_bit = func(count[pos], key=count[pos].get)
    working_data = select(working_data, selected_bit, pos)
    if len(working_data) == 1:
      break
  return working_data[0]


def select(data: List, bit_selected: str, pos: int):
  return [
    i for i in data if i[pos] == bit_selected
  ]


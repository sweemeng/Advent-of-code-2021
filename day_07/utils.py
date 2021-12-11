from functools import partial, lru_cache
from typing import List, Callable


def parse(path: str) -> List[int]:
  f = open(path)
  raw_data = f.read().strip("\n").split(',')
  return [int(i) for i in raw_data]

def get_fuel(origin:int, destination: int) -> int:
  move = destination - origin
  if move < 0:
    return -1 * move
  return move


def get_fuel_incremental(origin: int, destination: int) -> int:
  range_end = abs(destination - origin) + 1
  mid_num = range_end / 2
  return int((range_end - 1) * mid_num)


def get_fuels(
  data: List[int], destination: int, func: Callable=get_fuel) -> int:
  get_fuel_for_dest = lru_cache(maxsize=None)(partial(func, destination=destination))
  fuels = map(get_fuel_for_dest, data)
  return sum(fuels)



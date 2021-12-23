from day_15 import utils
import math

class ExtrapolatedMap:
  def __init__(self, basemap, basesize, x_factor=5):
    self.base = basemap
    self.base_size = basesize
    self.size = self.base_size * x_factor

  def extrapolated_value(self, row, col):
    rsector, rmod = self.count_sector(row, self.base_size)
    csector, cmod = self.count_sector(col, self.base_size)
    value = self.base[rmod, cmod] + rsector + csector
    if value > 9:
      value = value % 9
    return value
  
  def count_sector(self, pos, size):
    # row column, same maths, it's a square
    sector = 0
    if pos == 0:
      return sector, 0
    modulo = pos % size
    sector = math.floor(pos / size)
    return sector, int(modulo)
  
  def get(self, pos):
    row, col = pos
    if row < self.base_size and col < self.base_size:
      return self.base[row, col]
    return self.extrapolated_value(row, col)
  
def solution(path):
  data, size = utils.parse(path)
  # utils.walk_simple(data, size)
  x_map = ExtrapolatedMap(data, size)
  utils.dwalk_with_heap(x_map, x_map.size, print_mode=False)
  
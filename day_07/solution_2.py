from day_07 import utils


def solution(path: str):
  data = utils.parse(path)
  max_distance = max(data)
  fuel = utils.get_fuels(data, 0, func=utils.get_fuel_incremental)
  min_fuel = fuel
  for distance in range(1, max_distance + 1):
    fuel = utils.get_fuels(data, distance, func=utils.get_fuel_incremental)
    if fuel < min_fuel:
      min_fuel = fuel
    
  print(min_fuel)
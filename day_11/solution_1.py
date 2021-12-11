from day_11 import utils


def solution(path: str):
  data = []
  with open(path) as f:
    data = f.readlines()
    data = [i.strip("\n") for i in data]
  data_map = utils.make_map(data)
  flash_count = 0
  for _ in range(100):
    utils.round(data_map)
    flash_count += utils.flash(data_map)
    utils.print_data(data_map)
    print("\n")
    print("=======")
  print(flash_count)


  
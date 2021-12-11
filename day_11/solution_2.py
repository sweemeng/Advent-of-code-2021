from day_11 import utils
import os
import time

def solution(path: str, animate=True):
  data = []
  with open(path) as f:
    data = f.readlines()
    data = [i.strip("\n") for i in data]
  data_map = utils.make_map(data)
  flash_count = 0
  step = 0
  while True:
    step += 1
    utils.round(data_map)
    
    flash_count = utils.flash(data_map)
    print("Step:", step)
    utils.print_data(data_map)
    print("\n")
    if animate:
      time.sleep(0.01)
      os.system('clear')
    if flash_count == len(data_map):
      print("Step:", step)
      utils.print_data(data_map)
      break
      


  
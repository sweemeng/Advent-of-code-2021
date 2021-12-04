from day_03 import utils


def solution(path):
  counter = {}
  f = open(path)
  
  data = f.readlines()
  counter = utils.count_bytes(data)
  
  gamma_rate = utils.assemble_bytes(counter, max)
  
  epsilon_rate = utils.assemble_bytes(counter, min)
  print(gamma_rate)
  print(epsilon_rate)

  print(gamma_rate * epsilon_rate)
    
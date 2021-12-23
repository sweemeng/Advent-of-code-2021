from day_16 import utils


def solution(path=None):
  data="D2FE28"
  parser = utils.Parser(data)
  print(parser.bin_string)
  parser.parse()
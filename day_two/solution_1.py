from day_two.utils import parse_move


def main():
  point = (0, 0)
  with open("day_two/input.txt") as f:
    for move in f:
      new_point = parse_move(move, point)
      point = new_point
  v,h = point
  print(v*h)



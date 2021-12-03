from day_two.utils import parse_move_with_aim


def main():
  point = (0, 0, 0)
  with open("day_two/input.txt") as f:
    for move in f:
      new_point = parse_move_with_aim(move, point)
      point = new_point
      
  v,a,h = point
  print(v*h)



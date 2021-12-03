from typing import Tuple


def parse_move(move: str, point: Tuple[int, int]) -> Tuple[int, int]:
  direction, distance = move.split(" ")
  distance = int(distance)
  vertical, horizontal = point
  if direction == "forward":
    vertical += distance
  elif direction == "down":
    horizontal += distance
  elif direction == "up":
    horizontal -= distance
  return vertical, horizontal


def parse_move_with_aim(move: str, point: Tuple[int, int, int]) -> Tuple[int, int, int]:
  direction, distance = move.split(" ")
  distance = int(distance)
  vertical, aim, horizontal = point
  if direction == "forward":
    vertical += distance
    delta = distance * aim
    horizontal += delta
  elif direction == "down":
    aim += distance
  elif direction == "up":
    aim -= distance
  return vertical, aim, horizontal
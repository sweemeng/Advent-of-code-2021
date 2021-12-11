from typing import Generator


def parse(path: str) -> Generator:
  with open(path) as f:
    for item in f:
      temp = item.strip("\n")
      signal_str, digits_str = temp.split("|")
      signals = [i for i in signal_str.split(" ") if i]
      digits = [i for i in digits_str.split(" ") if i]
      yield signals, digits

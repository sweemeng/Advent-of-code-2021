from itertools import product


class Instructions:
  def __init__(self):
    self.maps = []
    self.folder = []
    self.step = []

  def parse(self, path):
    with open(path) as f:
      switch_mode = False
      for line in f:
        line = line.strip("\n")
        if not line: 
          switch_mode = True
          continue
        if switch_mode:
          _,_,i = line.split(" ")
          direct, axis = i.split("=")
          self.step.append((direct, int(axis)))
        else:
          x,y = line.split(",")
          self.maps.append((int(x), int(y)))
  
  def fold_map(self, maps, direction, axis):
    transforms = []
    if direction == "x":
      func = self.fold_x
    else:
      func = self.fold_y

    for x,y in maps:
      new_x, new_y = func(x, y, axis)
      if (new_x, new_y) not in transforms:
        transforms.append((new_x, new_y))
    return transforms
    

  def fold_x(self, x, y, axis):
    return self.fold(x, axis), y
  
  def fold_y(self, x, y, axis):
    return x, self.fold(y, axis)
  
  def fold(self, value, axis):
    if value <= axis:
      return value
    return axis - (value - axis)

def get_display_range(data):
  min_x = 1000
  min_y = 1000
  max_x = 0
  max_y = 0
  for x, y in data:
    if x > max_x:
      max_x = x
    if min_x > x:
      min_x = x
    if y > max_y:
      max_y = y
    if min_y > y:
      min_y = y
  min_x -= 1
  if min_x < 0:
    min_x = 0
  if min_y < 0:
    min_y = 0
  
  max_x += 1
  max_y += 1
  
  return (min_x, min_y), (max_x, max_y)
 
def print_data(data):
  mins, maxs = get_display_range(data)
  print(mins, maxs)
  min_x, min_y = mins
  max_x, max_y = maxs
  range_x = range(min_x, max_x)
  range_y = range(min_y, max_y)
  
  for y, x in product(range_y, range_x):
    if x == max_x - 1:
      end = "\n"
    else:
      end = ""
    if (x,y) in data:
      print("##", end=end)
    else:
      print("..", end=end)
      
    
    
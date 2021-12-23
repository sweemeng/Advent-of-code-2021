# store in string now,
hex_map = {
  "0": "0000",
  "1": "0001",
  "2": "0010",
  "3": "0011",
  "4": "0100",
  "5": "0101",
  "6": "0110",
  "7": "0111",
  "8": "1000",
  "9": "1001",
  "A": "1010",
  "B": "1011",
  "C": "1100",
  "D": "1101",
  "E": "1110",
  "F": "1111",
}




class Parser:
  def __init__(self, hex_string):
    self.hex_string = hex_string
    self.bin_string = hex2binary(hex_string)
    self.counter = 0
    self.stack = []
    self.start = True
    self.end = False
  
  def parse(self):
    while self.counter < len(self.bin_string):
      if self.start:
        packet_version = get_packet_version(self.bin_string[0:3])
        type_id = get_type_id(self.bin_string[3:6])
        length_id = None
        length = None # More like length remain
        count = None # More like token rmeains
        self.counter += 6
        
        if type_id == 4:
          # it's a literal
          pass

        else:
          # It's an ops
          length_id = int(self.bin_string[self.counter])
          # Ready to push meta data into the stack
          # Push in (packet_version, type_id, length_id, length, count)
          if length_id:
            pass
          else:
            pass
          



def hex2binary(hex_string):
  # not going to read a file this time
  s = ""
  for c in hex_string:
    s+=hex_map[c]
  return s
  

def get_packet_version(bin_string):
  return int(bin_string, base=2)
  

def get_type_id(bin_string):
  return int(bin_string, base=2)

  
  
def parse_operator(bin_string, length_id):
  if length_id:
    parse_operator_11bit(bin_string)
  else:
    parse_operator_15bit(bin_string)
  

def parse_operator_11bit(bin_string):
  pass


def parse_operator_15bit(bin_string):
  # 6th bit length type, 7 to 7 + 15 is length 
  length = int(bin_string[7:22], base=2)
    

def parse_literal(bin_string):
  cont = 1
  pos = 6
  result = ""
  while cont:
    s = bin_string[pos:pos+5]
    print(s)
    cont = int(s[0])
    print(s[1:])
    result += s[1:]
    pos = pos + 5
  print(result)
  print(int(result, base=2))
  return int(result, base=2)
      



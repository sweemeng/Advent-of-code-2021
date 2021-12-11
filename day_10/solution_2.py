from day_10 import utils

completion_score = {
  ")": 1,
  "]": 2,
  "}": 3,
  ">": 4, 
}

open_tokens = {
  "(": ")",
  "[": "]",
  "{": "}",
  "<": ">",
}

def complete_token(stack):
  cscore = 0
  
  for idx in range(len(stack)-1, -1, -1):
    token = stack[idx]
    close_token = open_tokens[token]
    score = completion_score[close_token]
    cscore = cscore * 5
    cscore += score
  return cscore

def solution(path: str):
  with open(path) as f:
    
    cscores = []
    for line in f:
      stack = []
      line = line.strip("\n")
      for c in line:
        if not stack:
          stack.append(c)
          continue
        if c in utils.close_tokens:
          test_c = utils.close_tokens[c]
          to_close = stack[-1]
          if test_c == to_close:
            stack.pop()
          else:
            stack = []
            break
        else:
          stack.append(c)
      if stack:
        cscore = complete_token(stack)
        cscores.append(cscore) 
    cscores.sort()
    ptr = int((len(cscores)) / 2)
    print(cscores[ptr])

          
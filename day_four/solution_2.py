from day_four import utils

def solution(path: str):
  game_input, boards = utils.parse(path)
  players: utils.Player = []
  for board in boards:
    player = utils.Player(board)
    players.append(player)
  
  ranks = []
  num_players = len(players)
  for i in game_input:
    if num_players == ranks:
        break
    for player_id in range(num_players):
      if player_id in ranks:
        continue
      player = players[player_id]
      player.check(i)
      if player.bingo:
        ranks.append(player_id)
  last_player_id = ranks[-1]
  result = players[last_player_id].print_result()
  print(result)
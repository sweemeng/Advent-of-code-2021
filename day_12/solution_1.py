from day_12 import utils


def solution(path):
  maps = utils.PathMaps()
  maps.parse(path)
  maps.build_tables()
  maps.walk("start")
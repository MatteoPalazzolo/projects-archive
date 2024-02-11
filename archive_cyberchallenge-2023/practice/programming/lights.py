import pwn, json, re, time

conn = pwn.remote('130.192.5.212', 1734)



def new_lamps_number(LENGHT, LAMP_RANGE, LAMP_POSITIONS) -> int:
  CORRIDOR = ['0'] * LENGHT
  for lp in LAMP_POSITIONS:
    i1 = lp - 1
    for i2 in range(-LAMP_RANGE, LAMP_RANGE+1):
      try:
        if i1+i2 >= 0:
            CORRIDOR[i1+i2] = '1'
      except IndexError:
        pass
      
  STR_CORRIDOR = ''.join(CORRIDOR)
  print(STR_CORRIDOR)
  k2 = (2*LAMP_RANGE)+1
  # print(k2)
  RE = re.findall('0{0,' + str(k2) + '}', STR_CORRIDOR)
  print(RE)

  NEW_LAMPS = 0
  for r in RE:
    if '0' in r:
      NEW_LAMPS += 1
      
  return NEW_LAMPS

def extract_data(T):
  LENGHT, LAMP_NUMBER, LAMP_RANGE, LAMP_POSITIONS = 0, 0, 0, []
  for t in T:
    if ('N = ' in t):
      LENGHT = int(t.replace('N = ', '').replace('\n', ''))
    elif ('M = ' in t):
      LAMP_NUMBER = int(t.replace('M = ', '').replace('\n', ''))
    elif ('K = ' in t):
      LAMP_RANGE = int(t.replace('K = ', '').replace('\n', ''))
    elif ('Lamp positions: ' in t):
      LAMP_POSITIONS = json.loads(t.replace('Lamp positions: ', '').replace('\n', ''))
  print(LENGHT, LAMP_RANGE, LAMP_POSITIONS)
  return (LENGHT, LAMP_RANGE, LAMP_POSITIONS)

try:
    for i in range(51):
        msg = conn.recvuntil(b'How many additional lamps?').decode().split('\n')
        num = new_lamps_number(*extract_data(msg))
        print('num: ', num)

        conn.sendline(str(num).encode())
        print(i)

except EOFError:
    conn.interactive()

# str_msg2 = ''.join(recvall(conn))
# print(str_msg2)
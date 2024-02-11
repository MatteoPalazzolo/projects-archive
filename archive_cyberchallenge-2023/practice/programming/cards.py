import pwn, itertools

conn = pwn.remote('130.192.5.212', 1733)

FILL = 999999999999

def playoff(DECKS):

  # if len(DECKS) <= 1 or len(DECKS[0]) < 1:
  #   return 0
  
  check = list(itertools.chain.from_iterable(DECKS))
  print(DECKS)
  print(check)

  if len(check) == 0:
    print("CHECK è lungo 0")
    return 0

  n = 0
  for c in check:
    if c != FILL:
      n = c
  if check.count(n) + check.count(FILL) == len(check):
    return check.index(n)


  max_len = max([len(d) for d in DECKS])
  for d in DECKS:
    while len(d) < max_len:
      d.append(FILL)

  comp = list(zip(*DECKS))
  for c in comp:
    b = min(c)
    if c.count(b) == 1:
      return c.index(b)
    else:
      new_deck = []
      for deck in DECKS:
        if deck[1:] == []:
          new_deck.append([FILL]*(max([len(d) for d in DECKS])-1))
        elif b == deck[0]:
          new_deck.append(deck[1:])
        else:
          new_deck.append([FILL]*(max([len(d) for d in DECKS])-1))
      return playoff(new_deck)


def main(DECKS):
  
  ## CAST TO INT
  DECKS = [[int(j) for j in i] for i in DECKS]

  out = []
  while True:
    # rimuovi mazzo se vuoto
    while [] in DECKS:
      DECKS.remove([])

    # pesca le prime tre carte da ogni mazzo
    draw = list(zip(*DECKS))[0]
    
    # scegli la più piccola e aggiungila alla lista
    val = min(draw)
    if draw.count(val) == 1:
      i = draw.index(val)
    else:
      new_deck = []
      for deck in DECKS:
        if deck[1:] == []:
          new_deck.append([FILL]*(max([len(d) for d in DECKS])-1))
        elif val == deck[0]:
          new_deck.append(deck[1:])
        else:
          new_deck.append([FILL]*(max([len(d) for d in DECKS])-1))
      i = playoff(new_deck)
    
    app = DECKS[i].pop(0)
    out.append(app)
    
    # se non ci sono più carte chiudi il ciclo
    if len(list(itertools.chain.from_iterable(DECKS))) <= 0:
      break

  return [str(o) for o in out]



conn.recvuntil(b'Now it\'s your turn!')

try:
  while True:
    msg = conn.recvuntil(b'What is the best possible "Solution sequence"?').decode()
    emsg = [c.split(' ') for c in msg.split('\n')[2:-3]]
    print('msg:', msg)
    print('list:', emsg)
    ans = main(emsg)
    print('ans:', ans)
    conn.sendline(" ".join(ans).encode())
    conn.recvuntil(b'Yes!\n')

except Exception as e:
  #raise(e)
  print('ERROR: ', e)
  conn.interactive()
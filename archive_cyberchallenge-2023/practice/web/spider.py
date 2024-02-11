import requests, bs4

visited_doors = []
pages = [
  {'door':'', 'key':''}
]

while len(pages) > 0:

  for i, p in enumerate(pages):
    print(len(pages))
    pages.remove(p)
    r = requests.get('http://130.192.5.212:48521/' + p['door'], cookies={'key': p['key']})

    if 'ptm{' in r.text or 'flag' in r.text:
      print(p, r.text) 

    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    td = [t.text for t in soup.find_all('td')[2:]]
    doors = td[::2]
    keys = td[1::2]
    for j in range(len(doors)):
      if doors[j] not in visited_doors:
        visited_doors.append(doors[j])
        pages.append({'door': doors[j], 'key': keys[j]})

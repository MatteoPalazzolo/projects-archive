import requests, random

r = requests.get('https://gist.githubusercontent.com/pzb/b4b6f57144aea7827ae4/raw/cf847b76a142955b1410c8bcef3aabe221a63db1/user-agents.txt')
user_agents = r.text.split('\n')
random_user_agent = random.choice(user_agents)

print(random_user_agent)
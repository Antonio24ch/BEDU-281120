import requests

#CONSTANTS
base_url = 'https://api.github.com/'

respose = requests.get(base_url)

#FUNCTION - construyendo la variable para consulta info del usuario
def get_github_user(username):
    url = f'{base_url}users/{username}'
    respose = requests.get(url)
    if respose.status_code == 200:
        return  respose.json() #para mandar traer función JSON
    return None

username = input('Give me a github username:\t')
user = get_github_user(username)
print(user)


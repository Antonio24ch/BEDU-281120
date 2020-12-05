import requests

#CONSTANTS
base_url = 'https://api.github.com/'

#respose = requests.get(base_url)

#FUNCTION - construyendo la variable para consulta info del usuario
def get_github_user(username):
    url = f'{base_url}users/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return  response.json() #para mandar traer función JSON
    return None

def download_github_user_avatar(avatar_url, username):
    response = requests.get(avatar_url)
    if response.status_code ==200:
        #download a file from internet
        response_content = response.content #objeto binario
        filename = f'tmp/{username}.png'
        with open(filename, 'wb') as image:#abreme un archivo que va a escribir en b(binario)cierto contenido
            image.write(response_content)
            return filename
    return None


username = input('Give me a github username:\t')
user = get_github_user(username)
ilename = download_github_user_avatar(user['avatar_url'], username)
print(filename)


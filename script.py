import requests
from bs4 import BeautifulSoup

page = requests.get("https://en.wikipedia.org/wiki/List_of_animal_names")

soup = BeautifulSoup(page.text, 'html.parser')

tables = soup.find_all('table',{'class':'wikitable'})

x=tables[1]
table = x.find('tbody')
results = {}
for row in table.find_all('tr'):
    cells = row.find_all('td') # data cells in 1 row
    if len(cells) > 2: # only the animal rows
        animal = cells[0].text.strip() # Animal
        collective_noun = cells[4].text.strip() # Collective noun
        if len(collective_noun) > 1:
            print(f"{animal} - {collective_noun}")
        
        else:
            collateral_adjective = cells[5].text.strip() # collateral adjective
            print(f"{animal} - {collateral_adjective}")


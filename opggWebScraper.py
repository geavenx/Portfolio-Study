import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}

region = input('(br, euw, eune, na, oce, kr)\nRegion: ')
nickname = input('Nickname: ')


url = f'https://www.op.gg/summoners/{region}/{nickname}'
page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.text, 'html.parser')

playerInfo = soup.find(id="content-container")
playerHeaderInfo = soup.find(id="content-header")

soloRank = playerInfo.find(class_="tier")
soloRankLp = playerInfo.find(class_="lp")
ladderRank = playerHeaderInfo.find(class_="ranking")
winrate = playerInfo.find(class_="ratio")
championBox = soup.find_all('div', class_="champion-box")

mostPlayedList = []
for champ in championBox:
    championName = champ.find('div', class_="name")
    mostPlayedList.append(championName.text)

print(f'SoloQueue rank: {soloRank.text}')
print(f'SoloQueue LP: {soloRankLp.text}')
print(f'Global ladder rank: {ladderRank.text.strip()}')
print(f'SoloQueue winrate: {winrate.text.strip()}')
print('Most played champions list: ')
for x in range(len(mostPlayedList)):
    print(f'{x + 1}.{mostPlayedList[x]}')

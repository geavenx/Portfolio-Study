import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}

mode = input('What do you want? Player data(P) or champion data(C)?\n> ')

class opggScraper:
    def __init__(self, mode):
        self.mode = mode
        
    def playerData(region, nickname):
        print('Started scrapping...\n')
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
            
    def championData(champ, role):
        print('Started scrapping...\n')
        url = f'https://www.op.gg/champions/{champ}/{role}/build'
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.text, 'html.parser')
        statistics = soup.find('div', class_='css-1cnh6jp ew1oorz8')
        numbers = statistics.find_all('div', class_='css-kjoz7i ew1oorz7')
        ratioList = []
        for stat in numbers:
            ratio = stat.find('div', class_='css-oxevym ew1oorz5')
            ratioList.append(ratio.text)
        print(f'Win rate: {ratioList[0]}\nPick rate: {ratioList[1]}\nBan rate: {ratioList[2]}')
        print(f'For further information access: {url}')
    
if __name__ == '__main__':
    if mode.upper() == 'P':
        region = input('(br, euw, eune, na, oce, kr)\nRegion: ')
        nickname = input('Nickname: ')
        print()
        opggScraper.playerData(region, nickname)
    elif mode.upper() == 'C':
        champ = input('Champion name > ')
        role = input('Which role > ')
        print()
        opggScraper.championData(champ, role)

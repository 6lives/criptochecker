from bs4 import BeautifulSoup
import requests, fake_useragent
import time



class Parser():
    def __init__(self):
        UsAg = fake_useragent.UserAgent()
        user = UsAg.random
        self.header = {'User-Agent': str(user)}
        url = input('coin: ')
        binance = True
        coinmarketcap = False
        while coinmarketcap:
            self.ipSite = f'https://coinmarketcap.com/currencies/{url}/'
            self.start()

        while binance:
            self.ipSite = f'https://www.binance.com/en/trade/{url}_USDT'
            self.startbinance()

    def start(self):
        adress = requests.get(self.ipSite, headers=self.header)
        soup = BeautifulSoup(adress.text, "html.parser")
        for tag in soup.find('td'):
            print(tag)
            time.sleep(6)

    def startbinance(self):
        adress = requests.get(self.ipSite, headers=self.header)
        soup = BeautifulSoup(adress.text, "html.parser")
        for tag in soup.find('title'):
            print(tag.split(' ')[0])
            time.sleep(6)




if __name__ == '__main__':
    Parser()

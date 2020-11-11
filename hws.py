import time
from colorama import init, Fore
import feedparser

init(autoreset=True)

def cool():
    while True:
        time.sleep(10)

        with open(f'hws.txt','r') as log:
            lastsent = log.read()

        Feed = feedparser.parse('https://www.reddit.com/r/hardwareswap/new/.rss')

        send = True

        for i in Feed.entries:

            if i.title == lastsent:
                send = False

            if send == True:
                print(Fore.BLUE + '\n~~~~~~~~~~~~~~~~~~~~~\n')
                print(Fore.BLUE + i.title)
                print(Fore.BLUE + i.authors[0].name)
                print(Fore.BLUE + str(i.updated_parsed[1]) + '/' + str(i.updated_parsed[2]) + '/' + str(i.updated_parsed[0]) + ', ' + str(i.updated_parsed[3])
                    + ':' + str(i.updated_parsed[4]) + ' UTC')

            if i == Feed.entries[0]:
                with open(f'hws.txt','w') as log:
                    log.write(str(i.title))
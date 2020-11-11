import time
from colorama import init, Fore
import feedparser

init(autoreset=True)

def cool():
    while True:
        time.sleep(10)
        
        with open(f'bapcs.txt','r') as log:
            lastsent = log.read()

        Feed = feedparser.parse('https://www.reddit.com/r/buildapcsales/new/.rss')

        send = True

        for i in Feed.entries:

            if i.title == lastsent:
                send = False

            if send == True:
                print(Fore.RED + '\n~~~~~~~~~~~~~~~~~~~~~\n')
                print(Fore.RED + i.title)
                print(Fore.RED + i.authors[0].name)
                print(Fore.RED + str(i.updated_parsed[1]) + '/' + str(i.updated_parsed[2]) + '/' + str(i.updated_parsed[0]) + ', ' + str(i.updated_parsed[3])
                    + ':' + str(i.updated_parsed[4]) + ' UTC')

            if i == Feed.entries[0]:
                with open(f'bapcs.txt','w') as log:
                    log.write(str(i.title))
from bs4 import BeautifulSoup
import urllib3
import sys

BASE_PAGE = "https://botrank.pastimes.eu/?sort=rank&page=" 
BASE_BOT_NAME =  sys.argv[1]
BOT_FOUND = False

http = urllib3.PoolManager()
print("Started searching, this might take a while.....")

for i in range(9999999999): # this number doesnt have to be any higher than 250 lol
    if i == 0:
        continue

    REQUEST_PAGE = BASE_PAGE + str(i)
    r = http.request("GET", REQUEST_PAGE)

    soup = BeautifulSoup(r.data, "html.parser")

    colums = soup.find_all("tr")

    if len(colums) == 1: # break if it reaches the last page
        break

    for element in range(len(colums)):
        
        PAGE_BOT_NAME = colums[element].a.get_text()

        if PAGE_BOT_NAME == "Rank":
            continue

        if PAGE_BOT_NAME == BASE_BOT_NAME:
            PAGE_BOT_RANK = colums[element].find_all("td")[0].get_text()
            PAGE_BOT_SCORE = colums[element].find_all("td")[2].get_text()
            PAGE_BOT_GOOD_VOTES = colums[element].find_all("td")[3].get_text()
            PAGE_BOT_BAD_VOTES = colums[element].find_all("td")[4].get_text()
            PAGE_BOT_COMMENT_KARMA = colums[element].find_all("td")[5].get_text()
            PAGE_BOT_LINK_KARMA = colums[element].find_all("td")[6].get_text()
            
            BOT_FOUND = True
            break

    if BOT_FOUND:
        break

if BOT_FOUND:
    print(f"\n\nFound bot {BASE_BOT_NAME} on page: \"{REQUEST_PAGE}\", here are the user/bot stats:")
    print(f"Bot Name: {PAGE_BOT_NAME}")
    print(f"Score: {PAGE_BOT_SCORE}")
    print(f"Good Bot Votes: {PAGE_BOT_GOOD_VOTES}")
    print(f"Bad Bot Votes: {PAGE_BOT_BAD_VOTES}")
    print(f"Comment Karma: {PAGE_BOT_COMMENT_KARMA} (this value might not be accurate)")
    print(f"Link Karma: {PAGE_BOT_LINK_KARMA} (this value migth not be accurate)")

else:
    print(f"Could not find user/bot: {BASE_BOT_NAME}")

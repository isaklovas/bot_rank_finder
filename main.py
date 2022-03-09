from bs4 import BeautifulSoup
import requests
import sys


def main():
    BASE_PAGE = "https://botrank.pastimes.eu/?sort=rank&page=" 

    if len(sys.argv) < 2:
        base_bot_name = input("Enter a reddit username: ")
    else:
        base_bot_name = sys.argv[1]

    print("Started searching, this might take a while...")
    for i in range(1, 999999999999): # this number doesnt have to be any higher than 250 lol
        request_page = BASE_PAGE + str(i)
        r = requests.get(request_page)

        soup = BeautifulSoup(r.text, "html.parser")

        colums = soup.find_all("tr")

        if len(colums) == 1:
            break

        for element in range(len(colums)):
            PAGE_BOT_NAME = colums[element].a.get_text()

            if PAGE_BOT_NAME == "Rank":
                continue

            if PAGE_BOT_NAME == base_bot_name:
                print(f"\nFound bot {base_bot_name} on page: \"{request_page}\", here are the user/bot stats:")
                print(f"Bot Name: {PAGE_BOT_NAME}")
                print(f"Bot Rank: {colums[element].find_all('td')[0].get_text().replace(',', '')}")
                print(f"Score: {colums[element].find_all('td')[2].get_text()}")
                print(f"Good Bot Votes: {colums[element].find_all('td')[3].get_text().replace(',', '')}")
                print(f"Bad Bot Votes: {colums[element].find_all('td')[4].get_text().replace(',', '')}")
                print(f"Comment Karma: {colums[element].find_all('td')[5].get_text().replace(',', '')}")
                print(f"Link Karma: {colums[element].find_all('td')[6].get_text().replace(',' , '')}")
                sys.exit()
    print(f"Could not find user/bot: {base_bot_name}")


if __name__ == "__main__":
    main()
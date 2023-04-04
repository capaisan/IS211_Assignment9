from bs4 import BeautifulSoup
import requests

def main():

    # Couldn't get this one to work in time.
    url = "https://secure.runescape.com/m=itemdb_oldschool/top100?list=1"

    result = requests.get(url)
    soup = BeautifulSoup(result.content, "html.parser")

    table = soup.find("table")
    rows = table.find_all("tr")
    # print(table)
    print("Rank\tPlayer\t\t\t\t\t\tPrice")

    for i, row in enumerate(rows):

        print(soup)
        print(table)
        print(rows)
        print(len(row))
        data = row.find_all("td")

        if len(data) >= 2:
            name = data[1].a.text.strip()
        else:
            name = "N/A"
        rank = i + 1
        name = data[1].a.text.strip()
        price = data[4].text.strip()




if __name__ == "__main__":

    main()
from bs4 import BeautifulSoup
import requests


def main():
    url = "https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/qualifiers/"

    result = requests.get(url)

    soup = BeautifulSoup(result.content, "lxml")

    table = soup.find("div", {"class": "TableBase"})

    # rows = table.find_all("tr")

    rows = table.find_all("tr", {"class": "TableBase-bodyTr"})

    # print(rows)

    #

    print("Rank\t\t\tPlayer\t\t\t\tPosition\t\t\tTeam\t\t\tTDs")

    for i, row in enumerate(rows[:20]):
        # if isinstance(row, str):  # check if row is a NavigableString

        #     continue

        data = row.find_all("td")

        # print(len(data))

        rank = i + 1

        name = data[0].text.strip().split('\n')[0].strip()

        position = data[0].text.strip().split('\n')[1].strip()

        team = data[0].text.strip().split('\n')[-1].strip()

        tds = data[8].text.strip()

        print(f"{rank}\t\t\t{name}\t\t\t\t{position}\t\t\t\t\t{team}\t\t\t\t\t{tds}")

        # print(name)

        # print(position)

        # print(team)

        # print(tds)


if __name__ == "__main__":
    main()
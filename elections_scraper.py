"""
elections_scraper.py: třetí projekt do Engeto Online Python Akademie

author: Kateřina Bartušková
email: kati.bartuskova@gmail.com
discord: bartuskovak
"""
import sys
from requests import get
from bs4 import BeautifulSoup
import unicodedata
import pandas as pd


def read_input_params(argv):
    """
    This function reads input arguments. First argument: url, second argument: output file name.
    :param argv: command line arguments
    :return: url, output file name
    """
    if len(argv) != 3:
        raise Exception("incorect input arguments, enter parameters <url> <output file name>")
    else:
        return argv[1], argv[2]


def process_table(root_url, table):
    """
    This function gets districts links and ids.
    :param root_url: url
    :param table: beautifulsoup object
    :return: list of district links and ids
    """
    links = []
    link_cols = table.find_all("td", "cislo")
    for link_col in link_cols:
        a = link_col.find("a")
        link = {"url": root_url + "/" + a["href"], "code": a.string}
        links.append(link)
    return links


def get_districts(page_url):
    """
    This function gets root url from input url and finds all tables on the page and processes them.
    :param page_url: program input url
    :return: list of districts
    """
    url_parts = page_url.rsplit("/", 1)
    root_url = url_parts[0]

    response = get(page_url)
    page = BeautifulSoup(response.text, features="html.parser")

    tables = page.find_all("table", "table")
    out_districts = []
    for tbl in tables:
        out_districts.extend(process_table(root_url, tbl))

    return out_districts


def create_output(districts):
    """
    This function gets all needed data from district tables and creates output csv file
    :param districts: list of district urls and ids
    """
    out_list = []
    for district in districts:
        district_response = get(district["url"])
        district_page = BeautifulSoup(district_response.text, features="html.parser")
        h3 = district_page.find_all("h3")
        location = ""
        if len(h3) >= 3:
            location = h3[2].text.strip().removeprefix("Obec: ")

        sum_table = district_page.findAll("table")[0]
        row = sum_table.findChildren("tr")[2]
        cols = row.findChildren()

        line = {
            "code": district["code"],
            "location": location,
            "registered": unicodedata.normalize("NFKD", cols[3].text),
            "envelopes": unicodedata.normalize("NFKD", cols[6].text),
            "valid": unicodedata.normalize("NFKD", cols[7].text),
        }

        parties_tables = district_page.findAll("table")[1:]
        for tbl in parties_tables:
            rows = tbl.findChildren("tr")[2:]
            for row in rows:
                cols = row.findChildren()
                line[cols[1].text] = unicodedata.normalize("NFKD", cols[2].text)

        out_list.append(line)
        print(line)

    df = pd.DataFrame(out_list)
    df.to_csv(out_file_name, index=False, header=True)


if __name__ == '__main__':

    #url = "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2109"
    #out_file_name = "output.csv"

    try:
        url, out_file_name = read_input_params(sys.argv)
    except Exception as err:
        print(err)

    districts = get_districts(url)

    create_output(districts)

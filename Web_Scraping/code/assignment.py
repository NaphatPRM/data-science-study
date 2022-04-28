from bs4 import BeautifulSoup
import requests
import sqlite3

### IEX TRADING API METHODS ###
IEX_TRADING_URL = "https://cloud.iexapis.com/stable/stock/"

### YAHOO FINANCE SCRAPING
MOST_ACTIVE_STOCKS_URL = "https://cs1951a-s21-brown.github.io/resources/stocks_scraping_2021.html"

### Register at IEX to receive your unique token
TOKEN = 'pk_cbffcd5c5e9340a293951c4dfde43fff'


# TODO: Use BeautifulSoup and requests to collect data required for the assignment.
def getData(url_to_scrap):
    if url_to_scrap is not None:
        r = requests.get(url_to_scrap)
        data = BeautifulSoup(r.content, 'html.parser')
    else:
        return

    headtable = data.find("table").find("tbody").find_all("tr")
    insert_sql_list = []
    for element in headtable:
        new_dict = {}
        result = element.find_all("td")
        new_dict["Name"] = result[1].text
        new_dict["Symbol"] = result[2].text.strip()
        new_dict["Price"] = float(result[3].text.replace(',', ''))
        new_dict["Chg."] = float(result[4].text)
        new_dict["Chg.%"] = float(result[5].text[:-1])
        new_dict["Vol"] = controlVol(result[6].text)
        new_dict["HQ(State)"] = result[7].text.lower().strip()
        insert_sql_list.append(new_dict)
    return insert_sql_list


def controlVol(inputString):
    if "M" in inputString:
        return float(inputString[:-1]) * 1000000
    elif "K" in inputString:
        return float(inputString[:-1]) * 1000
    else:
        return float(inputString)


# TODO: Use IEX trading API to collect sector and previous pricing data
list_dict = getData(MOST_ACTIVE_STOCKS_URL)
# Create a dictionary
current_dict = {}
previous_dict = {}
list_pass = []
for element in list_dict:
    web_request = requests.get(IEX_TRADING_URL + element["Symbol"] + "/chart/5d",
                               params={"token": TOKEN, "chartCloseOnly": True})
    previous_web_request = requests.get(IEX_TRADING_URL + element["Symbol"] + "/previous",
                                        params={"token": TOKEN, "chartCloseOnly": True})
    if (web_request.status_code != 200) or (previous_web_request.status_code != 200):
        continue

    # Parsing into the databases
    list_pass.append(element["Symbol"])
    value = 0
    # This loop represent all of the data within 5 days : using length instead of 5
    # because some of them could be missing
    average = web_request.json()
    for second_element in average:
        value = value + second_element["close"]
    average_value = value / len(average)
    current_dict[element["Symbol"]] = average_value

    previous_value = 0
    # Parsing the previous close
    previous_average = previous_web_request.json()
    previous_dict[element["Symbol"]] = previous_average["close"]

# Create connection to database
conn = sqlite3.connect('data.db')
c = conn.cursor()

# Delete tables if they exist
c.execute('DROP TABLE IF EXISTS "companies";')
c.execute('DROP TABLE IF EXISTS "quotes";')

# TODO: Create tables in the database and add data to it. REMEMBER TO COMMIT
# First, create both companies and quotes table
c.execute('CREATE TABLE companies(symbol text PRIMARY KEY NOT NULL, name text, location text)')
conn.commit()
command2 = '''
CREATE TABLE quotes
(symbol text PRIMARY KEY NOT NULL,
prev_close float,
price float,
avg_price float,
volume int,
change_pct float);
'''
c.execute(command2)
conn.commit()
for element in list_dict:
    if element["Symbol"] in list_pass:
        c.execute('INSERT INTO companies VALUES (?, ?, ?)', (element["Symbol"], element["Name"], element["HQ(State)"]))
        c.execute('INSERT INTO quotes VALUES (?, ?, ?, ?, ?, ?)',
                  (element["Symbol"], previous_dict[element["Symbol"]], element["Price"],
                   current_dict[element["Symbol"]], element["Vol"], element["Chg.%"]))
        conn.commit()
    else:
        continue

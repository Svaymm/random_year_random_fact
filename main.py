import http.client
import json
import art
from colorama import Fore, Style


Fore.BLUE = '\033[94m'
Fore.RED = '\033[91m'
Fore.GREEN = '\033[92m'
Style.RESET_ALL = '\033[0m'

conn = http.client.HTTPSConnection("numbersapi.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "f72f8f425emsh180e7644a2d9215p1335cfjsn31c1a5f6b43d",
    'X-RapidAPI-Host': "numbersapi.p.rapidapi.com"
    }

conn.request("GET", "/6/21/date?fragment=true&json=true", headers=headers)

res = conn.getresponse() 
data = res.read()

json_data = json.loads(data.decode("utf-8"))

year = json_data["year"]
fact = json_data["text"]

print(Fore.BLUE + f"Fact from year {year}: {fact}" + Style.RESET_ALL)

while True:
    year_input = input("Enter a year to get a fact about it (or 'exit' to quit): ")
    if year_input == "exit":
        break

    try:
        year_input = int(year_input)
        conn.request("GET", f"/{year_input}/year?json=true", headers=headers)

        res = conn.getresponse()
        data = res.read()

        json_data = json.loads(data.decode("utf-8"))

        if json_data["found"]: 
            fact = json_data["text"]
            print(Fore.BLUE + f"---\nFact from year {year_input}: {fact}" + Style.RESET_ALL)
            print(Fore.GREEN + art.text2art(str(year_input)) + Style.RESET_ALL)
        else:
            print(Fore.RED + f"---\nNo fact found for year {year_input}" + Style.RESET_ALL)
    except ValueError:
        print(Fore.RED + "Please enter a valid year." + Style.RESET_ALL)

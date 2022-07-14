import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

#Pull in team page, updating with your team's information
URL = "https://www.tennisrecord.com/adult/teamprofile.aspx?teamname=_______&year=2022&s=2"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

#Select the players table
results_list = [table for table in soup.find_all("table", class_="responsive14")]

#Create list of players names
td_list = [table.find_all("td", class_="padding10") for table in results_list]
a_list = [td.find_all("a") for td in td_list[2]]
content = [item.text.strip() for a in a_list for item in a]

#Convert names to all caps
#content = [name.upper() for name in content]

#Remove last blank entry from list
#content.pop()

print(content)
#Create list of names in format tennisrecord.com needs
search_params = [name.replace(" ", "%20") for name in content]
print(search_params)

#Delete unnecessary local variables
del results_list, td_list, a_list

for player in search_params:
    print(r'https://www.tennisrecord.com/adult/profile.aspx?playername='+ player)

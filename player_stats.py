import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

#Either a) hard-code the team roster in this section or b) knit this script with the previous team_tennisrecord or team_usta one
content = ['']
search_params = ['']


#Create blank dataframe that will house all the player data
df = pd.DataFrame(columns = ['Player','NTRP','Dynamic_Rating','Record','Current_Streak',
'Win_Streak_Max','Lose_Streak_Max','Set_Tiebraker','Third_Set_Tiebreaker','Postseason_Record',
'Average_Opponent_Rating','Total_Games_Per_Set_Self','Games_Per_Set_Self','Total_Games_Per_Set_Opponent',
'Games_Per_Set_Opponent','Double_Bagel_For','Double_Bagel_Against','Bagel_Breadstick_For','Bagel_Breadstick_Against',
'Double_Breadstick_For','Double_Breadstick_Against'])


for i in range(0, len(search_params)):
    #Import requisite page
    player = content[i]
    URL = r'https://www.tennisrecord.com/adult/playerstats.aspx?playername='+ search_params[i] + r'&mt=0&lt=0'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    #Pull all the tables from the page
    results_list = [table for table in soup.find_all("table", class_="responsive14")]

    #Initialize blank row with player name
    df = df.append({'Player': player}, ignore_index=True)

    #Get NTRP rating and estimated dynamic rating
    element_list = [e.find_all("span") for e in results_list]
    element_list = [item.text.strip() for e in element_list for item in e]
    df.loc[df['Player'] == player,'NTRP'] = element_list[1][0:3]
    df.loc[df['Player'] == player,'Dynamic_Rating'] = element_list[4]

    #Get brunt of stats
    element_list = [td.find_all("td", class_="padding10") for td in results_list]
    element_list = [item.text.strip() for e in element_list for item in e]
    df.loc[df['Player'] == player,'Record'] = element_list[3]
    df.loc[df['Player'] == player,'Current_Streak'] = element_list[5]
    df.loc[df['Player'] == player,'Win_Streak_Max'] = element_list[7]
    df.loc[df['Player'] == player,'Lose_Streak_Max'] = element_list[9]
    df.loc[df['Player'] == player,'Set_Tiebraker'] = element_list[11]
    df.loc[df['Player'] == player,'Third_Set_Tiebreaker'] = element_list[13]
    df.loc[df['Player'] == player,'Postseason_Record'] = element_list[15]
    df.loc[df['Player'] == player,'Average_Opponent_Rating'] = element_list[17]

    #Get games per set stats for self/opponent
    element_list = [td.find_all("td", style="text-align:right") for td in results_list]
    element_list = [item.text.strip() for e in element_list for item in e]
    df.loc[df['Player'] == player,'Games_Per_Set_Self'] = str([element_list[0],element_list[1],element_list[2]])
    df.loc[df['Player'] == player,'Total_Games_Per_Set_Self'] = element_list[3]
    df.loc[df['Player'] == player,'Games_Per_Set_Opponent'] = str([element_list[4],element_list[5],element_list[6]])
    df.loc[df['Player'] == player,'Total_Games_Per_Set_Opponent'] = element_list[7]

    #Get stats for Double_Bagel, Bagel_Breadstick, and Double_Breadstick
    element_list = [td.find_all("td", style="text-align:center") for td in results_list]
    element_list = [item.text.strip() for e in element_list for item in e]
    df.loc[df['Player'] == player,'Double_Bagel_For'] = element_list[0]
    df.loc[df['Player'] == player,'Double_Bagel_Against'] = element_list[1]
    df.loc[df['Player'] == player,'Bagel_Breadstick_For'] = element_list[2]
    df.loc[df['Player'] == player,'Bagel_Breadstick_Against'] = element_list[3]
    df.loc[df['Player'] == player,'Double_Breadstick_For'] = element_list[4]
    df.loc[df['Player'] == player,'Double_Breadstick_Against'] = element_list[5]

    print(content[i])


print(df)
df.to_csv(r'team_stats.csv',header=True, index = False)



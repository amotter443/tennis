# tennis
>Reverse engineering the USTA rating algorithm

Within both computer science and data science, a skillset that is crucial to master is web scraping. Scraping programs allow for data to be collected from websites and converted into a local data structure for subsequent analysis. Working on this project allowed me to get better at writing and process HTML requests in Python, and then using the scraped data to perform interesting analysis. Additionally, tennis with its complex scoring system and many variations provides a challenging and interesting dataset to perform cleaning and modeling. Working with tennis data allowed me to better understand the factors which affect player ratings and the many edge cases that can affect scoring and the ultimate match outcome. Even if you're not a tennis fan, this project has lots of unique challenges that are certain to prove engaging.


Who is this project for?
------------------------
- Python developers looking to gain experience in web scraping and using requests/BeautifulSoup libraries
- Data scientists looking to develop more skills with writing algorithms from scratch
- Tennis fans looking to upskill with an intermediate-advanced development project 


Data Sources
--------
![image](https://user-images.githubusercontent.com/71201000/179089031-6477ee0e-6a75-4a1d-8f66-1bd848205013.png)

- The United States Tennis Association (USTA) provides information about team members and aggregate team stats. You can find your team's information at: https://tennislink.usta.com/Leagues/Common/Default.aspx
- TennisRecord.com does a fantastic job at aggregating match statistics, dynamically calculating NTRP, and providing the backbone of data without which this project would be impossible. You can find your team's information at: https://www.tennisrecord.com/adult/teamsearch.aspx


Play Aggregate Stats Data Dictionary
------------------------
- `Player` -- Name of the player for whom the stats are stored
- `NTRP` -- National Tennis Rating Program (NTRP) rating on a scale of 1.5-7.0 in increments of 0.5
- `Dynamic_Rating` -- Approximate YTD non-rounded NTRP rating within 4 decimal points, i.e. 3.7203
- `Record` -- Win-to-loss ratio and percentage for player, i.e. 116-79 (59.5%)
- `Current_Streak` -- Measures recent streak of match results either win (W) or loss(L) and the quantity, i.e. W5
- `Win_Streak_Max` -- Maximum win streak for player over time
- `Lose_Streak_Max` -- Maximum loss streak for player over time
- `Set_Tiebraker` -- Overall win-to-loss ratio and percentage for player winning 6-6  tiebreakers within a set, i.e. 14-11 (56.0%)
- `Third_Set_Tiebraker` -- Win-to-loss ratio and percentage for player winning third-set tiebreakers, i.e. 25-21 (54.3%)
- `Postseason_Record -- Win/Loss record for league matches played beyond local play, i.e. 0-0
- `Average_Opponent_Rating` -- Average approximate YTD non-rounded NTRP rating within 4 decimal points of opponents, i.e. 3.7329
- `Total_Games_Per_Set_Self` -- Average games won across all three sets (considering that third sets are reduced to 1-0), i.e. 5.93
- `Games_Per_Set_Self` -- Average games won in each set, structured in a list in order from first to third set i.e. ['4.45', '4.56', '1.95']
- `Total_Games_Per_Set_Opponent` -- Average games won across all three sets (considering that third sets are reduced to 1-0) of opponents, i.e. 4.54
- `Games_Per_Set_Opponent` --  Average games won in each set by opponent, structured in a list in order from first to third set i.e. ['4.41', '4.19', '1.86']
- `Double_Bagel_For` -- When a player wins a match 6-0 6-0
- `Double_Bagel_Against` -- When a player loses a match 0-6 0-6
- `Bagel_Breadstick_For` -- When a player wins a match 6-0 6-1 or 6-1 6-0
- `Bagel_Breadstick_Against` -- When a player loses a match 6-0 6-1 or 6-1 6-0
- `Double_Breadstick_For` -- When a player wins a match 6-1 6-1
- `Double_Breadstick_Against` -- When a player loses a match 6-1 6-1

#!/usr/bin/env python
# coding: utf-8

# In[48]:


# use the nba_api to scrape the data 
# goal: collect data contains positions where each shot was made during a game 
from nba_api.stats.endpoints import shotchartdetail
import json 

# a list that stores team id for later use 
all_team_id = [1610612741, 1610612742, 1610612743, 1610612744, 1610612745, 1610612746, 1610612747, 1610612748, 1610612749, 1610612750, 1610612751, 1610612752, 1610612753, 1610612754, 1610612755, 1610612756, 1610612757, 1610612758, 1610612759, 1610612760, 1610612761, 1610612762, 1610612763, 1610612764, 1610612765, 1610612766 ]

# iterate the team list to get data of desired teams 
# manually change the season_nullable for desired season
for i in all_team_id:
    response = shotchartdetail.ShotChartDetail(
	team_id=i,
	player_id=0,
	season_nullable='2000-01',
    context_measure_simple = 'FGA',
	season_type_all_star='Regular Season'
)

    content = json.loads(response.get_json())

# convert contents into dataframe

    results = content["resultSets"][0]
    headers = results['headers']
    rows = results['rowSet']
    df = pd.DataFrame(rows)
    df.columns = headers

# write to csv file
# manually change file names for different seasons 
# without underscore refers to season 2020-2021 
# _1 refers to season 2000-01  
# _2 refers to season 2010-11 
#
    df.to_csv('shot_chart'+ str(i)+'_1.csv', index=False)
    




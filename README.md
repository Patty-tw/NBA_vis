# NBA_vis

# Rmd files 
- Shooting_data.Rmd: scraped shooting data from [NBA website](https://www.nba.com/stats/players/shooting)
- Traditional_stat.Rmd: scraped the traditional statatistics from [NBA website](https://www.nba.com/stats/players/traditional?sort=PTS&dir=-1)
- shot_dashboard.Rmd: scraped data from the shot dashboard for different positions, refers to [NBA](https://www.nba.com/stats/players/shots-general) for more information
- tidying.Rmd: tidy and transform the structure of scraped data 

# Python files and shot chart 
- NBA.py: scraped shot position data from [NBA](www.nba.com) using the [nba_api](https://github.com/swar/nba_api) from Swar Patel
- new_sc.rmd: combine all scraped data in the folder

# Data
- new_all_sc.zip: contains all shooting position data for all teams in 2000, 2010 and 2022 seasons 
- shoot_dash_center.csv: contains shooting dashboard statistic for all centers in the league of a specific season 
- shoot_dash_forward.csv: contains shooting dashboard statistic for all forwards in the league of a specific season 
- shoot_dash_guard.csv: contains shooting dashboard statistic for all guards in the league of a specific season 
- tr_long.csv: traditional statistic in long format 
- tr_stats_clean: tidy traditional statistic 
- tr_wide: traditional statistic in wide format 

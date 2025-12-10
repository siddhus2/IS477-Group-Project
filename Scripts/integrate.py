import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import os

CLEANED_PATH = r"C:\Users\siddh\OneDrive\Desktop\IS377 Project\results\cleaned"
OUTPUT_PATH = r"C:\Users\siddh\OneDrive\Desktop\IS377 Project\results"
os.makedirs(OUTPUT_PATH, exist_ok=True)

salaries_cleaned_df = pd.read_csv(os.path.join(CLEANED_PATH, "nba_player_stats_cleaned.csv"))
seasons_cleaned_df = pd.read_csv(os.path.join(CLEANED_PATH, "seasons_data_cleaned.csv"))

#Grouping by Team, Year, and Position to get the salary spent on each position
grouped = salaries_cleaned_df.groupby(['Team', 'Year', 'Pos'])['Salary'].sum().reset_index()

#Getting the total money spend by each team for every season
team_totals = salaries_cleaned_df.groupby(['Team', 'Year'])['Salary'].sum().reset_index()
team_totals = team_totals.rename(columns={'Salary': 'TeamTotal'})
team_totals.sample(n=10)

#Merging the team totals and grouped dfs to get the percent spend on each position each year
merged = grouped.merge(team_totals, on=['Team','Year'])
merged['Percent'] = merged['Salary'] / merged['TeamTotal'] * 100

team_map = {
    'Oklahoma City Thunder': 'OKC',
    'Cleveland Cavaliers': 'CLE',
    'Boston Celtics': 'BOS',
    'Minnesota Timberwolves': 'MIN',
    'Indiana Pacers': 'IND',
    'New York Knicks': 'NYK',
    'Denver Nuggets': 'DEN',
    'Los Angeles Clippers': 'LAC',
    'Houston Rockets': 'HOU',
    'Golden State Warriors': 'GSW',
    'Memphis Grizzlies': 'MEM',
    'Detroit Pistons': 'DET',
    'Sacramento Kings': 'SAC',
    'Los Angeles Lakers': 'LAL',
    'Milwaukee Bucks': 'MIL',
    'Dallas Mavericks': 'DAL',
    'Atlanta Hawks': 'ATL',
    'Chicago Bulls': 'CHI',
    'Orlando Magic': 'ORL',
    'San Antonio Spurs': 'SAS',
    'Phoenix Suns': 'PHO',
    'Portland Trail Blazers': 'POR',
    'Toronto Raptors': 'TOR',
    'Miami Heat': 'MIA',
    'Philadelphia 76ers': 'PHI',
    'Utah Jazz': 'UTA',
    'Washington Wizards': 'WAS'
}

#Creating Pivot Table to have df with the percent spend on each position for each team each year
pivoted = merged.pivot_table(
    index=['Team', 'Year'],
    columns='Pos',
    values='Percent',
    fill_value=0
).reset_index()
pivoted = pivoted.rename(columns=lambda x: f"Percent_{x}" if x not in ['Team','Year'] else x)
pivoted

#Making sure both dfs have the same type so they are ready to merge
seasons_cleaned_df['Year'] = seasons_cleaned_df['Year'].astype(int)
pivoted['Year'] = pivoted['Year'].astype(int)
seasons_cleaned_df['Team'] = seasons_cleaned_df['Team'].astype(str)
pivoted['Team'] = pivoted['Team'].astype(str)

#Creating column for team abbreviation
seasons_cleaned_df['TeamAbbr'] = seasons_cleaned_df['Team'].map(team_map)

#Merged pivot and seasons df to create a df with each teams performance and spending for every season
full_df = seasons_cleaned_df.merge(
    pivoted,
    left_on=['TeamAbbr','Year'],
    right_on=['Team','Year'],
    how='left'
)

full_df = full_df.drop(columns=['Team_y'])
full_df = full_df.rename(columns={'Team_x':'Team'})

integrated_output = os.path.join(OUTPUT_PATH, "integrated_data.csv")
full_df.to_csv(integrated_output, index=False)

print(f"✅ Integration complete. Integrated dataset saved to {integrated_output}")
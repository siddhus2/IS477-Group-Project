import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import os

DATA_PATH_SALARIES = "./data"
DATA_PATH_SEASONS = r"C:\Users\siddh\OneDrive\Desktop\IS377 Project\Data"
OUTPUT_PATH = r"C:\Users\siddh\OneDrive\Desktop\IS377 Project\results\cleaned"
os.makedirs(OUTPUT_PATH, exist_ok=True)

salaries_df = pd.read_csv(os.path.join(DATA_PATH_SALARIES, "NBA Player Stats and Salaries_2000-2025.csv"))
seasons_df = pd.read_csv(os.path.join(DATA_PATH_SEASONS, "Season_Data_Sheet1.csv"))

#Including only relevant columns in the datafram
contracts_relevant_columns = ["Player", "Salary", "Pos", "Year", "Team"]
salaries_df = salaries_df[contracts_relevant_columns]

#Changing some of the positions so that only the main 5 remain
salaries_df['Pos'] = salaries_df['Pos'].str.split('-').str[0]

# Only includes regular season stats and playoff W/L Totals
seasons_df = seasons_df.iloc[:, :21]

# Filter to only include 2005 and beyond
seasons_df = seasons_df[seasons_df['Year'] > 2004]

# Fills empty playoff W/L total columns with zero, as these were intentionally left blank since team missed playoffs
seasons_df[['PostW', 'PostL']] = seasons_df[['PostW', 'PostL']].fillna(0)

# Creates 0/1 Boolean for whether team made playoffs or not
seasons_df['Playoffs'] = (seasons_df[['PostW', 'PostL']].sum(axis=1) > 0).astype(int)

# Creates 0/1 Boolean for championship teams, teams that won championship had emoji in team name that was read as question marks
seasons_df['Championship'] = (
    seasons_df['Team'].str.contains(r'\?', regex=True)
).astype(int)

# Drops aforementioned question marks after championship files created
seasons_df['Team'] = seasons_df['Team'].str.replace('?', '', regex=False)

# Filter for teams that have 17 or more appearances in last 20 years (teams in NBA have shifted over the years)
seasons_df = seasons_df[seasons_df['Team'].isin(seasons_df['Team'].value_counts()[seasons_df['Team'].value_counts() >= 17].index)]

#Creating win_pct column
seasons_df['win_pct'] = seasons_df['W'] / (seasons_df['W'] + seasons_df['L'])

salaries_df.to_csv(os.path.join(OUTPUT_PATH, "nba_player_stats_cleaned.csv"), index=False)
seasons_df.to_csv(os.path.join(OUTPUT_PATH, "seasons_data_cleaned.csv"), index=False)

print("✅ Cleaning complete. Cleaned datasets saved.")





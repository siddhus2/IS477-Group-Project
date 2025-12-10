1. Project Overview

Brief description of the project:

Objective: Analyze NBA player stats and salaries from 2000–2025.

Data sources: Kaggle dataset (nba_player_stats) and manually compiled season data.

Workflow: Acquisition → Cleaning → Integration → Analysis/Visualization → Automation via Snakemake.

2. Data Acquisition

Description: Programmatically downloaded Kaggle dataset using Kaggle API. Season data CSV added to the project folder.

Scripts: Scripts/data_collection_and_acquisition.py

Inputs:

Kaggle dataset: https://www.kaggle.com/datasets/ratin21/nba-player-stats-and-salaries-2000-2025

CSV: data/Season_Data_Sheet1.csv

Outputs:

data/NBA Player Stats and Salaries_2000-2025.csv

data/Season_Data_Sheet1.csv

Checksums: data/checksums.txt

Steps to reproduce: 

1. Place Kaggle API token in environment variables.

2. Run data_collection_and_acquisition.py to download dataset and verify checksums.


3. Data Cleaning

Description:

Cleaned both datasets: removed nulls, standardized column names, fixed data types. narrowed range of data to fit our needs, filled empty values, created new columns

Scripts: Scripts/clean.py

Inputs:

data/NBA Player Stats and Salaries_2000-2025.csv

data/Season_Data_Sheet1.csv

Outputs:

results/cleaned/nba_player_stats_cleaned.csv

results/cleaned/seasons_data_cleaned.csv

Notes:

Cleaning steps include checking for null values, correcting inconsistent entries, filling in missing values, removing teams that were not relevant, adjusting to include last 25 years

Output files are ready for integration.

4. Data Integration

Description:

Merged player salary data with season-level data based on team and year to get a percentage of total salary spent on each positition for each team.

Scripts:

Scripts/integrate.py

Inputs:

results/cleaned/nba_player_stats_cleaned.csv

results/cleaned/seasons_data_cleaned.csv

Outputs:

results/integrated/integrated_data.csv

Integration schema: Found percentage of total salary spend on each position for every team for each year from the player salaries dataset 
and used and left join on team and year to merge with the seasons data


Ensured all teams in the seasons dataset and a corresponding percentage of salary spent on each position

5. Data Analysis and Visualization

Description:

Performed analysis and created visualizations to explore relationships such how salary spent on specific positions leads to more wins or success

Scripts: Scripts/analyze.py

Inputs: results/integrated/integrated_data.csv

Outputs / Figures:

results/analysis/top_vs_bottom.png

results/analysis/salary_pct_by_position.png

results/analysis/rTS_C_scatter.png

results/analysis/salary_by_position.png

results/analysis/salary_by_position_championship_teams.png

6. Workflow Automation (Snakemake)

Description:

Automates the full workflow from acquisition to analysis.

Ensures reproducibility of results.

Snakefile: Located at project root: Snakefile

Commands to run: python -m snakemake --cores 1

Notes:

Snakemake handles dependencies between rules: acquire → clean → integrate → analyze.

7. Filesystem Structure

IS377 Project/
│
├─ data/                  
│   ├─ NBA Player Stats and Salaries_2000-2025.csv
│   └─ Season_Data_Sheet1.csv
│
├─ results/
│   ├─ cleaned/
│   ├─ integrated/
│   └─ analysis/
│
├─ Scripts/
│   ├─ data_collection_and_acquisition.py
│   ├─ clean.py
│   ├─ integrate.py
│   └─ analyze.py
│
├─ Snakefile

8. Software Dependencies

Python 3.12

Packages: pandas, numpy, matplotlib, seaborn, kaggle, snakemake

requirements.txt included for reproducibility.

9. How to Reproduce

1 Clone the repository.
2 Set Kaggle API credentials as environment variables.
3 Install dependencies:
4 Run Snakemake
5 Check outputs in results/ folder.




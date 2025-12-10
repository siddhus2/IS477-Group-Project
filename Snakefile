rule acquire:
    output:
        "data/NBA Player Stats and Salaries_2000-2025.csv"
    script:
        "Scripts/data_collection_and_acquisition.py"


# Step 2: Clean data
rule clean:
    input:
        salaries="data/NBA Player Stats and Salaries_2000-2025.csv",
        seasons="data/Season_Data_Sheet1.csv"
    output:
        cleaned_salaries="results/cleaned/nba_player_stats_cleaned.csv",
        cleaned_seasons="results/cleaned/seasons_data_cleaned.csv"
    script:
        "Scripts/clean.py"

# Step 3: Integrate datasets
rule integrate:
    input:
        cleaned_salaries="results/cleaned/nba_player_stats_cleaned.csv",
        cleaned_seasons="results/cleaned/seasons_data_cleaned.csv"
    output:
        integrated="results/integrated_data.csv"
    script:
        "Scripts/integrate.py"

# Step 4: Generate visualizations
rule analyze:
    input:
        integrated="results/integrated_data.csv"
    output:
        "results/analysis/top_vs_bottom.png",
        "results/analysis/salary_pct_by_position.png",
        "results/analysis/rTS_C_scatter.png",
        "results/analysis/salary_by_position.png",
        "results/analysis/salary_by_position_championship_teams.png"
    script:
        "Scripts/analyze.py"
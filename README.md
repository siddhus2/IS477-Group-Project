Contributors:
Colin Papp (Summary, data profile, findings, future work, creating visualizations and sourcing data)
Siddhu Sami (Data quality, reproducibility, handling workflow automation, integrating data and splitting up code into scripts)

Summary [500-1000 words] Description of your project, motivation, research question(s), and any findings.
	
This project integrates two independently sourced NBA datasets to analyze how team spending allocation by position relates to on-court performance. The first dataset is a comprehensive player salary file originally scraped by data scientist Erik Gregory Webb, later cleaned and published under the permissive MIT license by Edwin Jeon on Kaggle. It includes thousands of player-season entries from 2001 onward, covering salary, team, position, and basic box-score statistics. Its licensing allows unrestricted educational use as long as attribution is preserved. The second dataset comes from CraftedNBA, a platform that aggregates publicly available NBA game data and applies its own transformations to generate advanced metrics. The extracted team-season data used here includes wins, losses, playoff outcomes, championships, and efficiency metrics spanning back to 1955. The data is publicly accessible and intended for analytical use, with the main ethical constraint being responsible interpretation of transformed, non-raw league data.
Both datasets required extensive cleaning before integration. The salary data needed standardization of currency formatting, consolidation of dual-position players, alignment of team names, and filtering to the years overlapping with reliable team data. The team dataset required corrections to playoff and championship markers, conversion of emojis and inconsistent symbols, and elimination of pre-2005 seasons where data quality was weaker. After cleaning, the combined dataset contained no null values and featured fully standardized team-year records.
The quality assessment found the datasets to be largely complete, with player coverage nearly exhaustive and team-season data fully populated for the selected window. Accuracy was supported by credible provenance: the salary data originates from a vetted data science project, while team performance metrics reflect factual NBA game results. The largest limitations were structural rather than numerical as salary figures do not reflect bonuses or unusual contract clauses, and dual-position assignments required judgement calls. Manual copy-pasting of CraftedNBA data introduced a small theoretical risk of transcription error, though no issues remained after verification.
The merged dataset enabled clear, interpretable findings. Leaguewide spending trends show a long-term decline in center salaries alongside a rise in point guard spending, consistent with the NBA’s transition toward perimeter-oriented play and the premium placed on shooting and creation. When comparing spending allocation between top-quartile and bottom-quartile teams by win percentage, successful teams spent materially more on small forwards and point guards and significantly less on shooting guards. Power forward and center spending remained broadly consistent, suggesting that interior defense and rebounding still require baseline investment even as the league evolves. Championship team spending profiles deviated from these patterns due to dynasty-driven skew: franchises like the Lakers and Warriors dominated the period, meaning stars such as Kobe Bryant and Steph Curry disproportionately influenced positional spending averages. Correlation analysis showed that similar positions cannibalize each other’s spending (SF vs. SG, PF vs. C), while less-related roles tend to rise together.
The project also highlighted key lessons about data feasibility. The original plan, NFL positional spending, was abandoned because public salary data was too inconsistent and paywalled to support rigorous modeling. This forced an early focus on data provenance, licensing, cleaning standards, and reproducibility. The amount of judgement involved in seemingly small decisions, such as handling combo-position players, reinforced that data science is not mechanical and that assumptions must be explicit. Integrating two unrelated datasets surfaced unanticipated inconsistencies in naming, structure, and missing fields, emphasizing that cleaning often consumes more time than analysis but ultimately strengthens the defensibility of the final results.


Data profile: [500-1000 words] Description of each dataset used including all ethical/legal constraints.

Dataset 1: Salary Data
Data Use
This is the dataset that will be paired with the team result dataset and contains player salary info on thousands of players spanning back to 2001

Provenance
The salary dataset we used for our analysis was initially discovered on Kaggle and traced back to its initial lineage from data collection to Kaggle post
Data scientist Erik Gregory Webb, who at the time worked for JPMorgan, scraped NBA player salary data
Permission to use here: erikgregorywebb/data: Datasets I've created or collected, usually via web scraping. (This is public information that can be used for educational purposes)
Edwin Jeon, another data scientist and basketball fan, cleans it and provides the script used to clean it, this is the dataset that was ultimately posted to Kaggle
Dataset: NBA-Salary-Prediction/data/NBA Player Stats and Salaries_2000-2025.csv at main · edwinjeon/NBA-Salary-Prediction
Script: NBA-Salary-Prediction/NBA Salary Project Data Preparation.ipynb at main · edwinjeon/NBA-Salary-Prediction

Ethical and legal constraints
Edwin Jeon cleaned Erik Webb’s dataset and did not add any new restrictive licenses, and the MIT license is very permissive, allowing modifications, copying and free use as long as attribution is maintained
This salary data is public but interpretation isn’t, this analysis will avoid misleading narratives about players and clearly note limitations 

Description
This dataset has the following columns 'Player', 'Salary', 'Year', 'Pos', 'Age', 'Team', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', '2P', '2PA', '2P%', 'eFG%', 'FT','FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS'
Player, Salary, Pos, Year, and Team will be the columns of interest
Player: 2133 unique values of player names, first and last name, object
Salary: $5.8 Million mean, $7.6M standard deviation, $56M maximum, integer
Pos: abbreviated position of player, filtered down to 5 unique values
Year: year of season, spanning from 2001 to present
Team: 3 letter abbreviation of team that player is on (this will be used as a primary key to combine with team results dataset)

Dataset 2: Team Results Data

Data Use:
This is the dataset we will compare positional spending allocations against, and contains several statistics on team performance and advanced stats, dating back to 1955

Provenance:
This dataset was derived from data that is publicly available on craftedNBA.com, a website for curated data for professional basketball fans
CraftedNBA.com aggregates publicly available NBA game data and applies its own calculations and models to generate advanced metrics with comprehensive data, the platform doesn’t generate any raw data, it transforms publicly accessible league data into analytics friendly format
Historical NBA Team Stats | CraftedNBA | NBA Stats & Analytics


Legal and Ethical Constraints:
The data is publicly accessible and intended for analytical use by visitors, and the data is used here for strictly non-commercial, educational purposes
The main ethical limitation is avoiding misleading interpretations and incorrectly frame 

Description:
After performing additional cleaning and selecting for recent years (2006 and later), key variables included Team, Year, W, L, Playoffs, Championship
Team: full team name to be abbreviated to three letters to match the other
W: season win total out of 82 games, mean of 41, max of 73, minimum of 10, standard deviation of 12.56
L: season loss total: mean of 40, maximum of 72, minimum of 9, standard deviation of 12.45
Playoffs: boolean variable for making playoffs, average of 0.56
Championship: boolean variable for winning championship

Data quality: [500-1000 words] Summary of the quality assessment and findings.

Data Quality
For this project, we analyzed NBA player salary data alongside NBA season performance data to investigate how team spending allocation by position correlates with team success metrics. Ensuring the quality of both datasets was crucial to producing reliable, accurate, and meaningful analysis. The datasets underwent a thorough assessment to evaluate completeness, consistency, accuracy, and usability, while also identifying potential limitations and cleaning steps.
The salary dataset was sourced from Edwin Jeon, who cleaned data originally collected by Erik Gregory Webb. Both individuals are professional data scientists sharing datasets for educational purposes, allowing free use. The dataset includes Player, Year, Salary, Position, and Team, which are sufficient to calculate team spending allocation by position. The season dataset was obtained from craftedNBA.com, a curated source of NBA statistics spanning back to 1955. While the website offers dozens of metrics per season, only data from 2005 onward was used, both for consistency with salary data and to ensure reliability. The season data includes wins, losses, playoff results, team strength, SRS, offensive and defensive ratings, pace, true shooting, and playoff wins and losses, among other metrics.
Completeness
The completeness of the datasets was generally high. Salary data contained almost all relevant entries for NBA players, though a small portion of players were listed with dual positions (e.g., SF-SG). To maintain consistency in spending allocation, these players were assigned to the first listed position. Historical data prior to 2005 was less reliable, which justified filtering both datasets to include only seasons from 2005 onward. Teams with limited representation across seasons were excluded, with only teams having at least 17 seasons retained for analysis.
The season dataset was complete for all selected seasons. Missing playoff wins and losses for teams that did not make the playoffs were replaced with zeros, reflecting the factual absence of playoff participation. No remaining null values were present in the processed datasets, and all relevant performance metrics were retained for analysis.
Consistency
Consistency issues were addressed through preprocessing. Player names were relatively standardized, but team names differed between datasets: the salary dataset used abbreviations (e.g., CLE), while the season dataset used full team names (e.g., Cleveland Cavaliers). A name mapping was created to align team names across datasets, allowing accurate merging. Salary values were also standardized, removing currency symbols and commas to ensure numerical formatting. Dual positions in the salary dataset were simplified to a single primary position to maintain consistency in spending allocation calculations.
Season data presented additional consistency challenges. Playoff wins and championship markers were initially stored as emojis or question marks in the raw data. These were converted into numeric and boolean variables, respectively, and any anomalies were corrected during preprocessing. This standardization ensured that derived metrics such as playoff appearance and championship wins were consistent across all teams and seasons.
Accuracy
Accuracy was supported by the reliability of the original sources. Salary data comes from verified educational datasets maintained by data science professionals, while season data reflects factual, non-copyrightable NBA statistics compiled from official game results. Minor discrepancies in salaries, such as adjustments due to mid-season trades or bonuses, were rare and unlikely to affect aggregate analyses.
To verify accuracy, all data entries were inspected for obvious errors or inconsistencies. Derived columns, such as playoff appearance (boolean) and championship win (boolean), were created using clear, consistent criteria. Manual verification was applied when converting season data from Excel to CSV to minimize transcription errors. After processing, all datasets were free of missing or anomalous values, providing a reliable foundation for analysis.
Usability and Preprocessing
Both datasets required significant preprocessing to enhance usability. Salary data was filtered to retain only relevant columns, then grouped by position and team. Salaries were normalized to produce team-level spending allocation distributions, which allowed direct comparison of spending strategies across teams and seasons. This processed data was then linked to the season dataset, enabling analysis of how spending allocation impacts team performance.
Season data was similarly filtered to retain only relevant metrics, with missing playoff statistics filled and derived variables created. Exploratory data analysis (EDA) was conducted using Matplotlib to visualize trends. For salary data, stacked bar charts revealed league-wide spending patterns by position, showing a growing share of spending allocated to guards and a decreasing share for centers and power forwards. Season data visualizations highlighted distributions of championships, playoff appearances, and win percentages, validating the datasets and confirming logical trends over time.
Limitations
Despite the overall high quality of the datasets, several limitations were identified. Salary data may not fully reflect bonuses or deferred payments, which could slightly distort spending allocation calculations. Season performance metrics do not account for qualitative factors such as injuries, trades, or coaching strategies, which may influence results. Assigning dual-position players to a single position introduces minor simplifications, but this approach ensures consistent comparison across teams. Manual copy-pasting of season data, while carefully verified, poses a small risk of transcription errors, though none were detected after cleaning.



Findings: [~500 words] Description of any findings including numeric results and/or visualizations.

	After finishing up acquiring and loading the data in, cleaning each respective data set and then integrating the two and calculating team allocation, we wanted to seek out trends in the data and compare it to our intuition about how basketball has evolved. A clear example of one of these trends can be seen by plotting the normalized leaguewide spending distribution by position. We used Matplotlib to graph this and visually capture this trend. Through this analysis, we can find that over the past few decades, leaguewide spending on centers has slowly regressed as spending on point guards started to marginally increase. This aligns with the perception that the traditional ‘bigs’ that use to dominate the game such as Shaquille O’Neal on the Lakers, have given way, at least in terms of salary, to sharpshooting guards like Steph Curry on the Warriors. The increase of the importance of 3-point shooting has tangibly impacted salary spending priorities. But how does is this shift in spending justified by improved performance?
Looking across team overall win/loss performance in our selected years (past two decades) we found the difference in spending between the upper quartile teams and bottom quartile teams. Upper quartile teams, on average, spent 6.55% more on small forwards, 3.01% on point guards, 0.62% on power forwards, essentially the same amount on centers, and shockingly 10% less on shooting guards. This suggests that successful teams are taking money out of the shooting guard position and putting it into more versatile power forward, point guard and small forward positions. Meanwhile, adequate spending on the center position is still necessary for interior defense and effective rebounding. 
We also looked at how championship teams spend. Contrasting with previous results, championship teams in our dataset are anchored by predominantly power forward, shooting guard and power forward expenditures. This contrasts with the negative sentiment against shooting guards from looking at bottom vs. top quartile spending for overall win/loss percentage. This contrasting data is likely because there are only a few dozen championship teams in the time period we selected, and several teams won multiple championships, so a spending mix for one dynasty franchise can skew these results. For example, the Los Angeles Lakers and Golden State Warriors won an outsized amount of championships in our selected data, which may skew results. Namely, Kobe Bryant players as a star shooting guard for the Lakers during their title runs, explaining this variance. 
	Furthermore, we wanted to analyze how different variables correlate with each other. When developing a correlation table between spending allocations of different positions, it appears that closely intertwined positions ‘cannibalize’ each other’s spending, where if one of two closely related positions sees an increase in spending, it is correlated with an outsized negative correlation in spending with other positions. These pairs with an outsized impact on each other include power forward / center, and small forward / shooting guard. Positions whose spending ‘cooperate’ with each other include shooting guard / center and point guard / small forward.

Future work: [~500-1000 words] Brief discussion of any lessons learned and potential future work.

Lessons Learned
Throughout the course of this project, a big lesson learned is that the quality and structure of available data molds the entire direction of an analysis. Our original NFL plan required a pivot because public salary data was inconsistent, incomplete and predominantly behind paywalls. Although analyzing NFL positional spending allocation would have been a very interesting project, we needed to respond to the hard truth that methodological rigor is impossible without reliable inputs. That pivot forced us to think early about data provenance, structure, cleaning and licensing and how this all plays into analytical feasibility. Going forward, that mindset will carry through our modeling decisions and how we evaluate our results.
Another key lesson has been the amount of manual judgement involved in simple cleaning decisions. Even something as small as assigning a player with a double position “SG-SF”. Initially we considered just cutting out these double position players as anomalies, but quickly realized it included legendary players such as Allen Iverson. These small decisions can compound decades of data and influence downstream results. This shows the importance of judgement, and that data science isn’t a mechanical process. 
We also learned that merging two independently-sourced datasets exposes inconsistencies you may not be able to anticipate such as empty playoff stats, name formatting, team changes, and unique artifacts like unicode championship emojis. Cleaning and integrating the two datasets took significantly more time than originally planned, but it ultimately gave us a much deeper understanding of what the data actually represents. This sets up our pipeline to be more defensible and less error prone. 

Potential Future Work
	An additional phase of the project could be separating the analysis into different eras. For example, this could be pre-2015 vs. post-2015 to see how the league-wide shift towards perimeter play changed the types of patterns that correlate with success. This would be a simple way of rerunning the same simple regressions on filtered subsets to glean new insights. 
We could also do cluster analysis, grouping teams by spending profiles to identify archetypes of teams (guard heavy, balanced, frontcourt, star-heavy) and comparing success rates. This could help display ownership styles within the league and produce insights that ground long-held beliefs and unproven opinions in empirical statistical reality. Once these clusters are formed, we could compare average win totals, playoff success rates or efficiency metrics to see whether certain spending archetypes tend to outperform others. Even a basic k-means clustering on positional spending percentages could give an interesting picture into how management and roster building philosophies manifest in data, and how they stack up to each other. 
Furthermore, if we had access, we could incorporate additional data that could improve model accuracy such as player availability (games missed), cap smoothing events and league salary rule changes. These factors influence salaries and team strategy and would help separate true spending impact from noise that is driven by context. Overall, we’ve learned that good data science relies on clean data, explicit assumptions and a willingness to pivot when the original plan may not be viable. 	



Reproducing: Sequence of steps required for someone else to reproduce your results.

1. Clone the Repository
The first step is to clone the project repository to a local environment. This ensures that all scripts, data placeholders, and workflow definitions (Snakefile) are available.
2. Set Up Environment
Ensure that Python 3.12 is installed. It is recommended to create a virtual environment to isolate project dependencies. The project requires the following Python packages: pandas, numpy, matplotlib, seaborn, kaggle, and snakemake. Installing via requirements.txt ensures version consistency. Additionally, the Kaggle API token must be set as an environment variable to allow programmatic download of the NBA player stats and salaries dataset:
3. Data Acquisition
Data acquisition is automated through the script Scripts/data_collection_and_acquisition.py. Running this script performs the following: downloads the NBA player stats and salaries dataset from Kaggle, verifies file integrity using provided checksums (data/checksums.txt), and places the downloaded file in the data/ directory. For manual data, the season dataset CSV (Season_Data_Sheet1.csv) should already be located in data/. After running the script, the project directory contains both input datasets ready for cleaning.
4. Data Cleaning
Cleaning ensures that datasets are analysis-ready. The cleaning script, Scripts/clean.py, performs the following. Removal of null values and irrelevant columns. Standardization of column names and data types. Filling in missing values where appropriate. Filtering the datasets to focus on the years 2000–2025. And creating derived columns necessary for further analysis. After running, the cleaned datasets are saved in results/cleaned/ as: nba_player_stats_cleaned.csv and seasons_data_cleaned.csv. 
5. Data Integration
Integration merges player salary data with season-level team data to calculate team spending allocation by position. The script Scripts/integrate.py does the following: Groups salaries by position and team, calculating the percentage of total salary spent per position. Performs a left join with the season dataset based on team and year. Ensures alignment of team names and completeness across datasets. The resulting integrated dataset is saved to results/integrated/integrated_data.csv and serves as the foundation for analysis.
6. Data Analysis and Visualization
The analysis script, Scripts/analyze.py, generates exploratory visualizations and investigates relationships between team spending and performance metrics. This includes: Stacked bar charts of league-wide spending by position. Normalized salary distributions over time.
Scatterplots linking salary allocation to team performance metrics. Visualizations comparing championship-winning teams to others. And output figures are saved to results/analysis/.
7. Workflow Automation with Snakemake
To ensure reproducibility and manage dependencies between each step, the entire workflow is automated using Snakemake. Running Snakemake will execute all steps in order, only re-running steps if inputs change. 
8. Verify Outputs
After completing the workflow, the results/ folder should contain the cleaned datasets (results/cleaned/), integrated dataset (results/integrated/), and analysis figures (results/analysis/). Checksums and manual inspection can confirm that files match expected outputs, ensuring reproducibility.







References: Formatted citations for any papers, datasets, or software used in your project.

MIT License: MIT License

Copyright Erik

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.




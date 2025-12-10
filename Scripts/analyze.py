import pandas as pd
import matplotlib.pyplot as plt
import os

INPUT_FILE = r"C:\Users\siddh\OneDrive\Desktop\IS377 Project\results\integrated_data.csv"
OUTPUT_DIR = r"C:\Users\siddh\OneDrive\Desktop\IS377 Project\results\analysis"
os.makedirs(OUTPUT_DIR, exist_ok=True)

full_df = pd.read_csv(INPUT_FILE)


#Graph 1
position_cols = [col for col in full_df.columns if col.startswith('Percent')]
avg_p = full_df[position_cols].mean().sort_values()
plt.figure(figsize=(10,5))
plt.bar(avg_p.index, avg_p.values)
plt.title("Average Salary Percentage by Position")
plt.ylabel("Percentage of Team Salary")
plt.savefig(os.path.join(OUTPUT_DIR, "salary_by_position.png"))
plt.close()


#Graph 2
champions = full_df[full_df['Championship'] == 1]
position_cols = [col for col in champions.columns if col.startswith('Percent')]
avg_pos = champions[position_cols].mean().sort_values()
plt.figure(figsize=(10,5))
plt.bar(avg_pos.index, avg_pos.values)
plt.title("Average Salary Percentage by Position (Championship Teams)")
plt.ylabel("Percentage of Team Salary")
plt.savefig(os.path.join(OUTPUT_DIR, "salary_by_position_championship_teams.png"))
plt.close()


#Graph 3
avg_by_year = full_df.groupby("Year")[position_cols].mean().reset_index()
plt.figure(figsize=(12,6))
for col in position_cols:
    plt.plot(avg_by_year["Year"], avg_by_year[col], marker='o', label=col)
plt.title("Average Salary Percentage by Position Across Years")
plt.xlabel("Year")
plt.ylabel("Average % of Team Salary")
plt.legend(title="Position")
plt.grid(True)
plt.savefig(os.path.join(OUTPUT_DIR, "salary_pct_by_position.png"))
plt.close()


#Graph 4
def plot_correlated_scatter(col_x, col_y, save_path=None):
    plt.figure(figsize=(8, 6))
    
    correlation = full_df[col_x].corr(full_df[col_y])
    
    plt.scatter(full_df[col_x], full_df[col_y], color='darkblue', alpha=0.6)

    plt.title(f'Scatter Plot of {col_y} vs. {col_x}')
    plt.xlabel(col_x)
    plt.ylabel(col_y)

    plt.annotate(
        f'Correlation (r): {correlation:.3f}', 
        xy=(0.05, 0.95), 
        xycoords='axes fraction',
        fontsize=12, 
        bbox=dict(boxstyle="round,pad=0.5", fc="white", alpha=0.7)
    )

    plt.grid(True, linestyle='--', alpha=0.4)
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=300)


    plt.close()

plot_correlated_scatter("rTS", "Percent_C", os.path.join(OUTPUT_DIR, "rTS_C_scatter.png"))


#Graph 5

recent = full_df[full_df.Year > 2020]

recent['Quartile'] = pd.qcut(recent['win_pct'], 4, labels=['Q4', 'Q3', 'Q2', 'Q1'])

percent_cols = [col for col in full_df.columns if col.startswith('Percent_')]

df_avg = recent.groupby('Quartile')[percent_cols].mean().reset_index()

q1_spending = df_avg[df_avg['Quartile'] == 'Q1'].drop(columns=['Quartile']).iloc[0]
q4_spending = df_avg[df_avg['Quartile'] == 'Q4'].drop(columns=['Quartile']).iloc[0]

df_diff = (q1_spending - q4_spending).to_frame(name='Difference').reset_index()
df_diff.columns = ['Position', 'Difference']

df_diff['Position'] = df_diff['Position'].str.replace('Percent_', '')

df_diff = df_diff.sort_values('Difference', ascending=False)

df_diff['Color'] = df_diff['Difference'].apply(lambda x: 'darkgreen' if x > 0 else 'darkred')

plt.figure(figsize=(10, 7))

plt.barh(
    y=df_diff['Position'], 
    width=df_diff['Difference'], 
    color=df_diff['Color'], 
    alpha=0.8
)

plt.title('Difference in % Salary Spent: Top Teams (Q1) vs. Bottom Teams (Q4)', fontsize=14)
plt.xlabel('Difference in Average % Salary Spent (Q1 - Q4)')
plt.ylabel('Position')
plt.axvline(0, color='grey', linewidth=0.8, linestyle='--')
plt.grid(axis='x', linestyle=':', alpha=0.5)

for i, diff in enumerate(df_diff['Difference']):
    ha = 'left' if diff > 0 else 'right'
    x_offset = 0.001 if diff > 0 else -0.001 
    
    plt.text(
        diff + x_offset, 
        i, 
        f'{diff:.2f}%', 
        ha=ha, 
        va='center', 
        fontsize=10
    )
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "top_vs_bottom.png"))
plt.close()

print("Analysis complete. Plots saved to:", OUTPUT_DIR)
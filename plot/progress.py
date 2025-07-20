import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Load the data
file_path = r'd:\Documents\Github\Forks\Dagda-scripts\data\plot\progress.tsv'
data = pd.read_csv(file_path, sep='\t')

# Parse dates and times
def parse_date(date_str):
    if date_str.startswith('@'):
        date_str = date_str[1:].strip()

    return datetime.strptime(date_str, "%B %d, %Y")

data['Date'] = data['Date'].apply(parse_date)
data['Time'] = pd.to_timedelta(data['Time'])
data['Progress'] = data['Progress'].str.replace(',', '.').astype(float)

# Combine date and time
data['DateTime'] = data['Date'] + data['Time']

# Sort by datetime
data = data.sort_values(by='DateTime')

# Generate a complete date range
full_date_range = pd.date_range(start=data['DateTime'].min().floor('D'), end=data['DateTime'].max().floor('D'), freq='D')
data = data.set_index(data['DateTime'].dt.floor('D')).reindex(full_date_range).reset_index()
data.rename(columns={'index': 'FullDate'}, inplace=True)

# Fill missing progress values with NaN
data['Progress'] = data['Progress'].fillna(method='ffill')  # Forward fill for continuity

# Plot the data as a stairs plot with filled area
plt.figure(figsize=(10, 6))
plt.step(data['FullDate'].dt.strftime('%d/%m'), data['Progress'], where='post', label='Progress', color='blue')
plt.fill_between(data['FullDate'].dt.strftime('%d/%m'), data['Progress'], step='post', alpha=0.3, color='blue')

# Add labels only for existing data points
filtered_data = data.dropna(subset=['Time'])  # Keep only original data points
for i, row in filtered_data.iterrows():
    plt.text(row['FullDate'].strftime('%d/%m'), row['Progress'], f"{row['Progress']} ({row['Time']})", fontsize=8, ha='right')

# Configure plot
plt.xlabel('Date (DD/MM)')
plt.ylabel('Progress')
plt.title('Progress Over Time')
plt.ylim(0, 1)
plt.grid(True)
plt.tight_layout()

# Save and show the plot
# output_path = r'D:\Documents\Github\Forks\Dagda-scripts\plot\progress_plot.png'
# plt.savefig(output_path)
plt.show()

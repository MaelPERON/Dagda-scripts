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
    if date_str.lower() == "today":
        return datetime.now()
    elif date_str.lower() == "yesterday":
        return datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) - pd.Timedelta(days=1)
    elif date_str.lower() == "last sunday":
        today = datetime.now()
        return today - pd.Timedelta(days=today.weekday() + 1)
    else:
        return datetime.strptime(date_str, "%B %d, %Y")

data['Date'] = data['Date'].apply(parse_date)
data['Time'] = pd.to_timedelta(data['Time'])
data['Progress'] = data['Progress'].str.replace(',', '.').astype(float)

# Combine date and time
data['DateTime'] = data['Date'] + data['Time']

# Sort by datetime
data = data.sort_values(by='DateTime')

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(data['DateTime'].dt.strftime('%d/%m'), data['Progress'], marker='o', label='Progress')

# Add labels to each point
for i, row in data.iterrows():
    plt.text(row['DateTime'].strftime('%d/%m'), row['Progress'], f"{row['Progress']} ({row['Time']})", fontsize=8, ha='right')

# Configure plot
plt.xlabel('Date (DD/MM)')
plt.ylabel('Progress')
plt.title('Progress Over Time')
plt.ylim(0, 1)
plt.grid(True)
plt.tight_layout()

# Save and show the plot
output_path = r'D:\Documents\Github\Forks\Dagda-scripts\plot\progress_plot.png'
plt.savefig(output_path)
plt.show()

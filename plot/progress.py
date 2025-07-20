import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def parse_date(date_str):
    if date_str.startswith('@'):
        date_str = date_str[1:].strip()

    return datetime.strptime(date_str, "%B %d, %Y")

def plot_progress(filepath, display_name: str = "", axis_time: str = "Time", axis_date: str = "Date", axis_progress: str = "Progress"):
    """Plots the progress data from a TSV file.

    Args:
        filepath (str): Path to the TSV file containing the progress data.
        display_name (str, optional): Plot name to display as title. Defaults to "".
        axis_time (str, optional): The time axis. Defaults to "Time".
        axis_date (str, optional): The date axis. Defaults to "Date".
        axis_progress (str, optional): The progress axis. Defaults to "Progress".

    Raises:
        ValueError: _description_
    """
    # Load the data
    data = pd.read_csv(filepath, sep='\t')

    # Ensure the required columns are present
    if axis_date not in data.columns or axis_time not in data.columns or axis_progress not in data.columns:
        raise ValueError(f"Required columns '{axis_date}', '{axis_time}', or '{axis_progress}' are missing from the data.")

    display_name = display_name or "Progress Over Time"

    data[axis_date] = data[axis_date].apply(parse_date)
    data[axis_time] = pd.to_timedelta(data[axis_time])
    data[axis_progress] = data[axis_progress].str.replace(',', '.').astype(float)

    # Combine date and time
    data['DateTime'] = data[axis_date] + data[axis_time]

    # Sort by datetime
    data = data.sort_values(by='DateTime')

    # Generate a complete date range
    full_date_range = pd.date_range(start=data['DateTime'].min().floor('D'), end=data['DateTime'].max().floor('D'), freq='D')
    data = data.set_index(data['DateTime'].dt.floor('D')).reindex(full_date_range).reset_index()
    data.rename(columns={'index': 'FullDate'}, inplace=True)

    # Fill missing progress values with NaN
    data[axis_progress] = data[axis_progress].fillna(method='ffill')  # Forward fill for continuity

    # Plot the data as a stairs plot with filled area
    plt.figure(figsize=(10, 6))
    plt.step(data['FullDate'].dt.strftime('%d/%m'), data[axis_progress], where='post', label='Progress', color='blue')
    plt.fill_between(data['FullDate'].dt.strftime('%d/%m'), data[axis_progress], step='post', alpha=0.3, color='blue')

    # Add labels only for existing data points
    filtered_data = data.dropna(subset=[axis_time])  # Keep only original data points
    for i, row in filtered_data.iterrows():
        plt.text(row['FullDate'].strftime('%d/%m'), row[axis_progress], f"{row[axis_progress]} ({row[axis_time]})", fontsize=8, ha='right')

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

if __name__ == "__main__":
    filepath = r'd:\Documents\Github\Forks\Dagda-scripts\data\plot\progress.tsv'
    plot_progress(filepath, display_name="UE Environment Progress")
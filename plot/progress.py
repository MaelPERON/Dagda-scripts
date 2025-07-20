import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import argparse

def parse_date(date_str):
    if date_str.startswith('@'):
        date_str = date_str[1:].strip()

    return datetime.strptime(date_str, "%B %d, %Y")

def plot_progress(filepath, display_name: str = "", axis_label: str = "Time", axis_date: str = "Date", axis_progress: str = "Progress"):
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
    if axis_date not in data.columns or axis_label not in data.columns or axis_progress not in data.columns:
        raise ValueError(f"Required columns '{axis_date}', '{axis_label}', or '{axis_progress}' are missing from the data.")

    display_name = display_name or "Progress Over Time"

    data[axis_date] = data[axis_date].apply(parse_date)
    data[axis_label] = data[axis_label]
    data[axis_progress] = data[axis_progress].str.replace(',', '.').astype(float)

    # Generate a complete date range
    full_date_range = pd.date_range(start=data[axis_date].min().floor('D'), end=data[axis_date].max().floor('D'), freq='D')
    data = data.set_index(data[axis_date].dt.floor('D')).reindex(full_date_range).reset_index()
    data.rename(columns={'index': 'FullDate'}, inplace=True)

    # Fill missing progress values with NaN
    data[axis_progress] = data[axis_progress].fillna(method='ffill')  # Forward fill for continuity

    # Plot the data as a stairs plot with filled area
    plt.figure(figsize=(10, 6))
    plt.step(data['FullDate'].dt.strftime('%d/%m'), data[axis_progress], where='post', label='Progress', color='blue')

    # Fill areas for empty days with red and others with blue
    for i in range(len(data) - 1):
        if pd.isna(data.loc[i, axis_label]):  # Check if the day is empty
            plt.fill_between(
                data.loc[i:i+1, 'FullDate'].dt.strftime('%d/%m'),
                data.loc[i:i+1, axis_progress],
                step='post',
                alpha=0.3,
                color='red'
            )
        else:
            plt.fill_between(
                data.loc[i:i+1, 'FullDate'].dt.strftime('%d/%m'),
                data.loc[i:i+1, axis_progress],
                step='post',
                alpha=0.3,
                color='blue'
            )

    # Add labels only for existing data points
    filtered_data = data.dropna(subset=[axis_label])  # Keep only original data points
    for i, row in filtered_data.iterrows():
        plt.text(row['FullDate'].strftime('%d/%m'), row[axis_progress], f"{row[axis_progress]} ({row[axis_label]})", fontsize=8, ha='right')

    # Configure plot
    plt.xlabel('Date (DD/MM)')
    plt.ylabel('Progress')
    plt.title(display_name)
    plt.ylim(0, 1)
    plt.grid(True)
    plt.tight_layout()

    # Save and show the plot
    # output_path = r'D:\Documents\Github\Forks\Dagda-scripts\plot\progress_plot.png'
    # plt.savefig(output_path)
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Plot progress from a TSV file.")
    parser.add_argument("filepath", help="Path to the TSV file containing the progress data.")
    parser.add_argument("--display_name", default="", help="Plot name to display as title.")
    parser.add_argument("--axis_time", "-t", default="Time", help="The time axis column name.")
    parser.add_argument("--axis_date", "-d", default="Date", help="The date axis column name.")
    parser.add_argument("--axis_progress", "-p", default="Progress", help="The progress axis column name.")

    args = parser.parse_args()

    plot_progress(
        filepath=args.filepath,
        display_name=args.display_name,
        axis_label=args.axis_time,
        axis_date=args.axis_date,
        axis_progress=args.axis_progress
    )
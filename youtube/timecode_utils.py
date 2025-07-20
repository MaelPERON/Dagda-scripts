import sys
import argparse
import pyperclip

def format_timecode(s: str):
	if not isinstance(s, str):
		return {}
	parts = [int(p) for p in s.split(':')]
	result = {}
	if len(parts) == 3:
		result['hour'] = parts[0]
		result['minute'] = parts[1]
		result['second'] = parts[2]
	elif len(parts) == 2:
		result['minute'] = parts[0]
		result['second'] = parts[1]
	elif len(parts) == 1:
		result['second'] = parts[0]
	return result

def get_percentage(current_str: str, duration_str: str):
	current = format_timecode(current_str)
	duration = format_timecode(duration_str)

	def to_seconds(tc):
		return tc.get('hour', 0) * 3600 + tc.get('minute', 0) * 60 + tc.get('second', 0)

	current_sec = to_seconds(current)
	duration_sec = to_seconds(duration)

	if not duration_sec:
		return None

	return current_sec / duration_sec

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("current_timecode", type=str)
	parser.add_argument("duration_timecode", type=str)
	args = parser.parse_args()

	current_timecode = args.current_timecode
	duration_timecode = args.duration_timecode
	percentage = get_percentage(current_timecode, duration_timecode)
	if percentage is not None:
		percentage_ = f"{percentage * 100:.2f}"
		print(f"Percentage: {percentage_}%")
		copy = input("Do you want to copy the percentage to clipboard? (y/n): ").strip().lower()
		if copy == 'y':
			pyperclip.copy(f"{percentage_}")
			print("Copied percentage to clipboard.")
	else:
		print("Duration is zero, cannot calculate percentage.")

	input("Press Enter to exit...")
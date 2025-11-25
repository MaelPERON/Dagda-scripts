import cv2 as cv
import argparse
import json
from pathlib import Path

def video_duration(video: Path) -> float:
	if not video.exists():
		raise FileExistsError(f"Video file {video} does not exist.")

	cap = cv.VideoCapture(str(video))
	if not cap.isOpened():
		raise IOError(f"Cannot open video file {video}.")
	
	frame_count = int(cap.get(cv.CAP_PROP_FRAME_COUNT))
	fps = cap.get(cv.CAP_PROP_FPS)
	seconds = frame_count / fps if fps > 0 else 0
	cap.release()

	return seconds
	
def format_seconds(seconds: float) -> str:
	hours = int(seconds // 3600)
	minutes = int((seconds % 3600) // 60)
	secs = int(seconds % 60)
	return f"{hours:02}:{minutes:02}:{secs:02}"

def scan_folder(folder: Path, output: Path | list[Path] = None):
	if not folder.exists() or not folder.is_dir():
		raise NotADirectoryError(f"Folder {folder} does not exist or is not a directory.")

	video_extensions = {'.mp4', '.avi', '.mov', '.mkv', '.flv'}
	videos = {}
	sum_seconds = 0.0

	print(f"Scanning folder: {folder}")

	for file in folder.glob('**/*'):
		if file.suffix.lower() in video_extensions:
			rel_path = file.relative_to(folder)
			duration = video_duration(file)
			videos[str(rel_path)] = (duration, format_seconds(duration))
			sum_seconds += duration
			print(f"\t{rel_path}: {format_seconds(duration)}")

	print(f"Scanning completed. Total duration: {format_seconds(sum_seconds)}")

	if output is not None:
		if not isinstance(output, list):
			output = [output]
	
		for path in output:
			print(f"Writing results to {path}")
			content = {
				"total_seconds": (sum_seconds, format_seconds(sum_seconds)),
				"folder": str(folder),
				"videos": videos,
			}
			with open(path, 'w') as f:
				match(path.suffix.lower()):
					case '.csv':
						f.write(format_table(content))
					case '.tsv':
						f.write(format_table(content, sep="\t"))
					case '.json':
						json.dump(content, f, indent=4)
				f.close()

		print("Results written successfully.")

def format_table(content: dict, sep: str = ",") -> str:
	lines = [f"Video{sep}Duration (HH:MM:SS)"]
	for video, (_, formatted_duration) in content["videos"].items():
		lines.append(f"{video}{sep}{formatted_duration}")
	lines.append(f"Total{sep}{content['total_seconds'][1]}")
	return "\n".join(lines)

def parse_path_from_string(path_str: str, root: Path = None) -> Path:
	if root is not None:
		print(root)
		return (root / path_str).expanduser().resolve()
	return Path(path_str).expanduser().resolve()

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Calculate video durations in a folder.")
	parser.add_argument("folder", type=str, help="Path to the folder containing video files.")
	parser.add_argument("-o", "--output", type=str, help="Output JSON file path.", default="")
	args = parser.parse_args()

	# folder = parse_path_from_string(args.folder)

	folder = parse_path_from_string(args.folder)
	output = None
	if args.output:
		output = [parse_path_from_string(out, root=folder) for out in args.output.split(",")]

	scan_folder(folder, output)
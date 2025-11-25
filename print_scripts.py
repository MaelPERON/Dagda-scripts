""" FILE TEMPLATE """

generated = "" # This will be replaced with the generation date and time
import argparse
scripts = [] # Will be populated with script identifiers

def print_scripts(folder: str = ""):
	global scripts
	head = ""
	print(f"Generated on: {generated}\n")
	print("Available scripts:")
	for script in scripts:
		script_group, script_name = script.split("-", 1)
		if folder and script_group != folder: continue
		if script_group != head:
			head = script_group
			print(f"\n{head.upper()}")
		print(f"{script_name}\t\t{script}")

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="List available scripts.")
	parser.add_argument("--folder", type=str, help="Filter scripts by folder/group", default="")
	args = parser.parse_args()

	print_scripts(args.folder)
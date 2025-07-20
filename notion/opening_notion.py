import os
import sys
import argparse
from subprocess import Popen

def open_notion_page(link: str, is_file: bool = False):
	if is_file:
		if os.path.isfile(link) and os.path.exists(link):
			with open(link, 'r') as file:
				link = file.read().strip()
		else:
			raise FileNotFoundError(f"The file {link} does not exist or is not a valid file path.")
	
	command = [
		"start",
		"",
		"notion:" + link,
		"&&", "exit"
	]

	if sys.platform.startswith('win'):
		Popen(command, shell=True, creationflags=0x08000000)
	else:
		raise NotImplementedError("This script is currently only implemented for Windows.")
	

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Open a Notion page using its link.")
	parser.add_argument("link", type=str, help="The Notion page link to open.")
	parser.add_argument("--is_file", action="store_true", help="Indicates if the link is a file path.")
	args = parser.parse_args()

	print(f"Opening Notion page: {args.link}")
	open_notion_page(args.link, args.is_file)
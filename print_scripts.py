""" FILE TEMPLATE """

scripts = [] # Will be populated with script identifiers

def print_scripts(folder: str = ""):
	head = ""
	print("Available scripts:")
	for script in scripts:
		script_group, script_name = script.split("-", 1)
		if folder and script_group != folder: continue
		if script_group != head:
			head = script_group
			print(f"\n{head.upper()}")
		print(f"{script_name}")

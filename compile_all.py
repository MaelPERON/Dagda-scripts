import argparse
from pathlib import Path
from py_compile import compile
from typing import Generator
from datetime import datetime

SCRIPT = Path(__file__)
SCRIPT_FOLDER = Path(__file__).parent
COMPILE_FOLDER = SCRIPT_FOLDER / "compiled"
EXCLUDE_FOLDERS = ["compiled", "tests", "data", "__pycache__", SCRIPT_FOLDER.name]

def list_scripts() -> Generator[tuple[Path, str], None, None]:
	"""Lists all Python scripts in the current directory."""
	for file in SCRIPT_FOLDER.glob("**/*.py"):
		folder_name = file.parent.name
		if not file.is_file(): continue # Ensure it's a file
		if file.name == SCRIPT.name: continue # Skip the current script
		if folder_name in EXCLUDE_FOLDERS: continue
		yield (file, f"{folder_name}-{file.stem}")

def read_template() -> str:
	return (SCRIPT_FOLDER / "print_scripts.py").read_text(encoding="utf-8")

def compile_all(folder: str = ""):
	scripts = []
	for file, identifier in list_scripts():
		folder_name = file.parent.name
		if folder and folder_name != folder: continue # Only compile scripts in the specified folder (if provided)
		print(f"Processing {identifier}...")
		scripts.append(identifier)
		compile_dest = COMPILE_FOLDER / f"{identifier}.pyc"
		compile(file, compile_dest)

	# Duplicating the template file and modifying it
	print_script_content = read_template().splitlines()
	print_script_content[2] = f"# Generated {datetime.now().strftime('%d/%m/%Y - %H:%M:%S')}"
	print_script_content[4] = f'scripts = {scripts!r}'
	del print_script_content[:2]

	# Creating a py file, compiling it, deleting it afterwards
	print_script_path = COMPILE_FOLDER / "print_scripts.py"
	print_script_path.write_text("\n".join(print_script_content), encoding="utf-8")
	compile(print_script_path, COMPILE_FOLDER / "print_scripts.pyc", doraise=True)
	print_script_path.unlink()

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Compile all Python scripts in subfolders.")
	parser.add_argument("--folder", type=str, default="", help="Only compile scripts in the specified folder")
	args = parser.parse_args()

	COMPILE_FOLDER.mkdir(exist_ok=True)
	compile_all(args.folder)
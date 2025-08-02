from pathlib import Path
from py_compile import compile
from typing import Generator

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

def compile_all():
	for file, identifier in list_scripts():
		print(f"Processing {identifier}...")
		compile_dest = COMPILE_FOLDER / f"{identifier}.pyc"
		compile(file, compile_dest)

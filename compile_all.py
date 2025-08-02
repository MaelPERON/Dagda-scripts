from pathlib import Path
from typing import Generator

SCRIPT = Path(__file__)
SCRIPT_FOLDER = Path(__file__).parent
COMPILE_FOLDER = SCRIPT_FOLDER / "compiled"

def list_scripts() -> Generator[tuple[Path, str], None, None]:
	"""Lists all Python scripts in the current directory."""
	for file in SCRIPT_FOLDER.glob("**/*.py"):
		folder_name = file.parent.name
		if not file.is_file(): continue # Ensure it's a file
		if file.name == SCRIPT.name: continue # Skip the current script
		if folder_name == "compiled": continue # Skip compiled scripts
		yield (file, f"{folder_name}-{file.stem}")

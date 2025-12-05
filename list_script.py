import os
import ast
from typing import List, Dict

BASE_DIRS = ["basic", "intermediate", "advanced"]

def get_py_files(base_dirs: List[str]) -> List[str]:
    py_files = []
    for base in base_dirs:
        if not os.path.isdir(base):
            continue
        for root, _, files in os.walk(base):
            for file in files:
                if file.endswith(".py"):
                    py_files.append(os.path.join(root, file))
    return py_files

def extract_header(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith('"""') or line.startswith("'''"):
                header = line.strip('"\' ')
                if header:
                    return header
                # If the first line is just the triple quotes, get the next line
                return next(f).strip()
    return "No description found."

def main():
    py_files = get_py_files(BASE_DIRS)
    summary: List[Dict[str, str]] = []
    for file in py_files:
        filename = os.path.basename(file)
        relpath = os.path.relpath(file)
        description = extract_header(file)
        summary.append({"filename": filename, "relpath": relpath, "description": description})

    # Prepare markdown table with clickable links
    table_header = "| Script | Description |\n|--------|-------------|\n"
    table_rows = [f"| [{entry['filename']}]({entry['relpath']}) | {entry['description']} |" for entry in summary]
    table = table_header + "\n".join(table_rows) + "\n"

    # Read README.md
    readme_path = "README.md"
    with open(readme_path, "r", encoding="utf-8") as f:
        readme = f.read()

    # Replace or insert Tutorials Index section
    import re
    pattern = r'(## Tutorials Index\n)([\s\S]*?)(\n\n|\Z)'
    replacement = f"## Tutorials Index\n\n{table}\n"
    if re.search(pattern, readme):
        readme = re.sub(pattern, replacement, readme)
    else:
        # If not found, append at the end
        readme += f"\n{replacement}"

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme)

    print("README.md updated with Tutorials Index.")

if __name__ == "__main__":
    main()

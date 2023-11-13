import pathlib
import sys

#path main.py to include all the needed modules

lib_path = pathlib.Path(sys.argv[1]).resolve()
base_path = pathlib.Path(__file__).resolve().parent
main_path = base_path / "main.py"
main_text = main_path.read_text()

exclude = [
  "ensurepip",
  "pip",
  "test",
  "tkinter",
  "turtledemo",
  "unittest",
  "turtle"
]

def find_modules(search_path):
  modules = []
  for path in search_path.iterdir():
    if path.name == "__init__.py" or "-" in path.name:
      continue

    name = path.stem
    if name in exclude:
      continue

    if path.is_file() and path.suffix == ".py":
      modules.append(name)
    elif path.is_dir() and (path / "__init__.py").exists():
      modules.append(name)
  
  return modules

module_names = find_modules(lib_path)
modules_string = ",".join(module_names)
new_main = main_text.replace("pass #modules_here", f"import {modules_string}", 1)

print(new_main)
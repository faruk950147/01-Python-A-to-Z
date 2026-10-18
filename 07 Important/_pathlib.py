import pathlib

# Create a Path object for a file named "data.txt"
path = pathlib.Path("data.txt") 
print(f"Path: {path}")

# Get the parent directory of the current file
parent = pathlib.Path(__file__).parent
print(f"Parent: {parent}")

# Get the absolute path of the current file
parent_path = pathlib.Path(__file__).resolve().parent.parent
print(f"Parent Path: {parent_path}")



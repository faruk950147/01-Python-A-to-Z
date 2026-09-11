import pathlib

path = pathlib.Path("example.txt") # creates a path object
print(f"Path: {path}")
parent = pathlib.Path(__file__).parent # gets the parent directory of the current file
print(f"Parent: {parent}")

parent_path = pathlib.Path(__file__).resolve().parent.parent
print(f"Parent Path: {parent_path}")



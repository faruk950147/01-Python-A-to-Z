# Python Package Building — Complete Notes

## 1. What Is a Python Package?

A **Python package** is a way to organize related Python modules and files into a directory structure so that code can be reused and distributed.

### Benefits of Python Packages

- Code reusability
- Easy distribution
- Better code organization
- Easy installation
- Version management
- Sharing code between projects

## 2. Module vs Package

### Module

A Python module is a single Python file.

Example:

```text
mathematics.py
```

### Package

A package organizes one or more Python modules in a directory.

Example:

```text
mathematics/
├── __init__.py
├── mathematics.py
└── geometry.py
```

The `__init__.py` file is commonly used to identify a package and define package-level imports.

## 3. Create a Python Package

Create the project directory:

```bash
mkdir mathematics-package
cd mathematics-package
mkdir mathematics
```

Project structure:

```text
mathematics-package/
├── pyproject.toml
├── README.md
└── mathematics/
    ├── __init__.py
    └── mathematics.py
```

## 4. Create the Calculator Module

File: `mathematics/mathematics.py`

```python
class Mathematics:
    def addition(self, *args):
        return sum(args)

    def subtraction(self, *args):
        if not args:
            return 0

        result = args[0]

        for number in args[1:]:
            result -= number

        return result
```

### Explanation

- `class Mathematics`: Defines a class.
- `addition()`: Calculates the sum of numbers.
- `subtraction()`: Subtracts subsequent numbers from the first number.
- `*args`: Accepts any number of positional arguments.
- `sum(args)`: Returns the sum of the supplied numbers.

Example:

```python
math = Mathematics()

print(math.addition(10, 20, 30))
print(math.subtraction(20, 5, 3))
```

Output:

```text
60
12
```

## 5. Configure `__init__.py`

File: `mathematics/__init__.py`

```python
from .mathematics import Mathematics

__all__ = ["Mathematics"]
```

The relative import makes `Mathematics` available directly from the package.

You can now write:

```python
from mathematics import Mathematics
```

`__all__` defines the names intended for wildcard imports.

## 6. What Is `pyproject.toml`?

`pyproject.toml` is a standard configuration file for Python project metadata and build-system settings.

Create the file in the project root:

```toml
[build-system]
requires = ["setuptools>=61"]
build-backend = "setuptools.build_meta"

[project]
name = "faruk-mathematics"
version = "0.1.0"
description = "A simple mathematics package"
requires-python = ">=3.9"

[tool.setuptools.packages.find]
include = ["mathematics*"]
```

### Important Fields

- **`build-system`**: Defines the build system.
- **`requires`**: Specifies the dependencies needed to build the package.
- **`build-backend`**: Specifies the backend used to build distributions.
- **`name`**: The distribution name.
- **`version`**: The package version.
- **`description`**: A short description of the package.
- **`requires-python`**: Specifies the supported Python versions.
- **`packages.find`**: Configures package discovery for setuptools.

## 7. Distribution Name vs Import Name

In `pyproject.toml`:

```toml
name = "faruk-mathematics"
```

The distribution name is `faruk-mathematics`.

However, the Python import name is `mathematics`:

```python
from mathematics import Mathematics
```

The distribution name and import name do not have to be identical.

## 8. Install the Build Tool

Run this command:

```bash
python -m pip install --upgrade build
```

Explanation:

- `python -m`: Runs a Python module.
- `pip`: Installs Python packages.
- `install`: Installs a package.
- `--upgrade`: Upgrades the package if needed.
- `build`: The Python package build tool.

## 9. Build the Package

Run the command from the project root, where `pyproject.toml` is located:

```bash
python -m build
```

A successful build typically generates two distribution files:

```text
dist/
├── faruk_mathematics-0.1.0.tar.gz
└── faruk_mathematics-0.1.0-py3-none-any.whl
```

### Source Distribution — `.tar.gz`

A source distribution, or `sdist`, is an archive containing source files and other files included by the build configuration.

It may require a build step during installation.

### Wheel Distribution — `.whl`

A wheel is a built Python distribution format.

It can generally be installed without building the package from its source distribution.

### Understanding the Wheel Filename

```text
faruk_mathematics-0.1.0-py3-none-any.whl
```

- `faruk_mathematics`: Distribution name, normalized for the filename.
- `0.1.0`: Package version.
- `py3`: Python 3 compatibility tag.
- `none`: No specific Python ABI requirement.
- `any`: Not restricted to a particular platform.

## 10. Install the Built Package

Install the wheel:

```bash
python -m pip install dist/faruk_mathematics-0.1.0-py3-none-any.whl
```

Verify the installation:

```bash
python -m pip show faruk-mathematics
```

Test the package import:

```bash
python -c "from mathematics import Mathematics; print(Mathematics().addition(5, 5))"
```

Expected output:

```text
10
```

## 11. Test the Package from Another Directory

Create a `main.py` file outside the project directory:

```python
from mathematics import Mathematics

math = Mathematics()

print(math.addition(9, 9))
print(math.subtraction(20, 5, 3))
```

Output:

```text
18
12
```

Testing from another directory helps verify that Python imports the installed package rather than accidentally importing files from the project directory.

## 12. Inspect the Distribution Files

List the files inside the wheel:

```bash
python -m zipfile -l dist/faruk_mathematics-0.1.0-py3-none-any.whl
```

List the files inside the source distribution:

```bash
tar -tzf dist/faruk_mathematics-0.1.0.tar.gz
```

Check that the required Python modules and metadata are included.

## 13. Common Problems

### Problem 1: `ModuleNotFoundError`

Possible causes:

- The package is not installed.
- The wrong Python environment is being used.
- The package structure is incorrect.

Solution:

```bash
python -m pip install dist/faruk_mathematics-0.1.0-py3-none-any.whl
```

### Problem 2: `No module named build`

Solution:

```bash
python -m pip install --upgrade build
```

### Problem 3: Old Build Files

Remove old generated files before rebuilding if necessary:

- `dist/`
- `build/`
- The relevant `.egg-info` directory

Then run:

```bash
python -m build
```

**Important:** Remove generated files only, not your source code.

### Problem 4: Missing Package Files

Check the package discovery configuration in `pyproject.toml`. If the package contains additional data files, configure the build backend to include them.

## 14. Complete Build Workflow

```text
Create Project
      ↓
Create Python Modules
      ↓
Create __init__.py
      ↓
Configure pyproject.toml
      ↓
Install the Build Tool
      ↓
Run python -m build
      ↓
Generate .tar.gz and .whl
      ↓
Install the Wheel
      ↓
Test Imports and Functionality
```

## 15. Important Commands Cheat Sheet

| Command | Purpose |
|---|---|
| `python --version` | Check the Python version |
| `python -m pip --version` | Check the pip version |
| `python -m pip install --upgrade build` | Install or upgrade the build tool |
| `python -m build` | Build the package distributions |
| `python -m pip install dist/package.whl` | Install a wheel |
| `python -m pip show package-name` | Display installed package information |
| `python -m zipfile -l dist/package.whl` | List wheel contents |
| `tar -tzf dist/package.tar.gz` | List source archive contents |

## Conclusion

The main purpose of building a Python package is to make your code reusable, installable, and distributable.

Remember these key concepts:

1. Python modules and packages
2. The purpose of `__init__.py`
3. `pyproject.toml` configuration
4. Building distributions with `python -m build`
5. Differences between `.tar.gz` and `.whl`
6. Installing and testing the built package

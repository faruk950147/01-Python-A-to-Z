# Python Package Building — বাংলা নোট

## 1. What Is a Python Package?

**Python Package** হলো Python modules এবং অন্যান্য প্রয়োজনীয় ফাইলকে একটি নির্দিষ্ট directory structure-এ সাজানোর পদ্ধতি, যাতে সেগুলো অন্য Python project-এ পুনরায় ব্যবহার করা যায়।

উদাহরণ:

```text
mathematics-package/
├── pyproject.toml
├── README.md
├── mathematics/
│   ├── __init__.py
│   └── calculator.py
└── dist/
```

### Benefits of Python Packages

- Code reusability
- Easy distribution
- Better code organization
- Easy installation
- Project sharing
- Version management

## 2. Python Module vs Package

### Module

একটি Python file-কে module বলা হয়।

উদাহরণ:

```text
calculator.py
```

### Package

একটি directory-তে এক বা একাধিক Python module সংগঠিত থাকলে সেটিকে সাধারণত package বলা হয়।

উদাহরণ:

```text
mathematics/
├── __init__.py
├── calculator.py
└── geometry.py
```

`__init__.py` প্রচলিতভাবে package directory চিহ্নিত করে এবং package-level imports নির্ধারণ করতে সাহায্য করে।

## 3. Create a Python Package

প্রথমে project directory তৈরি করো:

```bash
mkdir mathematics-package
cd mathematics-package
mkdir mathematics
```

তারপর এই structure তৈরি করো:

```text
mathematics-package/
├── pyproject.toml
├── README.md
└── mathematics/
    ├── __init__.py
    └── calculator.py
```

## 4. Create the Calculator Module

`mathematics/calculator.py`

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

- `class Mathematics`: একটি class তৈরি করে।
- `addition()`: একাধিক সংখ্যার যোগফল বের করে।
- `subtraction()`: প্রথম সংখ্যা থেকে পরবর্তী সংখ্যাগুলো বিয়োগ করে।
- `*args`: যেকোনো সংখ্যক positional arguments গ্রহণ করে।
- `sum(args)`: সব সংখ্যার যোগফল return করে।

Example:

```python
math.addition(10, 20, 30)
# 60

math.subtraction(20, 5, 3)
# 12
```

## 5. Configure `__init__.py`

`mathematics/__init__.py`

```python
from .calculator import Mathematics

__all__ = ["Mathematics"]
```

### Explanation

`from .calculator import Mathematics` ব্যবহার করে `calculator.py` থেকে class-টি import করা হয়েছে।

এখন ব্যবহার করা যাবে:

```python
from mathematics import Mathematics
```

`__all__` হলো wildcard import-এর জন্য নির্ধারিত public names-এর তালিকা।

## 6. What Is `pyproject.toml`?

`pyproject.toml` হলো Python project-এর build system এবং project configuration নির্ধারণের একটি standard configuration file।

Project root-এ `pyproject.toml` তৈরি করো:

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

**`[build-system]`**

Package build করার জন্য প্রয়োজনীয় backend ও build dependencies নির্ধারণ করে।

**`requires`**

Build করার সময় কোন packages প্রয়োজন তা নির্ধারণ করে।

**`build-backend`**

এখানে `setuptools` build backend হিসেবে ব্যবহৃত হয়েছে।

**`[project]`**

Package-এর metadata নির্ধারণ করে।

**`name`**

Distribution-এর নাম।

**`version`**

Package-এর version।

**`requires-python`**

Package-এর জন্য প্রয়োজনীয় Python version নির্ধারণ করে।

**`[tool.setuptools.packages.find]`**

`setuptools`-কে কোন Python packages খুঁজে build-এ অন্তর্ভুক্ত করতে হবে তা জানায়।

## 7. Distribution Name vs Import Name

এই উদাহরণে:

```toml
name = "faruk-mathematics"
```

Distribution name হলো `faruk-mathematics`।

কিন্তু Python code-এ import করতে হবে:

```python
from mathematics import Mathematics
```

এখানে `mathematics` হলো import package name।

দুটোর নাম একই হওয়া বাধ্যতামূলক নয়।

## 8. Install the Build Tool

Terminal-এ চালাও:

```bash
python -m pip install --upgrade build
```

এখানে:

- `python -m`: Python interpreter দিয়ে module চালায়।
- `pip`: Python package installer।
- `install`: package install করে।
- `--upgrade`: installed version থাকলে upgrade করার চেষ্টা করে।
- `build`: Python distribution তৈরির tool।

## 9. Build the Package

Project root directory থেকে চালাও:

```bash
python -m build
```

সাধারণত দুটি distribution তৈরি হবে:

```text
dist/
├── faruk_mathematics-0.1.0.tar.gz
└── faruk_mathematics-0.1.0-py3-none-any.whl
```

### `.tar.gz` — Source Distribution

Source Distribution বা `sdist` হলো source files-সহ তৈরি একটি archive।

এটি সাধারণত `.tar.gz` format-এ থাকে।

### `.whl` — Wheel Distribution

Wheel হলো Python package distribution-এর একটি built format।

সাধারণত এটি install করার সময় source distribution-এর মতো build step প্রয়োজন হয় না।

### Wheel Filename Explanation

```text
faruk_mathematics-0.1.0-py3-none-any.whl
```

- `faruk_mathematics`: Distribution name
- `0.1.0`: Version
- `py3`: Python 3
- `none`: নির্দিষ্ট Python ABI tag নেই
- `any`: নির্দিষ্ট operating system বা CPU architecture-এর জন্য সীমাবদ্ধ নয়

## 10. Install the Built Package

Wheel install করো:

```bash
python -m pip install dist/faruk_mathematics-0.1.0-py3-none-any.whl
```

Package install হয়েছে কি না যাচাই করো:

```bash
python -m pip show faruk-mathematics
```

Package import test:

```bash
python -c "from mathematics import Mathematics; print(Mathematics().addition(5, 5))"
```

Expected output:

```text
10
```

## 11. Test the Package from Another Directory

Project directory-এর বাইরে একটি `main.py` ফাইল তৈরি করো:

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

এভাবে পরীক্ষা করলে বর্তমান project directory থেকে accidental import হওয়ার সম্ভাবনা কমে এবং installed package যাচাই করা সহজ হয়।

## 12. Inspect the Built Files

Wheel-এর ভেতরের ফাইলগুলো দেখতে:

```bash
python -m zipfile -l dist/faruk_mathematics-0.1.0-py3-none-any.whl
```

Source Distribution-এর ফাইলগুলো দেখতে:

```bash
tar -tzf dist/faruk_mathematics-0.1.0.tar.gz
```

Package-এর প্রয়োজনীয় module ও metadata অন্তর্ভুক্ত হয়েছে কি না পরীক্ষা করো।

## 13. Common Problems

### Problem 1: `ModuleNotFoundError`

সম্ভাব্য কারণ:
- Package install করা হয়নি।
- ভুল Python environment ব্যবহার করা হচ্ছে।
- Package-এর directory structure ভুল।

সমাধান:

```bash
python -m pip install dist/faruk_mathematics-0.1.0-py3-none-any.whl
```

### Problem 2: `No module named build`

সমাধান:

```bash
python -m pip install --upgrade build
```

### Problem 3: Old Build Files

নতুন করে build করার আগে পুরোনো generated files সরিয়ে নিতে পারো:

```bash
python -m pip install --upgrade build
```

তারপর `dist/`, `build/` এবং প্রাসঙ্গিক `.egg-info` directory সরিয়ে আবার build করো:

```bash
python -m build
```

সতর্কতা: শুধু generated files সরাবে, source code নয়।

### Problem 4: Package Files Missing

`pyproject.toml`-এ package discovery configuration পরীক্ষা করো। অতিরিক্ত data files থাকলে build backend অনুযায়ী সেগুলো অন্তর্ভুক্ত করার configuration-ও প্রয়োজন হতে পারে।

## 14. Complete Workflow

```text
Create Project
      ↓
Create Python Modules
      ↓
Create __init__.py
      ↓
Configure pyproject.toml
      ↓
Install build Tool
      ↓
Run python -m build
      ↓
Generate .tar.gz and .whl
      ↓
Install Wheel
      ↓
Test Import and Functionality
```

## 15. Important Commands Cheat Sheet

| Command | Purpose |
|---|---|
| `python --version` | Python version দেখা |
| `python -m pip --version` | pip version দেখা |
| `python -m pip install --upgrade build` | Build tool install বা upgrade |
| `python -m build` | Package distribution তৈরি |
| `python -m pip install dist/package.whl` | Wheel install |
| `python -m pip show package-name` | Installed package-এর তথ্য দেখা |
| `python -m zipfile -l dist/package.whl` | Wheel-এর ফাইল দেখা |
| `tar -tzf dist/package.tar.gz` | Source archive-এর ফাইল দেখা |

## Conclusion

Python package build করার মূল উদ্দেশ্য হলো নিজের Python code-কে reusable, installable এবং distributable করা।

মূলত এই বিষয়গুলো মনে রাখবে:

1. Python module ও package-এর পার্থক্য।
2. `__init__.py`-এর ব্যবহার।
3. `pyproject.toml` configuration।
4. `python -m build` দিয়ে distribution তৈরি।
5. `.tar.gz` ও `.whl`-এর পার্থক্য।
6. Wheel install করে package পরীক্ষা করা।

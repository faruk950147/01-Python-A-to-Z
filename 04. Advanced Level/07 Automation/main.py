"""
# Python Automation + Shutil + Selenium + Playwright

## Easy English Full Notes

---

# 1. What is Python Automation?

**Python Automation** means using Python programs or scripts to perform repetitive or manual tasks automatically.

Simple idea:

```text
Manual / Repetitive Work
        ↓
   Python Script
        ↓
Computer does the work automatically
```

### Examples

Python can automate:

* File renaming
* File copying and moving
* Folder organization
* Backup creation
* Excel report generation
* CSV processing
* Web scraping
* Browser automation
* Form filling
* Sending emails
* PDF generation
* Database backup
* API requests
* Scheduled tasks

### Simple Definition

> **Python Automation = Using Python to make repetitive work automatic.**

---

# 2. Advantages of Python Automation

Python automation can:

1. Save time
2. Reduce repetitive manual work
3. Reduce human errors
4. Increase productivity
5. Process large amounts of data
6. Perform the same task consistently
7. Automate business processes
8. Improve developer productivity

---

# 3. Main Areas of Python Automation

Python can be used for:

1. File and Folder Automation
2. Excel / CSV Automation
3. Web Automation
4. Web Scraping
5. Email Automation
6. Task Scheduling
7. Desktop / GUI Automation
8. PDF / Document Automation
9. Database Automation
10. API Automation
11. Image Automation
12. Testing Automation

---

# 4. Important Python Automation Libraries

| Task                 | Library       | Main Use                    |
| -------------------- | ------------- | --------------------------- |
| File operations      | `os`          | List, rename, delete, paths |
| File operations      | `shutil`      | Copy, move, delete          |
| Path handling        | `pathlib`     | Modern path management      |
| Browser automation   | Selenium      | Control browsers            |
| Browser automation   | Playwright    | Modern browser automation   |
| HTTP requests        | Requests      | API/web requests            |
| HTML parsing         | BeautifulSoup | Parse HTML                  |
| Web crawling         | Scrapy        | Large-scale crawling        |
| Data processing      | Pandas        | Data analysis               |
| Excel                | openpyxl      | Read/write XLSX             |
| GUI automation       | PyAutoGUI     | Mouse/keyboard              |
| Email sending        | smtplib       | Send emails                 |
| Email reading        | imaplib       | Read emails                 |
| Scheduling           | schedule      | Run tasks at specific times |
| File monitoring      | watchdog      | Detect file changes         |
| PDF creation         | ReportLab     | Create PDFs                 |
| PDF extraction       | pdfplumber    | Extract PDF data            |
| Image processing     | Pillow        | Process images              |
| Database             | sqlite3       | SQLite database             |
| Database abstraction | SQLAlchemy    | Database access/ORM         |
| Async programming    | asyncio       | Asynchronous tasks          |

---

# 5. Python Automation Roadmap

## Level 1 — Python Basics

First learn:

* Variables
* Data types
* List
* Tuple
* Set
* Dictionary
* `if/else`
* `for` loop
* `while` loop
* Functions
* Modules
* Packages
* Exception handling
* File handling
* Virtual environments

---

## Level 2 — File and Folder Automation

Learn:

```text
os
shutil
pathlib
```

Practice:

* Rename files
* Copy files
* Move files
* Delete files
* Create folders
* Create backups
* Build a file organizer

---

## Level 3 — Excel / CSV Automation

Libraries:

```text
pandas
openpyxl
csv
```

Practice:

* Read CSV
* Write CSV
* Read Excel
* Write Excel
* Filter data
* Generate reports
* Merge Excel data

---

## Level 4 — Web Automation

Libraries:

```text
Selenium
Playwright
requests
```

Practice:

* Open websites
* Login
* Fill forms
* Click buttons
* Extract data
* Take screenshots
* Generate PDFs

---

## Level 5 — Web Scraping

Libraries:

```text
requests
BeautifulSoup
Scrapy
Playwright
```

Practice:

* Product scraping
* News scraping
* Table scraping
* Pagination
* Dynamic website scraping

---

## Level 6 — Email Automation

Libraries:

```text
smtplib
email
imaplib
```

Practice:

* Send email
* Read email
* Send daily reports
* Send attachments

---

## Level 7 — Task Scheduling

Libraries/tools:

```text
schedule
datetime
time
cron
```

Practice:

* Daily reports
* Periodic API requests
* Automatic backups
* Scheduled scraping

---

## Level 8 — Desktop Automation

Libraries:

```text
pyautogui
pynput
```

Practice:

* Mouse movement
* Mouse clicking
* Keyboard typing
* Screenshots
* Desktop application control

---

## Level 9 — Advanced Automation

Learn:

* `asyncio`
* `threading`
* `multiprocessing`
* API automation
* Database automation
* Logging
* Retry systems
* Configuration
* Deployment

---

## Level 10 — Real Projects

Build:

1. Auto File Organizer
2. Auto Backup System
3. Excel Report Generator
4. Daily Email Reporter
5. Web Scraper
6. Price Tracker
7. Auto Form Filler
8. Website Testing System
9. Database Backup System
10. Django Automation System

---

# 6. What is `shutil`?

`shutil` is a Python **standard library module** for high-level file and directory operations.

The name comes from **Shell Utilities**.

It is mainly used for:

* Copying files
* Moving files
* Copying folders
* Deleting folders
* Working with directory trees

---

# 7. Important `shutil` Methods

## `shutil.copy()`

Copies a file.

```python
import shutil

shutil.copy(
    "source.txt",
    "destination.txt"
)
```

---

## `shutil.copy2()`

Copies a file and tries to preserve file metadata such as modification time.

```python
shutil.copy2(
    "source.txt",
    "backup.txt"
)
```

---

## `shutil.copytree()`

Copies an entire directory tree.

```python
shutil.copytree(
    "my_folder",
    "backup_folder"
)
```

---

## `shutil.move()`

Moves a file or directory.

```python
shutil.move(
    "file.txt",
    "new_folder/file.txt"
)
```

---

## `shutil.rmtree()`

Deletes a directory and all of its contents recursively.

```python
shutil.rmtree("old_folder")
```

### Warning

Be careful with `rmtree()`.

It can delete the entire directory tree, including all files and subfolders.

---

# 8. `os` + `shutil`

### `os`

Commonly used for:

* File paths
* Directory listing
* Checking file existence
* Rename operations
* Basic operating-system operations

### `shutil`

Commonly used for:

* Copy
* Move
* Directory copy
* Recursive directory deletion

Example:

```python
import os
import shutil

source = "source.txt"
destination = "backup.txt"

if os.path.exists(source):
    shutil.copy(source, destination)

print("Backup completed")
```

---

# 9. `pathlib`

`pathlib` provides a modern and convenient way to work with file paths.

Example:

```python
from pathlib import Path

base = Path("files")

for file in base.iterdir():
    print(file)
```

### Check if a file exists

```python
path = Path("test.txt")

if path.exists():
    print("File exists")
```

### Create a folder

```python
Path("backup").mkdir(exist_ok=True)
```

### Why use `pathlib`?

It makes path-related code cleaner and more portable across operating systems.

---

# 10. Simple File Automation Project

Example:

```python
import os
import shutil

source_folder = "files"
backup_folder = "backup"

if not os.path.exists(backup_folder):
    os.mkdir(backup_folder)

for count, filename in enumerate(
    os.listdir(source_folder),
    start=1
):
    old_path = os.path.join(
        source_folder,
        filename
    )

    new_name = f"file_{count}.txt"

    new_path = os.path.join(
        backup_folder,
        new_name
    )

    shutil.move(
        old_path,
        new_path
    )

print("Files successfully moved!")
```

### Flow

```text
files/
   ↓
Rename
   ↓
backup/
```

Example:

```text
file1.txt → file_1.txt
file2.txt → file_2.txt
file3.txt → file_3.txt
```

### Important

This simple example assumes that all items are files and can safely be renamed to `.txt`.

In a real project, it is better to preserve the original extension.

---

# 11. Rename Files While Preserving Extension

```python
import os

folder = "files"

for i, filename in enumerate(
    os.listdir(folder),
    start=1
):

    old_path = os.path.join(
        folder,
        filename
    )

    name, ext = os.path.splitext(filename)

    new_name = f"file_{i}{ext}"

    new_path = os.path.join(
        folder,
        new_name
    )

    os.rename(
        old_path,
        new_path
    )

print("Rename completed")
```

Example:

```text
photo.jpg   → file_1.jpg
data.csv    → file_2.csv
report.pdf  → file_3.pdf
```

---

# 12. Safe File Copy

```python
import os
import shutil

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

source = os.path.join(
    BASE_DIR,
    "source.txt"
)

destination = os.path.join(
    BASE_DIR,
    "destination.txt"
)

if not os.path.exists(source):

    print("Source file does not exist")

else:

    if os.path.exists(destination):

        base, ext = os.path.splitext(
            destination
        )

        counter = 1

        while os.path.exists(
            f"{base}_{counter}{ext}"
        ):
            counter += 1

        destination = (
            f"{base}_{counter}{ext}"
        )

    shutil.copy(
        source,
        destination
    )

    print(
        f"File copied to {destination}"
    )
```

If `destination.txt` already exists, this code creates:

```text
destination_1.txt
destination_2.txt
destination_3.txt
```

instead of overwriting the existing file.

---

# 13. File Organizer Automation

A file organizer can move files into folders based on their extensions.

Example:

```text
Downloads/
│
├── photo.jpg
├── photo.png
├── document.pdf
├── data.csv
└── movie.mp4
```

After automation:

```text
Downloads/
│
├── images/
│   ├── photo.jpg
│   └── photo.png
│
├── documents/
│   └── document.pdf
│
├── csv/
│   └── data.csv
│
└── videos/
    └── movie.mp4
```

This is a good beginner automation project.

---

# 14. What is Selenium?

**Selenium** is an open-source framework used for **browser automation and web testing**.

It can control a real browser programmatically.

### Selenium can:

* Open websites
* Click buttons
* Fill forms
* Login
* Navigate between pages
* Take screenshots
* Test web applications
* Interact with dynamic websites

---

# 15. Selenium Use Cases

Common uses:

1. Web testing
2. UI testing
3. Login automation
4. Form automation
5. Browser automation
6. Dynamic website interaction
7. Repetitive browser tasks

---

# 16. Selenium Components

## 1. Selenium WebDriver

The most important component for browser control.

It allows Python code to control browsers.

---

## 2. Selenium IDE

A record-and-playback testing tool.

---

## 3. Selenium Grid

Used for running tests across multiple machines, browsers, or environments.

---

## 4. Selenium RC

An old Selenium technology.

It is not used for modern Selenium development.

---

# 17. Selenium Supported Languages

Selenium supports several programming languages, including:

* Python
* Java
* C#
* JavaScript
* Ruby

---

# 18. Selenium Installation

Install:

```bash
pip install selenium
```

Modern Selenium can often manage browser drivers through **Selenium Manager**, making driver setup easier.

Basic example:

```python
from selenium import webdriver

driver = webdriver.Chrome()

driver.get(
    "https://example.com"
)

print(driver.title)

driver.quit()
```

### Important

Always close the browser when your automation is finished:

```python
driver.quit()
```

---

# 19. Finding Elements in Selenium

## By ID

```python
driver.find_element(
    "id",
    "email"
)
```

## By Name

```python
driver.find_element(
    "name",
    "password"
)
```

## By XPath

```python
driver.find_element(
    "xpath",
    "//input[@type='text']"
)
```

## By CSS Selector

```python
driver.find_element(
    "css selector",
    ".class_name"
)
```

### Recommended style

```python
from selenium.webdriver.common.by import By

element = driver.find_element(
    By.ID,
    "email"
)
```

Using `By` makes Selenium code clearer and easier to maintain.

---

# 20. Selenium Actions

## Click

```python
element.click()
```

## Type text

```python
element.send_keys("Hello")
```

## Clear input

```python
element.clear()
```

## Get text

```python
print(element.text)
```

## Get an attribute

```python
print(
    element.get_attribute("href")
)
```

---

# 21. Selenium Waits

Waiting is very important in browser automation.

A webpage may take time to load.

If your code searches for an element before it is ready, the automation can fail.

---

## Implicit Wait

```python
driver.implicitly_wait(10)
```

This tells Selenium to wait for an element during element searches, up to the specified timeout.

---

## Explicit Wait

Explicit wait waits for a specific condition.

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(
    driver,
    10
)

email = wait.until(
    EC.presence_of_element_located(
        (By.ID, "email")
    )
)
```

### Simple idea

```text
Wait
 ↓
Condition becomes true
 ↓
Perform action
```

### Best Practice

Do not solve every timing problem using:

```python
time.sleep(10)
```

Condition-based waits are usually more reliable.

---

# 22. Selenium Headless Mode

A **headless browser** runs without displaying the normal browser window.

Example:

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()

options.add_argument("--headless")

driver = webdriver.Chrome(
    options=options
)

driver.get(
    "https://example.com"
)

print(driver.title)

driver.quit()
```

### Headless

```text
Browser works
     ↓
No visible browser window
```

This is useful for servers and automated jobs.

---

# 23. Selenium Screenshot

```python
driver.save_screenshot(
    "page.png"
)
```

This saves the current browser view as an image.

---

# 24. Selenium Navigation

```python
driver.get(
    "https://example.com"
)

driver.back()

driver.forward()

driver.refresh()
```

---

# 25. Selenium Multiple Tabs/Windows

Get window handles:

```python
window_handles = driver.window_handles
```

Switch to another window:

```python
driver.switch_to.window(
    window_handles[1]
)
```

You should make sure the required window actually exists before accessing a specific index.

---

# 26. Selenium Cookies

### Get cookies

```python
cookies = driver.get_cookies()

print(cookies)
```

### Add a cookie

```python
driver.add_cookie({
    "name": "test",
    "value": "123"
})
```

Cookies can be useful when working with sessions and authentication.

---

# 27. Selenium Login Automation

Example:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get(
    "https://example.com/login"
)

wait = WebDriverWait(
    driver,
    10
)

username = wait.until(
    EC.presence_of_element_located(
        (By.ID, "username")
    )
)

password = driver.find_element(
    By.ID,
    "password"
)

username.send_keys("admin")

password.send_keys("1234")

driver.find_element(
    By.ID,
    "login"
).click()

print(driver.title)

driver.quit()
```

### Note

Never put real passwords directly in source code.

Use environment variables or a secure secret-management system.

---

# 28. Selenium Advantages

* Controls real browsers
* Can interact with JavaScript websites
* Very popular for testing
* Supports multiple browsers
* Large ecosystem
* Good documentation and community

---

# 29. Selenium Disadvantages

* Browser process is relatively resource-heavy
* Usually slower than direct HTTP requests
* Large-scale crawling can be inefficient
* Browser automation needs more resources than simple HTTP scraping

---

# 30. What is Playwright?

**Playwright** is a modern framework for browser automation and testing.

It can be used with Python for:

* Browser automation
* Web testing
* Dynamic website interaction
* Data extraction
* Screenshots
* PDF generation

---

# 31. Playwright Browser Support

Playwright supports:

* Chromium
* Firefox
* WebKit

Chromium is used for Chromium-based browser automation.

WebKit is the browser engine used by Safari.

---

# 32. Playwright Installation

Install the Python package:

```bash
pip install playwright
```

Then install the required browsers:

```bash
playwright install
```

---

# 33. Playwright Basic Setup

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=False
    )

    page = browser.new_page()

    page.goto(
        "https://example.com"
    )

    print(page.title())

    browser.close()
```

---

# 34. Playwright Browser Types

### Chromium

```python
p.chromium.launch()
```

### Firefox

```python
p.firefox.launch()
```

### WebKit

```python
p.webkit.launch()
```

---

# 35. Playwright Headless Mode

### Headless

```python
browser = p.chromium.launch(
    headless=True
)
```

### Headful

```python
browser = p.chromium.launch(
    headless=False
)
```

During development, `headless=False` is useful because you can see what the browser is doing.

For automated server tasks, `headless=True` is often useful.

---

# 36. Playwright Selectors

## CSS

```python
page.locator("button")
```

## ID

```python
page.locator("#username")
```

## Class

```python
page.locator(".product")
```

## Text

```python
page.get_by_text("Submit")
```

## Role-based locator

```python
page.get_by_role(
    "button",
    name="Submit"
)
```

### Best Practice

Prefer Playwright's locator APIs, especially semantic locators such as:

```python
page.get_by_role()
page.get_by_text()
page.locator()
```

They often make automation code easier to understand and maintain.

---

# 37. Playwright Actions

## Fill

```python
page.fill(
    "#username",
    "admin"
)
```

## Click

```python
page.click(
    "#login"
)
```

## Hover

```python
page.hover(
    "#menu"
)
```

## Check

```python
page.check(
    "#checkbox"
)
```

## Select option

```python
page.select_option(
    "#dropdown",
    "Bangladesh"
)
```

---

# 38. Playwright Text Extraction

```python
element = page.locator("h1")

print(
    element.text_content()
)
```

You can also use:

```python
print(
    page.locator("h1").inner_text()
)
```

### Difference

`inner_text()` generally returns user-visible text.

`text_content()` returns the element's text content, including text that may not be currently visible.

---

# 39. Playwright Attribute Extraction

```python
link = page.locator("a").first

print(
    link.get_attribute("href")
)
```

---

# 40. Playwright Waiting

Playwright provides automatic waiting for many actions and locator operations.

For example:

```python
page.get_by_role(
    "button",
    name="Submit"
).click()
```

Playwright can automatically wait for the button to become actionable.

Explicit waiting can also be used when needed:

```python
page.wait_for_selector(
    "#username"
)
```

### Best Practice

Avoid unnecessary:

```python
time.sleep()
```

Prefer Playwright's built-in waiting and locator-based actions.

---

# 41. Playwright Screenshot

```python
page.screenshot(
    path="screenshot.png"
)
```

### Full page screenshot

```python
page.screenshot(
    path="full.png",
    full_page=True
)
```

---

# 42. Playwright PDF

Chromium can generate PDFs.

```python
page.pdf(
    path="page.pdf"
)
```

PDF generation is mainly supported through Chromium, so use Chromium when PDF output is required.

---

# 43. Playwright Navigation

```python
page.goto(
    "https://example.com/page2"
)

page.go_back()

page.go_forward()

page.reload()
```

---

# 44. Playwright Multiple Pages

```python
page1 = browser.new_page()

page1.goto(
    "https://example.com"
)

page2 = browser.new_page()

page2.goto(
    "https://example.org"
)

page2.close()
```

A browser can contain multiple pages/tabs.

---

# 45. Playwright JavaScript Execution

You can execute JavaScript inside the page.

```python
result = page.evaluate(
    "() => document.title"
)

print(result)
```

Another example:

```python
page.evaluate(
    "() => alert('Hello')"
)
```

Use this carefully because many normal browser interactions can already be performed through locators.

---

# 46. Playwright Multiple Items

Suppose the page contains multiple products:

```python
items = page.locator(
    ".product"
)

count = items.count()

for i in range(count):

    item = items.nth(i)

    print(
        item.inner_text()
    )
```

This processes each matching element.

---

# 47. Playwright Login Automation

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=False
    )

    page = browser.new_page()

    page.goto(
        "https://example.com/login"
    )

    page.fill(
        "#username",
        "admin"
    )

    page.fill(
        "#password",
        "1234"
    )

    page.click(
        "#login"
    )

    print(
        page.title()
    )

    browser.close()
```

Again, do not store real credentials directly in source code.

---

# 48. Playwright Async Version

Playwright provides both **sync** and **async** APIs.

Example:

```python
import asyncio

from playwright.async_api import async_playwright


async def main():

    async with async_playwright() as p:

        browser = await p.chromium.launch(
            headless=True
        )

        page = await browser.new_page()

        await page.goto(
            "https://example.com"
        )

        print(
            await page.title()
        )

        await browser.close()


asyncio.run(main())
```

### Remember

Use either the synchronous API or asynchronous API according to your application design.

Do not randomly mix sync and async Playwright APIs.

---

# 49. Playwright Best Practices

1. Do not mix sync and async APIs unnecessarily
2. Prefer locators
3. Avoid unnecessary `sleep()`
4. Use proper waits
5. Close the browser
6. Add logging in production
7. Add error handling
8. Respect website rules and terms
9. Avoid excessive requests/actions
10. Do not hard-code credentials

---

# 50. Selenium vs Playwright

| Feature              | Selenium                         | Playwright                   |
| -------------------- | -------------------------------- | ---------------------------- |
| Browser automation   | Yes                              | Yes                          |
| Chromium             | Yes                              | Yes                          |
| Firefox              | Yes                              | Yes                          |
| WebKit               | No direct WebKit engine support  | Yes                          |
| Auto-waiting         | Available                        | Strong built-in auto-waiting |
| Sync API             | Yes                              | Yes                          |
| Async API            | Not the same model as Playwright | Yes                          |
| Testing              | Excellent                        | Excellent                    |
| Modern locator API   | Yes                              | Yes                          |
| Dynamic websites     | Yes                              | Yes                          |
| Screenshot           | Yes                              | Yes                          |
| PDF                  | Browser-dependent                | Chromium supports PDF        |
| Large-scale scraping | Usually not ideal                | Usually not ideal            |

### Important Rule

For a simple static website:

```text
requests + BeautifulSoup
```

may be much more lightweight.

For a dynamic JavaScript website:

```text
Playwright / Selenium
```

may be necessary.

---

# 51. Selenium vs Scrapy

| Feature              | Selenium       | Scrapy                 |
| -------------------- | -------------- | ---------------------- |
| Real browser         | Yes            | No                     |
| JavaScript rendering | Yes            | No by default          |
| Speed                | Usually slower | Fast for HTTP crawling |
| Large-scale crawling | Limited        | Excellent              |
| Web testing          | Excellent      | Not its main purpose   |
| Browser interaction  | Excellent      | No                     |
| Data crawling        | Yes            | Excellent              |

### Rule of Thumb

```text
Browser interaction
        ↓
Selenium / Playwright

Large-scale HTTP crawling
        ↓
Scrapy

Simple HTML scraping
        ↓
Requests + BeautifulSoup
```

---

# 52. Web Automation vs Web Scraping

## Web Automation

Web automation means automating browser actions.

Example:

```text
Open browser
     ↓
Login
     ↓
Click
     ↓
Fill form
     ↓
Submit
```

## Web Scraping

Web scraping means collecting data from websites.

Example:

```text
Website
   ↓
HTML
   ↓
Parse
   ↓
Product name
Price
Rating
   ↓
CSV
```

These two can also be used together.

---

# 53. Email Automation

Python's `smtplib` can be used to send email through an SMTP server.

Example:

```python
import smtplib

server = smtplib.SMTP(
    "smtp.example.com",
    587
)

server.starttls()

server.login(
    "your_email",
    "your_password"
)

server.sendmail(
    "your_email",
    "receiver@example.com",
    "Hello"
)

server.quit()
```

### Security

Never put real passwords directly in source code.

Better:

```text
Environment variable
        ↓
Password / API key
```

For production systems, use secure credential management where appropriate.

---

# 54. Excel Automation

Important libraries:

```text
pandas
openpyxl
```

## Pandas

Good for:

* Data analysis
* CSV
* Excel data processing
* Filtering
* Aggregation

## openpyxl

Good for:

* Reading XLSX
* Writing XLSX
* Cell formatting
* Worksheet operations

Example:

```python
import pandas as pd

df = pd.read_csv(
    "data.csv"
)

print(df.head())

print(
    df["salary"].sum()
)
```

---

# 55. Task Scheduling

The `schedule` library can run functions at specific times.

Install:

```bash
pip install schedule
```

Example:

```python
import schedule
import time


def job():

    print(
        "Automation running..."
    )


schedule.every().day.at(
    "08:00"
).do(job)


while True:

    schedule.run_pending()

    time.sleep(1)
```

### Linux

For production environments, Linux `cron` is another common scheduling option.

---

# 56. Desktop Automation

`pyautogui` can automate:

* Mouse movement
* Mouse clicks
* Keyboard typing
* Screenshots

Example:

```python
import pyautogui

pyautogui.write(
    "Hello World"
)

pyautogui.press(
    "enter"
)
```

---

# 57. File Change Detection

The `watchdog` library can monitor files and folders.

Example workflow:

```text
New file detected
       ↓
Process file
       ↓
Move file
       ↓
Rename file
       ↓
Backup
```

This is useful for automated file-processing systems.

---

# 58. PDF Automation

Useful libraries include:

### PyPDF2

Common PDF operations such as:

* Merge
* Split
* Basic PDF manipulation

### pdfplumber

Useful for:

* Text extraction
* Table extraction

### ReportLab

Useful for:

* Creating PDFs programmatically

---

# 59. Image Automation

**Pillow** is a popular Python image-processing library.

It can:

* Resize
* Crop
* Convert
* Compress
* Change image formats

Example:

```python
from PIL import Image

image = Image.open(
    "photo.jpg"
)

image = image.resize(
    (800, 600)
)

image.save(
    "output.jpg"
)
```

---

# 60. Database Automation

Common libraries:

```text
sqlite3
SQLAlchemy
mysql-connector-python
```

Automation workflow:

```text
Data
 ↓
Process
 ↓
Database
 ↓
Report
```

Possible tasks:

* Database backup
* Insert data
* Update data
* Generate reports
* Scheduled cleanup

---

# 61. API Automation

`requests` can be used to automate API calls.

Example:

```python
import requests

response = requests.get(
    "https://api.example.com/data",
    timeout=10
)

if response.ok:

    data = response.json()

    print(data)
```

When working with APIs, understand:

* Authentication
* Headers
* JSON
* Error handling
* Retry
* Rate limits
* Timeouts

---

# 62. Automation Error Handling

Error handling is very important in automation.

Example:

```python
import shutil

try:

    shutil.copy(
        "source.txt",
        "backup.txt"
    )

except FileNotFoundError:

    print(
        "Source file was not found"
    )

except PermissionError:

    print(
        "Permission denied"
    )

except Exception as e:

    print(
        f"Unexpected error: {e}"
    )
```

### Why?

Without error handling:

```text
Small error
    ↓
Entire automation stops
```

With proper handling:

```text
Error
 ↓
Handle it
 ↓
Log it
 ↓
Continue or fail safely
```

---

# 63. Automation Logging

In production automation, `logging` is usually better than only using `print()`.

Example:

```python
import logging

logging.basicConfig(
    level=logging.INFO
)

logging.info(
    "Automation started"
)

logging.error(
    "Something went wrong"
)
```

Logging helps you understand:

* When the task started
* What happened
* Where an error occurred
* How often failures occurred

---

# 64. Automation Project — Auto Backup

```python
import os
import shutil
from datetime import datetime


source = "important_files"

backup_root = "backups"

timestamp = datetime.now().strftime(
    "%Y%m%d_%H%M%S"
)

backup_path = os.path.join(
    backup_root,
    f"backup_{timestamp}"
)

os.makedirs(
    backup_root,
    exist_ok=True
)

shutil.copytree(
    source,
    backup_path
)

print(
    f"Backup created: {backup_path}"
)
```

Result:

```text
backups/
└── backup_20261003_103000/
    ├── file1
    ├── file2
    └── file3
```

### Improvement

For production use, consider:

* Checking whether the source exists
* Handling permission errors
* Logging
* Avoiding accidental overwrite
* Retaining only the required number of backups

---

# 65. Auto File Organizer Project

```python
import os
import shutil


SOURCE = "downloads"


FILE_TYPES = {

    "images": [
        ".jpg",
        ".jpeg",
        ".png",
        ".gif"
    ],

    "documents": [
        ".pdf",
        ".docx",
        ".txt"
    ],

    "videos": [
        ".mp4",
        ".mkv",
        ".avi"
    ],

    "archives": [
        ".zip",
        ".rar"
    ]
}


for filename in os.listdir(SOURCE):

    file_path = os.path.join(
        SOURCE,
        filename
    )

    if not os.path.isfile(
        file_path
    ):
        continue

    _, ext = os.path.splitext(
        filename
    )

    ext = ext.lower()

    for folder, extensions in FILE_TYPES.items():

        if ext in extensions:

            destination_folder = os.path.join(
                SOURCE,
                folder
            )

            os.makedirs(
                destination_folder,
                exist_ok=True
            )

            shutil.move(
                file_path,
                os.path.join(
                    destination_folder,
                    filename
                )
            )

            break


print(
    "Files organized successfully!"
)
```

### Workflow

```text
Downloads
    ↓
Check extension
    ↓
Find category
    ↓
Create category folder
    ↓
Move file
```

---

# 66. Automation Project Ideas

## Beginner

1. Auto File Renamer
2. File Organizer
3. Folder Backup
4. Duplicate File Finder
5. CSV Processor

## Intermediate

6. Excel Report Generator
7. Daily Email Reporter
8. Website Data Collector
9. API Data Downloader
10. Automatic PDF Generator

## Advanced

11. Price Tracker
12. Web Testing Framework
13. Dynamic Website Automation
14. Database Backup System
15. Django Automation System
16. Multi-step Workflow Automation
17. Scheduled Reporting System

---

# 67. Python Automation Architecture

A good automation project often follows this structure:

```text
Input
  ↓
Validation
  ↓
Processing
  ↓
Storage
  ↓
Output
  ↓
Logging
```

Example:

```text
CSV File
   ↓
Read
   ↓
Validate
   ↓
Process
   ↓
Database
   ↓
Generate Report
   ↓
Email
```

This structure makes automation systems easier to maintain.

---

# 68. Automation + Scheduling

Example automated reporting workflow:

```text
08:00 AM
   ↓
Script starts
   ↓
Collect data from API
   ↓
Process data
   ↓
Create Excel report
   ↓
Create PDF report
   ↓
Send email
   ↓
Save log
```

This can become a complete automated reporting system.

---

# 69. Automation + Django

As a Django developer, Python automation can be very useful.

Example:

```text
Django
   ↓
Management Command
   ↓
Automation Task
   ↓
Database
   ↓
Report
```

Possible tasks:

* Database backup
* Scheduled data processing
* Email notifications
* API synchronization
* Report generation
* Background jobs

### Django Management Commands

Django management commands are especially useful for repeatable server-side tasks.

Example structure:

```text
manage.py
   ↓
custom management command
   ↓
automation logic
```

---

# 70. Automation Security

Security is very important in automation.

Never do this:

```python
password = "123456"
```

Instead, use environment variables or a secure secrets system.

Example:

```python
import os

username = os.getenv(
    "USERNAME"
)

password = os.getenv(
    "PASSWORD"
)
```

Sensitive information includes:

* Password
* API key
* Access token
* Secret key
* Database credentials

### Important

Never commit secrets to GitHub or other source-control repositories.

---

# 71. Automation Best Practices

1. Use a virtual environment
2. Keep a dependency file such as `requirements.txt`
3. Use logging
4. Add error handling
5. Use timeouts for network operations
6. Use a proper retry strategy
7. Keep credentials secure
8. Consider `pathlib` for path handling
9. Avoid unnecessary `sleep()`
10. Use proper browser waits
11. Clean up resources
12. Be careful with backup overwrites
13. Respect website access rules
14. Follow website terms and applicable restrictions
15. Keep the automation scope controlled

---

# 72. Selenium / Playwright Resource Management

When a browser is opened, close it after the work is finished.

### Selenium

```python
driver.quit()
```

### Playwright

```python
browser.close()
```

This helps:

* Release memory
* Stop browser processes
* Release system resources
* Prevent orphaned browser processes

---

# 73. Important Selenium Rule

A common browser automation flow is:

```text
Element
   ↓
Wait
   ↓
Action
```

Example:

```text
Wait until element is available
        ↓
Find element
        ↓
Click
```

Avoid solving every timing issue with:

```python
time.sleep(10)
```

Instead, use explicit or condition-based waits.

---

# 74. Important Playwright Rule

Take advantage of Playwright's built-in auto-waiting and locators.

Prefer:

```python
page.get_by_role(...)
page.get_by_text(...)
page.locator(...)
```

Then perform actions:

```python
click()
fill()
check()
select_option()
```

This usually makes the automation code more readable and reliable.

---

# 75. Selenium / Playwright / Requests / BeautifulSoup

Suppose you need data from a website.

## Static HTML

Use:

```text
requests
+
BeautifulSoup
```

Flow:

```text
Website
   ↓
HTTP Request
   ↓
HTML
   ↓
BeautifulSoup
   ↓
Data
```

---

## Dynamic JavaScript Website

Use:

```text
Playwright
or
Selenium
```

when browser interaction or JavaScript rendering is actually required.

---

## Large-Scale Crawling

Use:

```text
Scrapy
```

---

## API Available

If the website provides an appropriate API, prefer:

```text
requests
or
httpx
```

### General Rule

```text
API
 ↓
requests / httpx

Static HTML
 ↓
requests + BeautifulSoup

Dynamic browser
 ↓
Playwright / Selenium

Large crawler
 ↓
Scrapy
```

---

# 76. Automation Library Cheat Sheet

## File

```text
os
shutil
pathlib
```

## Web

```text
requests
BeautifulSoup
Selenium
Playwright
Scrapy
```

## Data

```text
pandas
csv
```

## Excel

```text
openpyxl
xlsxwriter
```

## Email

```text
smtplib
imaplib
email
```

## GUI

```text
pyautogui
pynput
```

## PDF

```text
PyPDF2
pdfplumber
reportlab
```

## Image

```text
Pillow
OpenCV
```

## Database

```text
sqlite3
SQLAlchemy
```

## Scheduling

```text
schedule
datetime
time
cron
```

## File Monitoring

```text
watchdog
```

## Async

```text
asyncio
```

---

# 77. Six-Week Python Automation Learning Plan

## Week 1 — Python Basics

Learn:

* Variables
* Conditions
* Loops
* Functions
* Exceptions
* Files

---

## Week 2 — File Automation

Learn:

```text
os
shutil
pathlib
```

Projects:

* File Renamer
* File Organizer
* Backup System

---

## Week 3 — CSV + Excel

Learn:

```text
csv
pandas
openpyxl
```

Projects:

* Report Generator
* Excel Processor

---

## Week 4 — Web Automation

Learn:

```text
requests
BeautifulSoup
Selenium
Playwright
```

Projects:

* Login automation
* Form automation
* Data extraction

---

## Week 5 — Email + Scheduling

Learn:

```text
smtplib
schedule
datetime
```

Project:

```text
Daily Automated Report
```

---

## Week 6 — Advanced Automation

Learn:

* `asyncio`
* Threading
* APIs
* Databases
* Logging
* Error handling

---

# 78. Final Mental Model

The main idea of Python Automation is:

```text
Manual Task
     ↓
Identify repetitive work
     ↓
Write Python script
     ↓
Add validation
     ↓
Add error handling
     ↓
Add logging
     ↓
Schedule if necessary
     ↓
Run automatically
```

### File Automation

```text
os + shutil + pathlib
```

### Data Automation

```text
pandas + openpyxl
```

### Web Automation

```text
Selenium + Playwright
```

### Web Scraping

```text
requests + BeautifulSoup + Scrapy
```

### Email

```text
smtplib + email + imaplib
```

### Scheduling

```text
schedule + cron
```

### Desktop

```text
pyautogui + pynput
```

### Database

```text
sqlite3 + SQLAlchemy
```

### PDF

```text
pdfplumber + PyPDF2 + reportlab
```

### Image

```text
Pillow + OpenCV
```

---

# 79. Very Short Revision

## Automation

Making manual or repetitive tasks automatic using programs.

---

## `shutil`

High-level file and directory operations.

```text
copy
move
delete
copy folder
```

---

## `os`

Basic operating-system and file/folder operations.

---

## `pathlib`

Modern and convenient path handling.

---

## Selenium

Browser automation + web testing.

---

## Playwright

Modern browser automation + testing.

---

## Requests

HTTP requests and API communication.

---

## BeautifulSoup

HTML/XML parsing.

---

## Scrapy

Large-scale web crawling and scraping framework.

---

## Pandas

Data processing and analysis.

---

## openpyxl

Excel XLSX automation.

---

## PyAutoGUI

Mouse and keyboard automation.

---

## smtplib

Sending email through SMTP.

---

## schedule

Time-based Python task scheduling.

---

## watchdog

File/folder change monitoring.

---

## SQLAlchemy

Database access and ORM/database abstraction.

---

# 80. Important Interview Questions

## Q1. What is Python Automation?

**Answer:**

Python Automation means using Python programs to perform repetitive or manual tasks automatically.

---

## Q2. What is `shutil`?

**Answer:**

`shutil` is a Python standard-library module used for high-level file and directory operations.

---

## Q3. What does `shutil.copy()` do?

**Answer:**

It copies a file from one location to another.

---

## Q4. What does `shutil.move()` do?

**Answer:**

It moves a file or directory to another location.

---

## Q5. What does `shutil.rmtree()` do?

**Answer:**

It recursively deletes a directory and all of its contents.

---

## Q6. What is Selenium?

**Answer:**

Selenium is a framework for browser automation and web application testing.

---

## Q7. What is Playwright?

**Answer:**

Playwright is a modern browser automation and testing framework.

---

## Q8. What is the main purpose of Selenium and Playwright?

**Answer:**

They are used to automate and test web applications through browsers.

---

## Q9. What is the difference between Requests and Selenium?

**Answer:**

### Requests

Sends HTTP requests directly.

```text
Python
 ↓
HTTP Request
 ↓
Server
 ↓
Response
```

### Selenium

Controls a real browser.

```text
Python
 ↓
Browser
 ↓
Website
```

---

## Q10. What is BeautifulSoup?

**Answer:**

BeautifulSoup is a Python library used to parse HTML and XML documents and extract information from them.

---

## Q11. What is Scrapy?

**Answer:**

Scrapy is a Python framework designed for web crawling and scraping, especially for larger projects.

---

## Q12. What is a headless browser?

**Answer:**

A headless browser runs browser operations without showing the normal graphical browser window.

---

## Q13. What is Explicit Wait?

**Answer:**

Explicit Wait means waiting until a specific condition becomes true before continuing.

Example:

```text
Wait for element
     ↓
Element becomes available
     ↓
Perform action
```

---

## Q14. Why is logging important in automation?

**Answer:**

Logging helps track:

* Execution
* Errors
* Failures
* Important events
* Timing information

---

## Q15. Why use environment variables?

**Answer:**

Environment variables help keep sensitive information such as passwords, API keys, and tokens outside the source code.

---

# 81. Final Conclusion

The main goal of Python Automation is:

> **Do a repetitive task once in Python, then let the computer perform it automatically.**

The overall learning path is:

```text
Python
   ↓
os / shutil / pathlib
   ↓
pandas / openpyxl
   ↓
requests / BeautifulSoup
   ↓
Selenium / Playwright
   ↓
Email / Scheduling
   ↓
Database / API
   ↓
Logging / Error Handling
   ↓
Production Automation
```

## Most Important Learning Order

```text
Beginner
   ↓
File Automation
   ↓
Excel / CSV Automation
   ↓
Web Automation
   ↓
Email + Scheduling
   ↓
API + Database
   ↓
Async + Advanced Concepts
   ↓
Real Automation Projects
```

## One-Line Formula

```text
Python Automation
=
Repetitive Task
+
Python Script
+
Validation
+
Error Handling
+
Logging
+
Scheduling
=
Automatic Workflow
```

## Final Rule for Choosing Tools

```text
Need file operations?
        ↓
os + shutil + pathlib

Need data processing?
        ↓
pandas + openpyxl

Need API?
        ↓
requests / httpx

Need static HTML scraping?
        ↓
requests + BeautifulSoup

Need browser interaction?
        ↓
Selenium / Playwright

Need large-scale crawling?
        ↓
Scrapy

Need email?
        ↓
smtplib / email / imaplib

Need scheduling?
        ↓
schedule / cron

Need desktop control?
        ↓
pyautogui / pynput

Need database automation?
        ↓
sqlite3 / SQLAlchemy
```

**The best automation is not simply the one that works once. It should be reliable, secure, maintainable, observable, and safe to run repeatedly.**

"""
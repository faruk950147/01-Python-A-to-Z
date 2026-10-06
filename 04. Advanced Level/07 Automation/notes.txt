"""
# ============================================================
# PYTHON AUTOMATION + SHUTIL + SELENIUM + PLAYWRIGHT
# FULL NOTES — BANGLA
# ============================================================


# ============================================================
# 1. PYTHON AUTOMATION কী?
# ============================================================

Python Automation মানে হলো Python ব্যবহার করে repetitive
বা manual কাজগুলো automatically program/script-এর মাধ্যমে
করানো।

সহজভাবে:

মানুষ যে কাজ বারবার হাতে করে
        ↓
Python script তৈরি করি
        ↓
কম্পিউটার নিজে কাজটি করে

উদাহরণ:

- File rename
- File copy/move
- Folder organize
- Backup তৈরি
- Excel report তৈরি
- CSV process
- Web scraping
- Browser automation
- Form fill-up
- Email পাঠানো
- PDF তৈরি
- Database backup
- API call
- Scheduled task


# ============================================================
# 2. PYTHON AUTOMATION-এর সুবিধা
# ============================================================

1. Time save করে
2. Repetitive কাজ কমায়
3. Human error কমাতে সাহায্য করে
4. Productivity বাড়ায়
5. Large amount of data process করা যায়
6. একই কাজ বারবার নির্ভুলভাবে করা যায়
7. Business process automate করা যায়
8. Developer productivity বাড়ায়


# ============================================================
# 3. PYTHON AUTOMATION-এর প্রধান ক্ষেত্র
# ============================================================

Python দিয়ে সাধারণত নিচের কাজগুলো automate করা যায়:

1. File & Folder Automation
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


# ============================================================
# 4. PYTHON AUTOMATION LIBRARIES
# ============================================================

| কাজ | Library | ব্যবহার |
|---|---|---|
| File operation | os | rename, delete, list |
| File operation | shutil | copy, move, delete |
| File path | pathlib | path management |
| Web automation | Selenium | browser control |
| Web automation | Playwright | modern browser automation |
| HTTP | requests | API/web request |
| Scraping | BeautifulSoup | HTML parsing |
| Scraping | Scrapy | large-scale scraping |
| Data | pandas | CSV/data processing |
| Excel | openpyxl | XLSX read/write |
| GUI | pyautogui | mouse/keyboard |
| Email | smtplib | email send |
| Email | imaplib | email read |
| Scheduling | schedule | scheduled task |
| File monitoring | watchdog | file change detection |
| PDF | reportlab | PDF generation |
| PDF | pdfplumber | PDF extraction |
| Image | Pillow | image processing |
| Database | sqlite3 | SQLite |
| Database | SQLAlchemy | database abstraction |
| Async | asyncio | asynchronous programming |


# ============================================================
# 5. AUTOMATION ROADMAP
# ============================================================

LEVEL 1
-------
Python Basics

শিখতে হবে:

- Variable
- Data Types
- List
- Tuple
- Set
- Dictionary
- if/else
- for loop
- while loop
- Function
- Module
- Package
- Exception Handling
- File Handling
- Virtual Environment


LEVEL 2
-------
File & Folder Automation

Libraries:

- os
- shutil
- pathlib

Practice:

- Rename files
- Copy files
- Move files
- Delete files
- Create folders
- Backup system
- File organizer


LEVEL 3
-------
Excel / CSV Automation

Libraries:

- pandas
- openpyxl
- csv

Practice:

- CSV read
- CSV write
- Excel read
- Excel write
- Data filtering
- Report generation
- Excel merge


LEVEL 4
-------
Web Automation

Libraries:

- Selenium
- Playwright
- requests

Practice:

- Website open
- Login
- Form fill
- Button click
- Data extraction
- Screenshot
- PDF generation


LEVEL 5
-------
Web Scraping

Libraries:

- requests
- BeautifulSoup
- Scrapy
- Playwright

Practice:

- Product scraping
- News scraping
- Table scraping
- Pagination
- Dynamic website scraping


LEVEL 6
-------
Email Automation

Libraries:

- smtplib
- email
- imaplib

Practice:

- Send email
- Read email
- Daily report email
- Attachment send


LEVEL 7
-------
Task Scheduling

Libraries:

- schedule
- datetime
- time
- cron (Linux)

Practice:

- Daily report
- Periodic API request
- Automatic backup
- Scheduled scraping


LEVEL 8
-------
Desktop Automation

Libraries:

- pyautogui
- pynput

Practice:

- Mouse click
- Keyboard typing
- Screenshot
- Desktop application control


LEVEL 9
-------
Advanced Automation

শিখতে হবে:

- asyncio
- threading
- multiprocessing
- API automation
- Database automation
- Logging
- Retry system
- Configuration
- Deployment


LEVEL 10
--------
Real Projects

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


# ============================================================
# 6. SHUTIL LIBRARY
# ============================================================

shutil = Shell Utilities

এটি Python-এর standard library।

মূলত file এবং folder-এর high-level operation করার জন্য
shutil ব্যবহার করা হয়।

প্রধান কাজ:

- Copy
- Move
- Delete
- Folder copy
- Directory tree operations


# ============================================================
# 7. SHUTIL-এর গুরুত্বপূর্ণ METHODS
# ============================================================

shutil.copy(src, dst)

একটি file copy করে।

Example:

import shutil

shutil.copy(
    "source.txt",
    "destination.txt"
)


------------------------------------------------------------

shutil.copy2(src, dst)

File copy করার পাশাপাশি metadata-ও preserve করার চেষ্টা করে।

Example:

shutil.copy2(
    "source.txt",
    "backup.txt"
)


------------------------------------------------------------

shutil.copytree(src, dst)

পুরো folder এবং তার ভিতরের file/folder copy করে।

Example:

shutil.copytree(
    "my_folder",
    "backup_folder"
)


------------------------------------------------------------

shutil.move(src, dst)

File অথবা folder move করে।

Example:

shutil.move(
    "file.txt",
    "new_folder/file.txt"
)


------------------------------------------------------------

shutil.rmtree(path)

পুরো directory এবং ভিতরের contents delete করে।

Example:

shutil.rmtree("old_folder")


WARNING:

rmtree() খুব carefully ব্যবহার করতে হবে।

কারণ এটি recursiveভাবে folder-এর contents delete করে।


# ============================================================
# 8. OS + SHUTIL
# ============================================================

os:

- path তৈরি
- directory list
- file existence check
- rename
- basic OS operations

shutil:

- copy
- move
- folder copy
- recursive folder delete


Example:

import os
import shutil

source = "source.txt"
destination = "backup.txt"

if os.path.exists(source):
    shutil.copy(source, destination)

print("Backup completed")


# ============================================================
# 9. PATHLIB
# ============================================================

Modern Python code-এ pathlib ব্যবহার করা খুব সুবিধাজনক।

Example:

from pathlib import Path

base = Path("files")

for file in base.iterdir():
    print(file)


File check:

path = Path("test.txt")

if path.exists():
    print("File exists")


Folder create:

Path("backup").mkdir(exist_ok=True)


# ============================================================
# 10. FILE AUTOMATION PROJECT
# ============================================================

Example:

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


কাজ:

files/
    ↓
rename
    ↓
backup/

Example:

file1.txt → file_1.txt
file2.txt → file_2.txt
file3.txt → file_3.txt


IMPORTANT:

উপরের example ধরে নেয় source folder-এর সব item file
এবং সব file .txt হিসেবে rename করা যাবে।

বাস্তব project-এ extension preserve করা ভালো।


# ============================================================
# 11. EXTENSION PRESERVE করে RENAME
# ============================================================

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


# ============================================================
# 12. SAFE FILE COPY
# ============================================================

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


# ============================================================
# 13. AUTOMATION-এ FILE ORGANIZER
# ============================================================

একটি folder-এর file extension দেখে আলাদা folder-এ
move করা যায়।

Example:

Downloads/

photo.jpg
photo.png
document.pdf
data.csv
movie.mp4

Automation:

Downloads/
    images/
        photo.jpg
        photo.png

    documents/
        document.pdf

    csv/
        data.csv

    videos/
        movie.mp4


# ============================================================
# 14. SELENIUM কী?
# ============================================================

Selenium হলো browser automation এবং web testing-এর জন্য
একটি জনপ্রিয় open-source framework।

Selenium দিয়ে browser control করা যায়।

যেমন:

- Website open
- Button click
- Form fill
- Login
- Page navigation
- Screenshot
- Testing
- কিছু ক্ষেত্রে data extraction


# ============================================================
# 15. SELENIUM-এর USE CASE
# ============================================================

1. Web testing
2. UI testing
3. Login automation
4. Form automation
5. Browser automation
6. Dynamic website interaction
7. Repetitive browser tasks


# ============================================================
# 16. SELENIUM COMPONENTS
# ============================================================

1. Selenium WebDriver

Browser control করার সবচেয়ে গুরুত্বপূর্ণ component।

2. Selenium IDE

Record & playback based testing tool।

3. Selenium Grid

Multiple machine/browser environment-এ test চালাতে সাহায্য করে।

4. Selenium RC

পুরোনো technology।

বর্তমানে সাধারণ Selenium development-এ ব্যবহার করা হয় না।


# ============================================================
# 17. SELENIUM SUPPORTED LANGUAGES
# ============================================================

- Python
- Java
- C#
- JavaScript
- Ruby


# ============================================================
# 18. SELENIUM INSTALLATION
# ============================================================

Install:

pip install selenium


Modern Selenium সাধারণত Selenium Manager-এর মাধ্যমে
browser driver management সহজ করে।

Basic code:

from selenium import webdriver

driver = webdriver.Chrome()

driver.get(
    "https://example.com"
)

print(driver.title)

driver.quit()


# ============================================================
# 19. SELENIUM ELEMENT FIND
# ============================================================

ID:

driver.find_element(
    "id",
    "email"
)


Name:

driver.find_element(
    "name",
    "password"
)


XPath:

driver.find_element(
    "xpath",
    "//input[@type='text']"
)


CSS Selector:

driver.find_element(
    "css selector",
    ".class_name"
)


Modern recommended style:

from selenium.webdriver.common.by import By

element = driver.find_element(
    By.ID,
    "email"
)


# ============================================================
# 20. SELENIUM ACTIONS
# ============================================================

Click:

element.click()


Input:

element.send_keys(
    "Hello"
)


Clear:

element.clear()


Get text:

print(element.text)


Attribute:

print(
    element.get_attribute("href")
)


# ============================================================
# 21. SELENIUM WAIT
# ============================================================

Web automation-এ সবচেয়ে important বিষয়গুলোর একটি হলো
waiting।

কারণ webpage load হতে সময় লাগতে পারে।


------------------------------------------------------------
Implicit Wait
------------------------------------------------------------

driver.implicitly_wait(10)


এতে Selenium element search করার সময় অপেক্ষা করতে পারে।


------------------------------------------------------------
Explicit Wait
------------------------------------------------------------

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


Explicit wait নির্দিষ্ট condition-এর জন্য অপেক্ষা করে।


# ============================================================
# 22. SELENIUM HEADLESS MODE
# ============================================================

Browser screen না দেখিয়ে background-এ browser চালানোকে
Headless mode বলা হয়।

Example:

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()

options.add_argument(
    "--headless"
)

driver = webdriver.Chrome(
    options=options
)

driver.get(
    "https://example.com"
)

print(driver.title)

driver.quit()


# ============================================================
# 23. SELENIUM SCREENSHOT
# ============================================================

driver.save_screenshot(
    "page.png"
)


# ============================================================
# 24. SELENIUM NAVIGATION
# ============================================================

driver.get(
    "https://example.com"
)

driver.back()

driver.forward()

driver.refresh()


# ============================================================
# 25. SELENIUM MULTIPLE TABS
# ============================================================

window_handles = driver.window_handles

driver.switch_to.window(
    window_handles[1]
)


# ============================================================
# 26. SELENIUM COOKIES
# ============================================================

Get cookies:

cookies = driver.get_cookies()

print(cookies)


Add cookie:

driver.add_cookie({
    "name": "test",
    "value": "123"
})


# ============================================================
# 27. SELENIUM LOGIN AUTOMATION
# ============================================================

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


# ============================================================
# 28. SELENIUM ADVANTAGES
# ============================================================

- Real browser control
- JavaScript website handle করতে পারে
- Testing-এর জন্য জনপ্রিয়
- Multiple browser support
- Large ecosystem


# ============================================================
# 29. SELENIUM DISADVANTAGES
# ============================================================

- Browser চালাতে হয়
- Resource বেশি লাগে
- সাধারণ HTTP request-এর তুলনায় ধীর
- Large-scale scraping-এর জন্য inefficient হতে পারে


# ============================================================
# 30. PLAYWRIGHT কী?
# ============================================================

Playwright হলো modern browser automation এবং testing
framework।

Python-এ Playwright ব্যবহার করে:

- Browser automation
- Web testing
- Dynamic website interaction
- Data extraction
- Screenshot
- PDF generation


# ============================================================
# 31. PLAYWRIGHT SUPPORT
# ============================================================

Playwright প্রধানত:

- Chromium
- Firefox
- WebKit

support করে।

Chromium browser family-এর মধ্যে Chrome/Edge-এর জন্য
ব্যবহার করা যায়।

WebKit Safari-এর browser engine।


# ============================================================
# 32. PLAYWRIGHT INSTALLATION
# ============================================================

pip install playwright

তারপর:

playwright install


# ============================================================
# 33. PLAYWRIGHT BASIC SETUP
# ============================================================

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


# ============================================================
# 34. PLAYWRIGHT BROWSER TYPES
# ============================================================

Chromium:

p.chromium.launch()


Firefox:

p.firefox.launch()


WebKit:

p.webkit.launch()


# ============================================================
# 35. PLAYWRIGHT HEADLESS
# ============================================================

Headless:

browser = p.chromium.launch(
    headless=True
)


Headful:

browser = p.chromium.launch(
    headless=False
)


Development-এর সময় headless=False ব্যবহার করলে
browser-এর action দেখা যায়।

Production automation-এ প্রয়োজন অনুযায়ী headless=True
ব্যবহার করা যায়।


# ============================================================
# 36. PLAYWRIGHT SELECTORS
# ============================================================

CSS:

page.locator(
    "button"
)


ID:

page.locator(
    "#username"
)


Class:

page.locator(
    ".product"
)


Text:

page.get_by_text(
    "Submit"
)


Role-based:

page.get_by_role(
    "button",
    name="Submit"
)


Playwright-এর modern locator API ব্যবহার করা সাধারণত
ভালো practice।


# ============================================================
# 37. PLAYWRIGHT ACTIONS
# ============================================================

Fill:

page.fill(
    "#username",
    "admin"
)


Click:

page.click(
    "#login"
)


Hover:

page.hover(
    "#menu"
)


Check:

page.check(
    "#checkbox"
)


Select:

page.select_option(
    "#dropdown",
    "Bangladesh"
)


# ============================================================
# 38. PLAYWRIGHT TEXT EXTRACTION
# ============================================================

element = page.locator(
    "h1"
)

print(
    element.text_content()
)


Modern locator:

print(
    page.locator("h1").inner_text()
)


# ============================================================
# 39. PLAYWRIGHT ATTRIBUTE EXTRACTION
# ============================================================

link = page.locator(
    "a"
).first

print(
    link.get_attribute("href")
)


# ============================================================
# 40. PLAYWRIGHT WAIT
# ============================================================

Playwright action-এর আগে অনেক ক্ষেত্রে automatically
element-এর প্রয়োজনীয় state-এর জন্য wait করে।

এটি automation-কে robust করতে সাহায্য করে।

Explicit wait প্রয়োজন হলে:

page.wait_for_selector(
    "#username"
)


তবে unnecessary sleep() ব্যবহার না করাই ভালো।


# ============================================================
# 41. PLAYWRIGHT SCREENSHOT
# ============================================================

page.screenshot(
    path="screenshot.png"
)


Full page:

page.screenshot(
    path="full.png",
    full_page=True
)


# ============================================================
# 42. PLAYWRIGHT PDF
# ============================================================

Chromium-based browser-এ:

page.pdf(
    path="page.pdf"
)


Note:

PDF generation-এর ক্ষেত্রে browser/context এবং rendering
requirements অনুযায়ী Chromium ব্যবহার করা সুবিধাজনক।


# ============================================================
# 43. PLAYWRIGHT NAVIGATION
# ============================================================

page.goto(
    "https://example.com/page2"
)

page.go_back()

page.go_forward()

page.reload()


# ============================================================
# 44. PLAYWRIGHT MULTIPLE PAGES
# ============================================================

page1 = browser.new_page()

page1.goto(
    "https://example.com"
)


page2 = browser.new_page()

page2.goto(
    "https://example.org"
)


page2.close()


# ============================================================
# 45. PLAYWRIGHT JAVASCRIPT EXECUTION
# ============================================================

result = page.evaluate(
    "() => document.title"
)

print(result)


Example:

page.evaluate(
    "() => alert('Hello')"
)


# ============================================================
# 46. PLAYWRIGHT MULTIPLE ITEMS
# ============================================================

items = page.locator(
    ".product"
)

count = items.count()

for i in range(count):

    item = items.nth(i)

    print(
        item.inner_text()
    )


# ============================================================
# 47. PLAYWRIGHT LOGIN AUTOMATION
# ============================================================

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


# ============================================================
# 48. PLAYWRIGHT ASYNC VERSION
# ============================================================

Playwright-এর sync এবং async দুই ধরনের API আছে।

Async example:

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


# ============================================================
# 49. PLAYWRIGHT BEST PRACTICES
# ============================================================

1. Sync এবং async API একসাথে mix না করা
2. Locator ব্যবহার করা
3. Unnecessary sleep() avoid করা
4. Proper wait ব্যবহার করা
5. Browser close করা
6. Production-এ logging রাখা
7. Error handling রাখা
8. Website-এর terms/rules respect করা
9. Excessive request না পাঠানো
10. Credentials source code-এ hard-code না করা


# ============================================================
# 50. SELENIUM VS PLAYWRIGHT
# ============================================================

| Feature | Selenium | Playwright |
|---|---|---|
| Browser automation | Yes | Yes |
| Chromium | Yes | Yes |
| Firefox | Yes | Yes |
| WebKit | No direct WebKit engine support | Yes |
| Auto-waiting | Available | Strong built-in auto-waiting |
| Sync API | Yes | Yes |
| Async API | Different model | Yes |
| Testing | Excellent | Excellent |
| Modern locator API | Yes | Yes |
| Dynamic website | Yes | Yes |
| Screenshot | Yes | Yes |
| PDF | Browser dependent | Chromium supports PDF |
| Large-scale scraping | Usually not ideal | Usually not ideal |


Important:

Selenium বা Playwright browser চালায়।

তাই সাধারণ static website-এর জন্য requests + BeautifulSoup
অনেক সময় বেশি lightweight।

Dynamic JavaScript website-এর জন্য browser automation
প্রয়োজন হতে পারে।


# ============================================================
# 51. SELENIUM VS SCRAPY
# ============================================================

| Feature | Selenium | Scrapy |
|---|---|---|
| Browser | Yes | No |
| JavaScript rendering | Yes | No by default |
| Speed | তুলনামূলক ধীর | Fast |
| Large-scale crawling | সীমিত | Excellent |
| Web testing | Excellent | No |
| Browser interaction | Excellent | No |
| Data crawling | Yes | Excellent |


Rule of thumb:

Browser interaction দরকার
        ↓
Selenium / Playwright

Large-scale HTTP crawling দরকার
        ↓
Scrapy

Simple HTML scraping
        ↓
requests + BeautifulSoup


# ============================================================
# 52. WEB AUTOMATION vs WEB SCRAPING
# ============================================================

Web Automation:

Browser-এর action automate করা।

Example:

Open browser
↓
Login
↓
Click
↓
Form fill
↓
Submit


Web Scraping:

Website থেকে data collect করা।

Example:

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


দুইটি একসাথেও ব্যবহার করা যায়।


# ============================================================
# 53. EMAIL AUTOMATION
# ============================================================

Email পাঠানোর জন্য:

smtplib

Example:

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


Production project-এ password source code-এ রাখা উচিত নয়।

Environment variable ব্যবহার করা ভালো।


# ============================================================
# 54. EXCEL AUTOMATION
# ============================================================

Libraries:

pandas
openpyxl


pandas:

- Data analysis
- CSV
- Excel
- Filtering
- Aggregation


openpyxl:

- XLSX read
- XLSX write
- Cell formatting
- Worksheet operation


Example:

import pandas as pd

df = pd.read_csv(
    "data.csv"
)

print(df.head())

print(
    df["salary"].sum()
)


# ============================================================
# 55. TASK SCHEDULING
# ============================================================

schedule library ব্যবহার করে নির্দিষ্ট সময় অনুযায়ী
function চালানো যায়।

Install:

pip install schedule


Example:

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


Linux production environment-এ cron-ও ব্যবহার করা যায়।


# ============================================================
# 56. DESKTOP AUTOMATION
# ============================================================

pyautogui:

- Mouse move
- Mouse click
- Keyboard typing
- Screenshot


Example:

import pyautogui

pyautogui.write(
    "Hello World"
)

pyautogui.press(
    "enter"
)


# ============================================================
# 57. FILE CHANGE DETECTION
# ============================================================

watchdog library দিয়ে file/folder change detect করা যায়।

Possible use:

একটি folder monitor করা।

নতুন file এলে:

New file detected
        ↓
Process
        ↓
Move
        ↓
Rename
        ↓
Backup


# ============================================================
# 58. PDF AUTOMATION
# ============================================================

Useful libraries:

PyPDF2
pdfplumber
reportlab


PyPDF2:

- Merge
- Split
- Read/write basic PDF operations


pdfplumber:

- Text extraction
- Table extraction


reportlab:

- Programmatically PDF তৈরি


# ============================================================
# 59. IMAGE AUTOMATION
# ============================================================

Pillow:

- Resize
- Crop
- Convert
- Compress
- Format change


Example:

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


# ============================================================
# 60. DATABASE AUTOMATION
# ============================================================

Libraries:

sqlite3
SQLAlchemy
mysql-connector-python


Automation example:

Data
 ↓
Process
 ↓
Database
 ↓
Report


Possible কাজ:

- Backup
- Insert data
- Update data
- Generate report
- Scheduled database cleanup


# ============================================================
# 61. API AUTOMATION
# ============================================================

requests দিয়ে API automate করা যায়।

Example:

import requests

response = requests.get(
    "https://api.example.com/data",
    timeout=10
)

if response.ok:

    data = response.json()

    print(data)


API automation-এর ক্ষেত্রে:

- Authentication
- Headers
- JSON
- Error handling
- Retry
- Rate limit

বোঝা গুরুত্বপূর্ণ।


# ============================================================
# 62. AUTOMATION ERROR HANDLING
# ============================================================

Automation script-এ error handling খুব গুরুত্বপূর্ণ।

Example:

import shutil

try:

    shutil.copy(
        "source.txt",
        "backup.txt"
    )

except FileNotFoundError:

    print(
        "Source file পাওয়া যায়নি"
    )

except PermissionError:

    print(
        "Permission denied"
    )

except Exception as e:

    print(
        f"Unexpected error: {e}"
    )


# ============================================================
# 63. AUTOMATION LOGGING
# ============================================================

Production automation-এ print() এর পরিবর্তে logging
ব্যবহার করা ভালো।

Example:

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


Log দিয়ে পরে বোঝা যায়:

- কখন কাজ শুরু হয়েছে
- কোন কাজ হয়েছে
- কোথায় error হয়েছে
- কতবার failure হয়েছে


# ============================================================
# 64. AUTOMATION PROJECT — AUTO BACKUP
# ============================================================

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


Result:

backups/
    backup_20261003_103000/
        file1
        file2
        file3


# ============================================================
# 65. AUTO FILE ORGANIZER PROJECT
# ============================================================

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


# ============================================================
# 66. AUTOMATION PROJECT IDEAS
# ============================================================

BEGINNER:

1. Auto File Renamer
2. File Organizer
3. Folder Backup
4. Duplicate File Finder
5. CSV Processor


INTERMEDIATE:

6. Excel Report Generator
7. Daily Email Reporter
8. Website Data Collector
9. API Data Downloader
10. Automatic PDF Generator


ADVANCED:

11. Price Tracker
12. Web Testing Framework
13. Dynamic Website Automation
14. Database Backup System
15. Django Automation System
16. Multi-step workflow automation
17. Scheduled reporting system


# ============================================================
# 67. PYTHON AUTOMATION ARCHITECTURE
# ============================================================

একটি ভালো automation project সাধারণত:

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


Example:

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


# ============================================================
# 68. AUTOMATION + SCHEDULING
# ============================================================

Example workflow:

08:00 AM
   ↓
Script start
   ↓
API থেকে data collect
   ↓
Data process
   ↓
Excel report
   ↓
PDF report
   ↓
Email send
   ↓
Log save


এটি সম্পূর্ণ automated reporting system হতে পারে।


# ============================================================
# 69. AUTOMATION + DJANGO
# ============================================================

Django developer হিসেবে Python Automation-এর অনেক use case
আছে।

Example:

Django
   ↓
Management Command
   ↓
Automation Task
   ↓
Database
   ↓
Report


Possible tasks:

- Database backup
- Scheduled data processing
- Email notification
- API synchronization
- Report generation
- Background jobs


Django management command automation-এর জন্য খুব useful।


# ============================================================
# 70. AUTOMATION SECURITY
# ============================================================

Automation script-এ security গুরুত্বপূর্ণ।

কখনো source code-এ সরাসরি:

password = "123456"

এভাবে credential রাখা উচিত নয়।


এর পরিবর্তে:

Environment Variables

ব্যবহার করা ভালো।

Example:

import os

username = os.getenv(
    "USERNAME"
)

password = os.getenv(
    "PASSWORD"
)


Sensitive data:

- Password
- API key
- Token
- Secret key

GitHub-এ commit করা যাবে না।


# ============================================================
# 71. AUTOMATION BEST PRACTICES
# ============================================================

1. Virtual environment ব্যবহার করো
2. requirements.txt রাখো
3. Logging ব্যবহার করো
4. Error handling রাখো
5. Timeout ব্যবহার করো
6. Retry strategy রাখো
7. Credentials secure রাখো
8. File path-এর জন্য pathlib consider করো
9. Production-এ unnecessary sleep avoid করো
10. Browser automation-এ proper waits ব্যবহার করো
11. Resource cleanup করো
12. Backup automation-এ overwrite carefully করো
13. User-Agent/website rules respect করো
14. Website terms এবং applicable restrictions মেনে চলো
15. Automation-এর scope সীমিত রাখো


# ============================================================
# 72. SELENIUM / PLAYWRIGHT RESOURCE MANAGEMENT
# ============================================================

Browser open করলে শেষে close করতে হবে।

Selenium:

driver.quit()


Playwright:

browser.close()


এতে:

- Memory leak কমে
- Browser process বন্ধ হয়
- Resource release হয়


# ============================================================
# 73. SELENIUM-এর জন্য IMPORTANT RULE
# ============================================================

Browser automation-এ:

Element
   ↓
Wait
   ↓
Action


Example:

Wait until element exists
        ↓
Find element
        ↓
Click


শুধু:

time.sleep(10)

ব্যবহার করে সব problem solve করার চেষ্টা করা উচিত নয়।


# ============================================================
# 74. PLAYWRIGHT-এর জন্য IMPORTANT RULE
# ============================================================

Playwright-এর auto-waiting সুবিধা ব্যবহার করো।

Prefer:

page.get_by_role(...)
page.get_by_text(...)
page.locator(...)


এরপর action:

click()
fill()
check()
select_option()


এতে automation code সাধারণত বেশি readable হয়।


# ============================================================
# 75. SELENIUM / PLAYWRIGHT / REQUESTS / BS4
# ============================================================

Problem:

"আমার website থেকে data দরকার। কোনটা ব্যবহার করব?"


------------------------------------------------------------
Static HTML
------------------------------------------------------------

requests
+
BeautifulSoup


------------------------------------------------------------
Dynamic JavaScript website
------------------------------------------------------------

Playwright
অথবা
Selenium


------------------------------------------------------------
Large-scale crawling
------------------------------------------------------------

Scrapy


------------------------------------------------------------
API available
------------------------------------------------------------

requests
অথবা
httpx


সাধারণ rule:

API
 ↓
requests/httpx

Static HTML
 ↓
requests + BeautifulSoup

Dynamic browser
 ↓
Playwright/Selenium

Large crawler
 ↓
Scrapy


# ============================================================
# 76. AUTOMATION LIBRARY CHEAT SHEET
# ============================================================

File:
os
shutil
pathlib


Web:
requests
BeautifulSoup
Selenium
Playwright
Scrapy


Data:
pandas
csv


Excel:
openpyxl
xlsxwriter


Email:
smtplib
imaplib
email


GUI:
pyautogui
pynput


PDF:
PyPDF2
pdfplumber
reportlab


Image:
Pillow
OpenCV


Database:
sqlite3
SQLAlchemy


Scheduling:
schedule
datetime
time
cron


File monitoring:
watchdog


Async:
asyncio


# ============================================================
# 77. AUTOMATION LEARNING PLAN
# ============================================================

WEEK 1
-------

Python basics

- Variables
- Conditions
- Loops
- Functions
- Exceptions
- Files


WEEK 2
-------

File automation

- os
- shutil
- pathlib

Projects:

- Renamer
- Organizer
- Backup


WEEK 3
-------

CSV + Excel

- csv
- pandas
- openpyxl

Projects:

- Report generator
- Excel processor


WEEK 4
-------

Web automation

- requests
- BeautifulSoup
- Selenium
- Playwright


Projects:

- Login automation
- Form automation
- Data extraction


WEEK 5
-------

Email + scheduling

- smtplib
- schedule
- datetime


Project:

Daily automated report


WEEK 6
-------

Advanced automation

- asyncio
- threading
- APIs
- database
- logging
- error handling


# ============================================================
# 78. FINAL MENTAL MODEL
# ============================================================

Python Automation:

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


File Automation:

os + shutil + pathlib


Data Automation:

pandas + openpyxl


Web Automation:

Selenium + Playwright


Web Scraping:

requests + BeautifulSoup + Scrapy


Email:

smtplib + email + imaplib


Scheduling:

schedule + cron


Desktop:

pyautogui + pynput


Database:

sqlite3 + SQLAlchemy


PDF:

pdfplumber + PyPDF2 + reportlab


Image:

Pillow + OpenCV


# ============================================================
# 79. VERY SHORT REVISION
# ============================================================

Automation
-----------
Manual/repetitive কাজকে programmatically automatic করা।


shutil
-------
File/folder copy, move, delete করার জন্য high-level
standard library।


os
--
Operating system এবং file/folder basic operations।


pathlib
-------
Modern path handling।


Selenium
--------
Browser automation + testing।


Playwright
----------
Modern browser automation + testing।


requests
--------
HTTP request এবং API communication।


BeautifulSoup
-------------
HTML parsing।


Scrapy
------
Large-scale web crawling/scraping।


pandas
------
Data processing।


openpyxl
--------
Excel XLSX automation।


pyautogui
---------
Mouse + keyboard automation।


smtplib
-------
Email send।


schedule
--------
Time-based Python task scheduling।


watchdog
--------
File/folder change monitoring।


SQLAlchemy
----------
Database abstraction/ORM।


# ============================================================
# 80. IMPORTANT INTERVIEW QUESTIONS
# ============================================================

Q1. Python Automation কী?

Ans:
Python ব্যবহার করে repetitive/manual কাজ automatically
করাকে Python Automation বলে।


Q2. shutil কী?

Ans:
shutil Python standard library-এর একটি module, যা high-level
file এবং directory operations-এর জন্য ব্যবহৃত হয়।


Q3. shutil.copy() কী করে?

Ans:
একটি file copy করে।


Q4. shutil.move() কী করে?

Ans:
File বা directory move করে।


Q5. shutil.rmtree() কী করে?

Ans:
একটি directory এবং তার contents recursively delete করে।


Q6. Selenium কী?

Ans:
Browser automation এবং web testing framework।


Q7. Playwright কী?

Ans:
Modern browser automation/testing framework।


Q8. Selenium এবং Playwright-এর মূল উদ্দেশ্য কী?

Ans:
Browser-এর মাধ্যমে web application automate এবং test করা।


Q9. requests এবং Selenium-এর পার্থক্য কী?

Ans:

requests:
HTTP request পাঠায়।

Selenium:
Real browser control করে।


Q10. BeautifulSoup কী?

Ans:
HTML/XML parse করার library।


Q11. Scrapy কী?

Ans:
Large-scale web crawling এবং scraping framework।


Q12. Headless browser কী?

Ans:
Browser UI না দেখিয়ে background-এ browser চালানো।


Q13. Explicit Wait কী?

Ans:
নির্দিষ্ট condition পূরণ হওয়া পর্যন্ত অপেক্ষা করা।


Q14. Automation-এ logging কেন দরকার?

Ans:
Script-এর execution এবং error track করার জন্য।


Q15. Automation-এ environment variable কেন দরকার?

Ans:
Password, API key, token-এর মতো sensitive information
securely manage করার জন্য।


# ============================================================
# 81. FINAL CONCLUSION
# ============================================================

Python Automation শেখার মূল উদ্দেশ্য হলো:

"যে কাজ বারবার করতে হয়,
সেটা একবার Python-এ লিখে
কম্পিউটারকে দিয়ে করানো।"


Core Stack:

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


সবচেয়ে গুরুত্বপূর্ণ:

Beginner
    ↓
File Automation
    ↓
Excel Automation
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
"""
"""
# Web Crawling & Web Scraping with Python

# 1. What is Web Crawling?

**Web Crawling** is an automated process where a program visits web pages and follows links to discover other pages.

### Easy Definition

> **Crawling = Finding and visiting web pages.**

Example:

```text
Page A
  ↓
Page B
  ↓
Page C
  ↓
Page D
```

A crawler may work like this:

```text
Visit A
  ↓
Find B and C
  ↓
Visit B
  ↓
Find D
  ↓
Visit D
```

### Main jobs of a Web Crawler

* Collect URLs
* Discover new pages
* Follow links
* Understand website structure
* Discover pages for search engines
* Monitor websites
* Analyze websites

### Examples

* Googlebot
* Bingbot
* Custom Python crawler
* Scrapy Spider

---

# 2. What is Web Scraping?

**Web Scraping** is the process of automatically extracting specific data from a website.

### Easy Definition

> **Scraping = Extracting useful information from web pages.**

For example, from an e-commerce website we may collect:

```text
Product Name
Price
Rating
Image
Availability
```

### Uses of Web Scraping

* Product information
* Price monitoring
* News collection
* Job listings
* Research
* Data analysis
* Real-estate data
* Public data collection

---

# 3. Web Crawling vs Web Scraping

| Feature      | Web Crawling       | Web Scraping            |
| ------------ | ------------------ | ----------------------- |
| Main purpose | Discover pages     | Extract data            |
| Main focus   | URLs and structure | Page content            |
| Main action  | Follow links       | Select and extract data |
| Output       | URLs / pages       | Structured data         |
| Common use   | Indexing           | Research / analysis     |
| Example      | Googlebot          | Product scraper         |

### Easy way to remember

```text
Crawler = Where is it?

Scraper = What is inside it?
```

---

# 4. Crawling + Scraping

A real project can use both crawling and scraping.

```text
Crawler
   ↓
Find URLs
   ↓
Visit Pages
   ↓
Scraper
   ↓
Extract Data
   ↓
Clean Data
   ↓
Store Data
```

For example:

```text
Website
   ↓
Find product pages
   ↓
Visit product pages
   ↓
Extract name, price, rating
   ↓
Save to CSV/Database
```

---

# 5. Uses of Web Crawling

Web crawling can be used for:

* Search engine indexing
* Website structure analysis
* Link discovery
* SEO analysis
* Research
* Broken-link detection
* Website monitoring
* Content discovery

---

# 6. Uses of Web Scraping

Web scraping can be used for:

* Product information
* Price monitoring
* News data
* Job data
* Research data
* Real-estate data
* Public data collection
* Data analysis

Always follow the target site's terms, access rules, and applicable laws.

---

# 7. Python Web Crawling Libraries

Python has many useful libraries for crawling and scraping.

### Basic HTTP

```text
requests
```

### HTML Parsing

```text
BeautifulSoup
lxml
```

### Crawling Framework

```text
Scrapy
```

### Browser Automation

```text
Selenium
Playwright
```

### Async HTTP

```text
aiohttp
httpx
```

### Data Processing

```text
pandas
csv
json
```

### Helpers

```text
urllib
re
time
```

---

# 8. Which Library Should You Use?

| Task                  | Library                   |
| --------------------- | ------------------------- |
| HTTP request          | `requests`                |
| HTML parsing          | `BeautifulSoup`           |
| Fast HTML/XML parsing | `lxml`                    |
| Large-scale crawling  | `Scrapy`                  |
| JavaScript websites   | `Selenium` / `Playwright` |
| Async HTTP            | `aiohttp` / `httpx`       |
| Data analysis         | `pandas`                  |
| CSV files             | `csv`                     |
| JSON files            | `json`                    |

### Simple rule

```text
requests
→ Get web page

BeautifulSoup
→ Read HTML

urljoin
→ Build correct URLs

Scrapy
→ Large crawler

Selenium / Playwright
→ Control a real browser
```

---

# Part 1: Requests

# 9. Install Requests

```bash
pip install requests
```

Import:

```python
import requests
```

---

# 10. Basic GET Request

```python
import requests

url = "https://example.com"

response = requests.get(
    url,
    timeout=10
)

print(response.status_code)
```

Here:

```python
requests.get()
```

sends an HTTP GET request.

The result is stored in:

```python
response
```

---

# 11. Why Use Timeout?

Always use a timeout for network requests.

```python
response = requests.get(
    url,
    timeout=10
)
```

Without a suitable timeout, a request may wait for a very long time if the network or server does not respond.

### Easy Definition

> **Timeout limits how long your program waits for a request.**

---

# 12. HTTP Status Codes

Use:

```python
print(response.status_code)
```

Common status codes:

| Code  | Meaning               |
| ----- | --------------------- |
| `200` | OK                    |
| `301` | Permanent Redirect    |
| `302` | Temporary Redirect    |
| `400` | Bad Request           |
| `401` | Unauthorized          |
| `403` | Forbidden             |
| `404` | Not Found             |
| `429` | Too Many Requests     |
| `500` | Internal Server Error |
| `502` | Bad Gateway           |
| `503` | Service Unavailable   |

### Most important

```text
2xx → Success
3xx → Redirect
4xx → Client error
5xx → Server error
```

---

# 13. `raise_for_status()`

`raise_for_status()` raises an exception when the HTTP response indicates an error.

Example:

```python
import requests

url = "https://example.com"

try:
    response = requests.get(
        url,
        timeout=10
    )

    response.raise_for_status()

    print(response.text)

except requests.RequestException as e:
    print("Request failed:", e)
```

This makes error handling easier.

---

# 14. Response Text

Use:

```python
print(response.text)
```

`response.text` gives the response body as decoded text.

For an HTML page, it usually contains the HTML source.

---

# 15. Response Content

Use:

```python
print(response.content)
```

`response.content` returns the response body as **bytes**.

This can be useful when working with binary data.

---

# 16. Response Headers

Print all headers:

```python
print(response.headers)
```

Get one header:

```python
print(
    response.headers.get("Content-Type")
)
```

Print all headers:

```python
for key, value in response.headers.items():
    print(
        f"{key} <-------> {value}"
    )
```

---

# 17. Response URL

```python
print(response.url)
```

This shows the final URL associated with the response.

This can be useful when redirects are involved.

---

# 18. Response History

```python
print(response.history)
```

This shows previous redirect responses.

For example:

```text
URL A
 ↓
301 Redirect
 ↓
URL B
 ↓
200 OK
```

`response.history` can help inspect the redirect chain.

---

# 19. Response Time

```python
print(response.elapsed)
```

This gives the approximate time taken for the request/response exchange as measured by Requests.

---

# 20. Request Object

You can inspect the request:

```python
print(response.request)
```

For example, you can inspect:

```python
response.request.method
response.request.url
```

---

# 21. Cookies

Use:

```python
print(response.cookies)
```

Cookies may contain information sent by the server.

For persistent session state, a `requests.Session()` is often more useful.

---

# 22. JSON Response

If the server returns valid JSON:

```python
data = response.json()

print(data)
```

Example API response:

```json
{
    "name": "Python",
    "version": "3.14"
}
```

Then:

```python
data = response.json()

print(data["name"])
```

---

# 23. Raw Response

You can access the underlying raw response:

```python
print(response.raw)
```

For example:

```python
print(
    response.raw.read()
)
```

This is more advanced and usually not needed for normal scraping.

---

# Part 2: Requests Session

# 24. `requests.Session()`

A session allows you to reuse settings and maintain session state such as cookies.

Example:

```python
import requests

session = requests.Session()

session.headers.update({
    "User-Agent": "MyCrawler/1.0"
})

response = session.get(
    "https://example.com",
    timeout=10
)

print(response.status_code)
```

### Benefits

* Reuse connection-related resources
* Reuse headers
* Maintain cookies
* Keep common request settings

---

# 25. User-Agent

A crawler should identify itself appropriately.

Example:

```python
import requests

headers = {
    "User-Agent": "MyCrawler/1.0"
}

response = requests.get(
    "https://example.com",
    headers=headers,
    timeout=10
)

print(response.status_code)
```

For a real production crawler, use a descriptive User-Agent.

Also follow the website's:

* Terms
* Access rules
* Robots instructions where applicable
* Rate limits
* Applicable laws

---

# Part 3: BeautifulSoup

# 26. What is BeautifulSoup?

**BeautifulSoup** is a Python library used to parse HTML and XML-like markup and extract information from it.

Install:

```bash
pip install beautifulsoup4
```

Import:

```python
from bs4 import BeautifulSoup
```

---

# 27. Parse HTML

```python
import requests

from bs4 import BeautifulSoup

url = "https://example.com"

response = requests.get(
    url,
    timeout=10
)

response.raise_for_status()

soup = BeautifulSoup(
    response.text,
    "html.parser"
)

print(soup)
```

Here:

```text
requests
    ↓
Downloads HTML

BeautifulSoup
    ↓
Parses HTML
```

---

# 28. Get Page Title

Get the complete `<title>` tag:

```python
title = soup.title

print(title)
```

Get only the text:

```python
print(
    soup.title.get_text(strip=True)
)
```

Safe version:

```python
title = (
    soup.title.get_text(strip=True)
    if soup.title
    else "No Title"
)
```

---

# 29. Extract Headings

```python
for heading in soup.find_all("h1"):
    print(
        heading.get_text(strip=True)
    )
```

This extracts all `<h1>` elements.

---

# 30. Extract Paragraphs

```python
for paragraph in soup.find_all("p"):
    print(
        paragraph.get_text(strip=True)
    )
```

---

# 31. Extract Links

```python
for link in soup.find_all(
    "a",
    href=True
):
    print(
        link["href"]
    )
```

Example HTML:

```html
<a href="/about">About</a>
```

The result is:

```text
/about
```

---

# 32. Extract Images

```python
for image in soup.find_all(
    "img",
    src=True
):
    print(
        image["src"]
    )
```

---

# 33. HTML Attributes

Suppose the HTML is:

```html
<a href="/about" class="menu">
    About
</a>
```

Python:

```python
link = soup.find("a")

print(
    link.get("href")
)

print(
    link.get("class")
)
```

Output may be:

```text
/about
['menu']
```

---

# 34. `find()`

`find()` returns the **first matching element**.

Example:

```python
heading = soup.find("h1")

print(heading)
```

---

# 35. `find_all()`

`find_all()` returns **all matching elements**.

Example:

```python
headings = soup.find_all("h1")

for heading in headings:
    print(
        heading.get_text(strip=True)
    )
```

### Remember

```text
find()
→ First matching element

find_all()
→ All matching elements
```

---

# 36. CSS Selectors

BeautifulSoup also supports CSS selectors.

### Class

```python
items = soup.select(".product")

for item in items:
    print(
        item.get_text(strip=True)
    )
```

### ID

```python
element = soup.select_one("#main")
```

### One class element

```python
element = soup.select_one(".product")
```

### Important CSS syntax

```text
.product
→ class="product"

#main
→ id="main"

a
→ all <a> elements
```

---

# Part 4: URL Handling

# 37. `urllib.parse`

Python provides URL tools through `urllib.parse`.

Import:

```python
from urllib.parse import (
    urljoin,
    urlparse
)
```

---

# 38. Relative URL

Suppose:

```text
Base URL:
https://example.com

Link:
/about
```

The link is relative.

Use `urljoin()`:

```python
from urllib.parse import urljoin

full_url = urljoin(
    "https://example.com",
    "/about"
)

print(full_url)
```

Output:

```text
https://example.com/about
```

### Easy Definition

> **`urljoin()` converts a relative URL into the correct absolute URL.**

This is very important in web crawling.

---

# 39. `urlparse()`

`urlparse()` breaks a URL into different parts.

Example:

```python
from urllib.parse import urlparse

url = "https://example.com/products?id=10"

parsed = urlparse(url)

print(parsed.scheme)
print(parsed.netloc)
print(parsed.path)
print(parsed.query)
```

Output:

```text
https
example.com
/products
id=10
```

### Main parts

```text
scheme
→ https

netloc
→ example.com

path
→ /products

query
→ id=10
```

---

# Part 5: Basic Web Crawler

# 40. Basic Crawler

```python
import requests

from bs4 import BeautifulSoup

url = "https://example.com"

response = requests.get(
    url,
    timeout=10
)

response.raise_for_status()

soup = BeautifulSoup(
    response.text,
    "html.parser"
)

for link in soup.find_all(
    "a",
    href=True
):
    print(
        link["href"]
    )
```

This crawler:

```text
Request page
    ↓
Get HTML
    ↓
Parse HTML
    ↓
Find <a> tags
    ↓
Extract links
```

---

# Part 6: Multi-Page Crawler

# 41. Recursive Crawler

A simple recursive crawler can look like this:

```python
import requests

from bs4 import BeautifulSoup

from urllib.parse import urljoin


visited = set()


def crawl(url, depth):

    if depth == 0:
        return

    if url in visited:
        return

    visited.add(url)

    print("Crawling:", url)

    try:
        response = requests.get(
            url,
            timeout=10
        )

        response.raise_for_status()

    except requests.RequestException:
        return

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    for link in soup.find_all(
        "a",
        href=True
    ):

        next_url = urljoin(
            url,
            link["href"]
        )

        crawl(
            next_url,
            depth - 1
        )


crawl(
    "https://example.com",
    depth=2
)
```

### Main idea

```text
Start URL
   ↓
Visit page
   ↓
Find links
   ↓
Visit links
   ↓
Find more links
   ↓
Continue
```

---

# 42. Why Do We Need `visited`?

Imagine:

```text
A → B
B → C
C → A
```

Without a visited set:

```text
A → B → C → A → B → C → ...
```

This can create an endless loop.

So we use:

```python
visited = set()
```

Before crawling:

```python
if url in visited:
    return
```

Then:

```python
visited.add(url)
```

### Easy Definition

> **`visited` prevents the crawler from processing the same URL repeatedly.**

---

# 43. Depth Control

Depth limits how far the crawler can go.

Example:

```text
Depth 0
Start page

Depth 1
 ├── A
 ├── B
 └── C

Depth 2
 ├── A1
 ├── A2
 ├── B1
 └── C1
```

For example:

```python
max_depth = 2
```

Depth control prevents the crawler from exploring an unlimited number of pages.

---

# Part 7: Queue-Based Crawler

# 44. BFS-Style Crawler

Instead of recursion, we can use a queue.

```python
import requests

from bs4 import BeautifulSoup

from urllib.parse import urljoin

from collections import deque


visited = set()

start_url = "https://example.com"

max_depth = 2

queue = deque([
    (start_url, 0)
])


while queue:

    url, depth = queue.popleft()

    if depth > max_depth:
        continue

    if url in visited:
        continue

    visited.add(url)

    print(
        f"Crawling ({depth}): {url}"
    )

    try:

        response = requests.get(
            url,
            timeout=10
        )

        response.raise_for_status()

    except requests.RequestException:

        continue

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    for link in soup.find_all(
        "a",
        href=True
    ):

        next_url = urljoin(
            url,
            link["href"]
        )

        if next_url not in visited:

            queue.append(
                (
                    next_url,
                    depth + 1
                )
            )
```

This is similar to **Breadth-First Search (BFS)**.

### Why use `deque`?

Because:

```python
queue.popleft()
```

is efficient.

---

# Part 8: Domain Restriction

# 45. Why Restrict the Domain?

Suppose you start from:

```text
https://example.com
```

The page may contain links to:

```text
https://google.com
https://youtube.com
https://example.com/about
```

You may want to crawl only:

```text
example.com
```

---

# 46. Same-Domain Check

```python
from urllib.parse import urlparse


def is_same_domain(url, domain):

    return (
        urlparse(url).netloc
        == domain
    )
```

Example:

```python
domain = "example.com"

print(
    is_same_domain(
        "https://example.com/about",
        domain
    )
)
```

Result:

```text
True
```

---

# 47. Domain-Restricted Crawler

```python
import requests

from bs4 import BeautifulSoup

from urllib.parse import (
    urljoin,
    urlparse
)


visited = set()

start_url = "https://example.com"

domain = urlparse(
    start_url
).netloc


def crawl(url):

    if url in visited:
        return

    if urlparse(url).netloc != domain:
        return

    visited.add(url)

    print(
        "Crawling:",
        url
    )

    try:

        response = requests.get(
            url,
            timeout=10
        )

        response.raise_for_status()

    except requests.RequestException:

        return

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    for link in soup.find_all(
        "a",
        href=True
    ):

        next_url = urljoin(
            url,
            link["href"]
        )

        next_url = next_url.split(
            "#",
            1
        )[0]

        crawl(next_url)


crawl(start_url)
```

---

# Part 9: URL Fragment

# 48. What is a URL Fragment?

Example:

```text
https://example.com/about#team
```

Here:

```text
#team
```

is the **fragment**.

For crawling, the fragment often does not identify a different server resource.

We can remove it:

```python
url = url.split(
    "#",
    1
)[0]
```

Example:

```text
https://example.com/about#team
```

becomes:

```text
https://example.com/about
```

This can reduce duplicate URLs.

---

# Part 10: Data Extraction

# 49. Extract Title + Links

```python
import requests

from bs4 import BeautifulSoup

from urllib.parse import urljoin


url = "https://example.com"

response = requests.get(
    url,
    timeout=10
)

response.raise_for_status()

soup = BeautifulSoup(
    response.text,
    "html.parser"
)

title = (
    soup.title.get_text(strip=True)
    if soup.title
    else None
)

links = []

for a in soup.find_all(
    "a",
    href=True
):

    full_url = urljoin(
        url,
        a["href"]
    )

    links.append(full_url)


data = {
    "title": title,
    "links": links
}

print(data)
```

---

# 50. Extract Structured Data

```python
import requests

from bs4 import BeautifulSoup


url = "https://example.com"

response = requests.get(
    url,
    timeout=10
)

response.raise_for_status()

soup = BeautifulSoup(
    response.text,
    "html.parser"
)

data = {

    "title": (
        soup.title.get_text(strip=True)
        if soup.title
        else None
    ),

    "h1": [
        h.get_text(strip=True)
        for h in soup.find_all("h1")
    ],

    "paragraphs": [
        p.get_text(strip=True)
        for p in soup.find_all("p")
    ]

}

print(data)
```

---

# Part 11: Save Data

# 51. Save as JSON

```python
import json

data = {
    "name": "Python",
    "type": "Programming Language"
}

with open(
    "data.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        data,
        file,
        indent=4,
        ensure_ascii=False
    )
```

---

# 52. Save as CSV

```python
import csv

data = [
    ["Name", "Price"],
    ["Product A", "100"],
    ["Product B", "200"]
]

with open(
    "products.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.writer(file)

    writer.writerows(data)
```

---

# 53. Save with Pandas

Install:

```bash
pip install pandas
```

Code:

```python
import pandas as pd

data = [
    {
        "name": "Product A",
        "price": 100
    },
    {
        "name": "Product B",
        "price": 200
    }
]

df = pd.DataFrame(data)

print(df)

df.to_csv(
    "products.csv",
    index=False
)
```

### When is Pandas useful?

Pandas is especially useful when you want to:

* Clean data
* Analyze data
* Filter data
* Sort data
* Export structured data

---

# 54. Save HTML

```python
import os

import requests


url = "https://example.com"

response = requests.get(
    url,
    timeout=10
)

response.raise_for_status()

os.makedirs(
    "websites",
    exist_ok=True
)

with open(
    "websites/index.html",
    "w",
    encoding="utf-8"
) as file:

    file.write(
        response.text
    )
```

---

# Part 12: Rate Limiting

# 55. What is Rate Limiting?

Rate limiting controls how frequently the crawler sends requests.

Simple example:

```python
import time

time.sleep(1)
```

Example:

```python
for url in urls:

    response = requests.get(
        url,
        timeout=10
    )

    time.sleep(1)
```

### Why?

It helps reduce excessive load on the server.

In real crawlers, rate limits should be designed according to the site's policies and technical constraints.

---

# Part 13: Error Handling

# 56. Handle Request Errors

```python
try:

    response = requests.get(
        url,
        timeout=10
    )

    response.raise_for_status()

except requests.RequestException as e:

    print(
        f"Error: {e}"
    )
```

This prevents one failed request from crashing the entire crawler.

---

# 57. Retry

Temporary network failures may happen.

A simple retry function:

```python
import time

import requests


def fetch(
    url,
    retries=3
):

    for attempt in range(retries):

        try:

            response = requests.get(
                url,
                timeout=10
            )

            response.raise_for_status()

            return response

        except requests.RequestException as e:

            print(
                f"Attempt {attempt + 1} failed: {e}"
            )

            time.sleep(2)

    return None
```

### Better production approach

A production crawler may use:

```text
Retry
+
Exponential Backoff
+
Maximum Retry Limit
```

---

# Part 14: Threading

# 58. Basic Threading

Threads can be useful for I/O-bound crawling.

```python
import threading


def worker():

    print(
        "Worker running"
    )


threads = []

for _ in range(5):

    thread = threading.Thread(
        target=worker
    )

    thread.start()

    threads.append(thread)


for thread in threads:

    thread.join()
```

### Important

Threading does not automatically make every program faster.

It is most useful here when work spends significant time waiting for I/O.

---

# Part 15: Queue + Threading

# 59. Worker Queue

```python
from queue import Queue

import threading


queue = Queue()


def worker():

    while True:

        item = queue.get()

        if item is None:

            queue.task_done()

            break

        print(
            "Processing:",
            item
        )

        queue.task_done()


for item in range(10):

    queue.put(item)


threads = []

for _ in range(3):

    thread = threading.Thread(
        target=worker
    )

    thread.start()

    threads.append(thread)


queue.join()


for _ in threads:

    queue.put(None)


for thread in threads:

    thread.join()
```

### Architecture

```text
              Queue
          /      |      \
         ↓       ↓       ↓
     Worker 1 Worker 2 Worker 3
         ↓       ↓       ↓
        Task    Task    Task
```

This is a common worker-based pattern.

---

# Part 16: Thread Safety

# 60. `Lock` + Visited Set

When multiple threads access shared data, synchronization may be necessary.

Example:

```python
import threading

visited = set()

lock = threading.Lock()

with lock:

    if url not in visited:

        visited.add(url)
```

The lock protects the check-and-add operation from concurrent access.

### Important

> **When multiple threads share mutable data, think about thread safety.**

---

# Part 17: Robots.txt

# 61. What is `robots.txt`?

Many websites publish crawler instructions at:

```text
https://example.com/robots.txt
```

Python provides:

```python
from urllib.robotparser import RobotFileParser
```

Example:

```python
from urllib.robotparser import RobotFileParser


rp = RobotFileParser()

rp.set_url(
    "https://example.com/robots.txt"
)

rp.read()

allowed = rp.can_fetch(
    "MyCrawler/1.0",
    "https://example.com/page"
)

print(allowed)
```

### Main idea

```text
robots.txt
    ↓
Crawler access instructions
    ↓
Check whether crawling is allowed
```

You should respect the site's published crawling instructions and applicable access restrictions.

---

# Part 18: Dynamic Websites

# 62. Static vs Dynamic Website

Some websites do not contain the actual data in the initial HTML.

The page may work like:

```text
Browser
   ↓
Initial HTML
   ↓
JavaScript
   ↓
API Request
   ↓
Data
   ↓
DOM Update
```

In these cases, simple `requests + BeautifulSoup` may not be enough.

Possible tools:

```text
Selenium
Playwright
```

But first check whether the data is available through a public API or direct HTTP request.

---

# Part 19: Selenium

# 63. What is Selenium?

Selenium is a browser automation tool.

Install:

```bash
pip install selenium
```

Basic example:

```python
from selenium import webdriver


driver = webdriver.Chrome()

driver.get(
    "https://example.com"
)

print(
    driver.title
)

driver.quit()
```

### Selenium can

* Open a browser
* Visit pages
* Click buttons
* Fill forms
* Execute JavaScript
* Read rendered page content

---

# Part 20: Playwright

# 64. What is Playwright?

Playwright is another browser automation tool.

Install:

```bash
pip install playwright
```

Install browser binaries:

```bash
playwright install
```

Example:

```python
from playwright.sync_api import sync_playwright


with sync_playwright() as p:

    browser = p.chromium.launch()

    page = browser.new_page()

    page.goto(
        "https://example.com"
    )

    print(
        page.title()
    )

    browser.close()
```

### Selenium vs Playwright

Both can automate browsers.

Playwright is especially popular for modern web applications and supports multiple browser engines.

---

# Part 21: Scrapy

# 65. What is Scrapy?

**Scrapy** is a Python framework designed for web crawling and web scraping.

It provides many features out of the box:

* Request scheduling
* Concurrency
* Spiders
* Item pipelines
* Middleware
* Feed exports
* Crawling structure

Install:

```bash
pip install scrapy
```

Create project:

```bash
scrapy startproject mycrawler
```

Create spider:

```bash
scrapy genspider example example.com
```

---

# 66. Basic Scrapy Spider

```python
import scrapy


class ExampleSpider(scrapy.Spider):

    name = "example"

    allowed_domains = [
        "example.com"
    ]

    start_urls = [
        "https://example.com"
    ]

    def parse(self, response):

        title = response.css(
            "title::text"
        ).get()

        yield {
            "title": title
        }

        for link in response.css(
            "a::attr(href)"
        ).getall():

            yield response.follow(
                link,
                callback=self.parse
            )
```

### Important Scrapy concepts

```text
Spider
→ Crawling logic

Request
→ Web request

Response
→ Server response

Item
→ Extracted data

Pipeline
→ Process/store data

Middleware
→ Modify request/response behavior
```

---

# Part 22: Requests + BeautifulSoup vs Scrapy

# 67. Comparison

| Feature           | Requests + BeautifulSoup | Scrapy                  |
| ----------------- | ------------------------ | ----------------------- |
| Learning          | Easy                     | Medium                  |
| Small project     | Excellent                | Good                    |
| Large crawler     | More manual work         | Excellent               |
| Queue             | Manual                   | Built-in                |
| Pipeline          | Manual                   | Built-in                |
| Middleware        | Manual                   | Built-in                |
| Concurrency       | Manual                   | Built-in                |
| Project structure | Simple                   | Structured              |
| Best for          | Small/custom scripts     | Large crawling projects |

### Simple Rule

```text
Small project
→ Requests + BeautifulSoup

Large crawler
→ Scrapy
```

---

# Part 23: Async Crawling

# 68. Async HTTP Crawling

For many HTTP requests, asynchronous programming can be useful.

Popular tools:

```text
asyncio
aiohttp
httpx
```

Conceptually:

```text
Request 1 ──┐
Request 2 ──┤
Request 3 ──┼── Async Event Loop
Request 4 ──┤
Request 5 ──┘
```

Async crawling is especially useful when the workload is heavily I/O-bound.

---

# Part 24: Production Crawler Architecture

# 69. Production Crawler

A production crawler may have this architecture:

```text
START URL
    ↓
URL Scheduler
    ↓
URL Queue
    ↓
HTTP Downloader
    ↓
Response Check
    ↓
HTML Parser
    ↓
 ┌───────────────┴───────────────┐
 ↓                               ↓
Link Extractor                Data Extractor
 ↓                               ↓
URL Normalize                 Data Cleaning
 ↓                               ↓
Duplicate Check               Data Storage
 ↓
URL Scheduler
```

---

# Part 25: Production Features

# 70. Basic Features

```text
✓ Requests
✓ BeautifulSoup
✓ Queue
✓ Visited Set
✓ Depth Control
✓ Domain Filtering
```

### Intermediate Features

```text
✓ Headers
✓ Timeout
✓ Error Handling
✓ Retry
✓ Rate Limiting
✓ URL Normalization
```

### Advanced Features

```text
✓ Threading
✓ Async I/O
✓ Logging
✓ Persistent Queue
✓ Database
✓ Duplicate Detection
✓ Robots.txt
✓ Content-Type Validation
```

---

# Part 26: Complete Crawler

# 71. Production-Style Crawler Example

```python
import os

import requests

from bs4 import BeautifulSoup

from urllib.parse import (
    urljoin,
    urlparse
)

from collections import deque


class ProductionCrawler:

    def __init__(
        self,
        start_url,
        max_depth=2,
        base_folder="websites"
    ):

        self.start_url = (
            start_url.rstrip("/")
        )

        self.max_depth = max_depth

        self.base_folder = base_folder

        self.visited = set()

        self.queue = deque([
            (
                self.start_url,
                0
            )
        ])

        self.session = (
            requests.Session()
        )

        self.session.headers.update({

            "User-Agent":
                "MyCrawler/1.0"

        })


    def is_same_domain(
        self,
        url
    ):

        start_domain = (
            urlparse(
                self.start_url
            ).netloc
        )

        current_domain = (
            urlparse(
                url
            ).netloc
        )

        return (
            current_domain
            == start_domain
        )


    def create_directory(
        self,
        url
    ):

        parsed_url = urlparse(url)

        domain_folder = (
            parsed_url.netloc
            .replace(":", "_")
        )

        folder_path = os.path.join(
            self.base_folder,
            domain_folder
        )

        os.makedirs(
            folder_path,
            exist_ok=True
        )

        return folder_path


    def save_html(
        self,
        url,
        html
    ):

        folder_path = (
            self.create_directory(
                url
            )
        )

        if (
            url.rstrip("/")
            == self.start_url
        ):

            file_name = "index.html"

        else:

            file_name = (
                f"{abs(hash(url))}.html"
            )

        file_path = os.path.join(
            folder_path,
            file_name
        )

        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(html)

        return file_path


    def fetch(
        self,
        url
    ):

        try:

            response = (
                self.session.get(
                    url,
                    timeout=10
                )
            )

            response.raise_for_status()

            return response

        except requests.RequestException as e:

            print(
                f"Request failed: {url}"
            )

            print(
                f"Error: {e}"
            )

            return None


    def crawl(self):

        while self.queue:

            url, depth = (
                self.queue.popleft()
            )

            if (
                depth
                > self.max_depth
            ):

                continue

            if url in self.visited:

                continue

            self.visited.add(url)

            print(
                f"[{depth}/"
                f"{self.max_depth}] "
                f"Crawling: {url}"
            )

            response = self.fetch(url)

            if response is None:

                continue

            file_path = (
                self.save_html(
                    url,
                    response.text
                )
            )

            print(
                f"Saved: {file_path}"
            )

            if (
                depth
                == self.max_depth
            ):

                continue

            soup = BeautifulSoup(
                response.text,
                "html.parser"
            )

            for tag in soup.find_all(
                "a",
                href=True
            ):

                next_url = urljoin(
                    url,
                    tag["href"]
                )

                next_url = (
                    next_url.split(
                        "#",
                        1
                    )[0]
                )

                if not next_url.startswith(
                    (
                        "http://",
                        "https://"
                    )
                ):

                    continue

                if not self.is_same_domain(
                    next_url
                ):

                    continue

                if (
                    next_url
                    not in self.visited
                ):

                    self.queue.append(
                        (
                            next_url,
                            depth + 1
                        )
                    )


if __name__ == "__main__":

    start_url = (
        "https://example.com"
    )

    crawler = ProductionCrawler(
        start_url=start_url,
        max_depth=2
    )

    crawler.crawl()
```

---

# Part 27: Production Crawler Flow

# 72. How Does It Work?

```text
Start URL
    ↓
Queue
    ↓
popleft()
    ↓
Visited Check
    ↓
HTTP Request
    ↓
Status Check
    ↓
Save HTML
    ↓
BeautifulSoup
    ↓
Find <a>
    ↓
urljoin()
    ↓
Remove Fragment
    ↓
HTTP/HTTPS Check
    ↓
Same Domain Check
    ↓
Visited Check
    ↓
Queue
    ↓
Next Page
```

---

# Part 28: Important Python Data Structures

# 73. `set`

```python
visited = set()
```

### Purpose

Avoid duplicate URLs.

Example:

```text
A
B
C
A  ← Duplicate
```

The set keeps only unique values.

---

# 74. `list`

```python
urls = []
```

### Purpose

Simple collection of URLs or data.

---

# 75. `dict`

```python
data = {
    "title": "Python",
    "url": "https://example.com"
}
```

### Purpose

Store structured data.

---

# 76. `Queue`

```python
from queue import Queue
```

Useful for worker-based processing, especially with threads.

---

# 77. `deque`

```python
from collections import deque
```

Useful for efficient queue operations such as:

```python
queue.popleft()
```

It is especially useful for BFS-style crawling.

---

# Part 29: Crawler Core

# 78. Core Concept

The basic crawler process is:

```text
URL
 ↓
Request
 ↓
Response
 ↓
HTML
 ↓
Parse
 ↓
Find Links
 ↓
Queue
 ↓
Visited
 ↓
Next URL
```

---

# Part 30: Scraper Core

# 79. Core Scraping Process

```text
URL
 ↓
HTTP Request
 ↓
HTML
 ↓
BeautifulSoup
 ↓
Find Elements
 ↓
Extract Data
 ↓
Clean Data
 ↓
JSON / CSV / Database
```

---

# Part 31: Common Mistakes

# 80. Mistake 1 — No Timeout

Bad:

```python
requests.get(url)
```

Better:

```python
requests.get(
    url,
    timeout=10
)
```

---

# 81. Mistake 2 — No Visited Set

Without:

```python
visited = set()
```

the crawler may process the same pages repeatedly.

Possible result:

```text
Infinite Loop
```

---

# 82. Mistake 3 — Not Handling Relative URLs

Bad:

```python
next_url = link["href"]
```

If the link is:

```text
/about
```

this is not a complete URL.

Better:

```python
next_url = urljoin(
    current_url,
    link["href"]
)
```

---

# 83. Mistake 4 — Crawling External Domains

A page may contain links to other websites.

Use domain filtering:

```python
if not is_same_domain(next_url):
    continue
```

---

# 84. Mistake 5 — No Error Handling

Bad:

```python
response = requests.get(url)
```

Better:

```python
try:

    response = requests.get(
        url,
        timeout=10
    )

    response.raise_for_status()

except requests.RequestException:
    pass
```

---

# 85. Mistake 6 — Sending Requests Too Quickly

Bad crawler:

```text
Request
Request
Request
Request
Request
Request
...
```

Better:

```text
Rate Limiting
+
Retry
+
Backoff
```

This helps reduce unnecessary load and handles temporary failures more responsibly.

---

# Part 32: URL Normalization

# 86. Why Normalize URLs?

The same resource may appear in different URL forms.

Example:

```text
https://example.com/page
https://example.com/page#section
```

The fragment can be removed:

```python
url = url.split(
    "#",
    1
)[0]
```

Depending on the project, you may also need to consider:

* Query parameters
* Trailing slashes
* URL encoding
* Case sensitivity
* Default ports

### Important

URL normalization rules depend on the application. Do not blindly remove query parameters because they may identify different resources.

---

# Part 33: Crawler Optimization

# 87. Optimization Techniques

Useful optimizations include:

1. Use a `Session`
2. Reuse connections
3. Deduplicate URLs
4. Restrict domains
5. Limit depth
6. Use rate limiting
7. Use concurrency carefully
8. Use async I/O when appropriate
9. Use an efficient parser
10. Add database indexes
11. Use retry logic
12. Add logging

---

# Part 34: Data Storage

# 88. Where Should We Store Scraped Data?

### Small Project

```text
JSON
CSV
```

### Medium Project

```text
SQLite
```

### Large Project

```text
PostgreSQL
MongoDB
```

### Simple Rule

```text
Small data
→ JSON / CSV

Structured application data
→ SQLite / PostgreSQL

Large-scale or document-oriented data
→ MongoDB or another suitable database
```

Choose the storage system based on the project requirements.

---

# Part 35: Static vs Dynamic Website

# 89. Static Website

For a simple static website:

```text
Requests
   ↓
HTML
   ↓
BeautifulSoup
   ↓
Data
```

---

# 90. Dynamic Website

For a JavaScript-heavy website:

```text
Browser
   ↓
HTML
   ↓
JavaScript
   ↓
API
   ↓
Data
```

Possible tools:

```text
Selenium
Playwright
```

But if a public API or direct HTTP endpoint provides the required data, that is often simpler and more efficient than browser automation.

---

# Part 36: Crawler vs Spider

# 91. Crawler vs Spider

### Crawler

A general concept.

```text
Find URLs
Visit URLs
Follow Links
```

### Spider

In Scrapy, a **Spider** is a class that defines crawling and extraction logic.

Example:

```python
class ExampleSpider(scrapy.Spider):
    ...
```

### Easy way to remember

```text
Crawler
→ General concept

Spider
→ Scrapy crawling component
```

---

# Part 37: Crawler vs Scraper

# 92. Crawler vs Scraper

### Crawler

Main focus:

```text
URL Discovery
Page Navigation
```

### Scraper

Main focus:

```text
Data Extraction
Data Cleaning
Data Storage
```

---

# Part 38: Web Crawling Roadmap

# 93. Learning Roadmap

```text
STEP 01
HTTP Basics
    ↓
STEP 02
Requests
    ↓
STEP 03
HTML Basics
    ↓
STEP 04
BeautifulSoup
    ↓
STEP 05
URL Handling
    ↓
STEP 06
Basic Crawler
    ↓
STEP 07
Depth Control
    ↓
STEP 08
Domain Restriction
    ↓
STEP 09
Data Extraction
    ↓
STEP 10
JSON / CSV
    ↓
STEP 11
Error Handling
    ↓
STEP 12
Rate Limiting
    ↓
STEP 13
Threading / Queue
    ↓
STEP 14
Async I/O
    ↓
STEP 15
Selenium / Playwright
    ↓
STEP 16
Scrapy
    ↓
STEP 17
Production Crawler
```

---

# Part 39: Practice Projects

# 94. Project 1 — Link Extractor

Input:

```text
Website URL
```

Output:

```text
All Links
```

---

# 95. Project 2 — Website Crawler

Input:

```text
Start URL
```

Output:

```text
Visited URLs
```

---

# 96. Project 3 — Website Structure Mapper

```text
URL
 ↓
Links
 ↓
Tree Structure
```

---

# 97. Project 4 — News Scraper

Extract:

```text
Title
Author
Date
URL
```

---

# 98. Project 5 — Product Scraper

Extract:

```text
Product
Price
Rating
URL
```

---

# 99. Project 6 — Job Scraper

Extract:

```text
Job Title
Company
Location
URL
```

---

# 100. Project 7 — Multi-threaded Crawler

Use:

```text
Queue
+
Threads
+
Visited Set
```

---

# 101. Project 8 — Scrapy Project

Use:

```text
Spider
Pipeline
Middleware
Database
```

---

# Part 40: Required Packages

# 102. Basic

```bash
pip install requests beautifulsoup4
```

### Pandas

```bash
pip install pandas
```

### Selenium

```bash
pip install selenium
```

### Playwright

```bash
pip install playwright
playwright install
```

### Scrapy

```bash
pip install scrapy
```

### Optional

```bash
pip install lxml
pip install aiohttp
pip install httpx
```

---

# Part 41: Short Revision

# 103. Quick Revision

```text
Web Crawling
→ Discover and visit web pages
```

```text
Web Scraping
→ Extract useful data from web pages
```

```text
Requests
→ Send HTTP requests
```

```text
BeautifulSoup
→ Parse HTML and extract data
```

```text
urljoin()
→ Convert relative URL to absolute URL
```

```text
urlparse()
→ Break URL into components
```

```text
Set
→ Prevent duplicate URLs
```

```text
Queue / deque
→ Manage URLs
```

```text
Depth
→ Control crawling levels
```

```text
Domain Restriction
→ Stay inside the target domain
```

```text
Session
→ Reuse settings and maintain session state
```

```text
Timeout
→ Prevent requests from waiting indefinitely
```

```text
Retry
→ Handle temporary failures
```

```text
Rate Limiting
→ Control request frequency
```

```text
robots.txt
→ Check published crawler access rules
```

```text
Selenium / Playwright
→ Automate browsers
```

```text
Scrapy
→ Framework for larger crawling/scraping projects
```

---

# Part 42: Interview Questions

# 104. What is Web Crawling?

### Answer

> **Web crawling is the automated process of discovering and visiting web pages, usually by following links.**

---

# 105. What is Web Scraping?

### Answer

> **Web scraping is the automated process of extracting useful data from web pages.**

---

# 106. What is the difference between Crawling and Scraping?

### Answer

```text
Crawling
→ Finds and visits pages

Scraping
→ Extracts data from pages
```

---

# 107. Why is `requests` used?

### Answer

`requests` is used to send HTTP requests and receive HTTP responses.

Example:

```python
response = requests.get(
    url,
    timeout=10
)
```

---

# 108. Why use BeautifulSoup?

### Answer

BeautifulSoup is used to parse HTML and extract elements such as:

```text
Title
Headings
Paragraphs
Links
Images
Attributes
```

---

# 109. What is `urljoin()`?

### Answer

`urljoin()` combines a base URL with a relative URL.

Example:

```python
urljoin(
    "https://example.com",
    "/about"
)
```

Result:

```text
https://example.com/about
```

---

# 110. Why do we use a `visited` set?

### Answer

To prevent processing the same URL multiple times and to reduce the chance of infinite crawling loops.

---

# 111. Why do we need depth control?

### Answer

Depth control limits how far the crawler can explore.

It prevents uncontrolled crawling.

---

# 112. Why use domain restriction?

### Answer

To prevent the crawler from leaving the target website/domain.

---

# 113. What is `robots.txt`?

### Answer

`robots.txt` is a file that can publish instructions about which parts of a site automated crawlers may access.

---

# 114. What is Scrapy?

### Answer

> **Scrapy is a Python framework for building web crawlers and web scrapers.**

It provides features such as:

```text
Spiders
Request scheduling
Concurrency
Pipelines
Middleware
Feed exports
```

---

# 115. When should you use Selenium or Playwright?

### Answer

Use browser automation when the required content or interaction depends on browser-side JavaScript and cannot be conveniently obtained through direct HTTP requests.

---

# 116. Why use a `Session`?

### Answer

A `requests.Session()` can:

* Reuse connections
* Reuse headers
* Maintain cookies
* Keep common request settings

---

# 117. Why is timeout important?

### Answer

A timeout prevents a network request from waiting indefinitely.

---

# 118. Why use retry?

### Answer

Network requests can fail temporarily.

Retry logic gives the request another chance.

Production systems often combine:

```text
Retry
+
Backoff
+
Maximum Attempts
```

---

# 119. What is the difference between threading and async?

### Simple Answer

Both can help with I/O-bound work, but they use different models.

```text
Threading
→ Multiple threads execute work

Async
→ An event loop manages cooperative asynchronous tasks
```

For many network operations, async can be very efficient, while threads can be easier for some existing synchronous code.

---

# Part 43: Final Mental Model

# 120. Complete Web Crawling System

```text
                         WEB
                          |
                          ↓
                    HTTP Request
                          |
                          ↓
                       Requests
                          |
                          ↓
                      HTML Page
                          |
                          ↓
                   BeautifulSoup
                          |
             +------------+------------+
             |                         |
             ↓                         ↓
        Extract Data                Links
             |                         |
             ↓                         ↓
        JSON / CSV               URL Handling
             |                         |
             ↓                         ↓
         Database                Queue / Set
                                       |
                                       ↓
                                    Crawler
                                       |
                         +-------------+-------------+
                         |                           |
                         ↓                           ↓
                    Threading                     Async
                         |                           |
                         +-------------+-------------+
                                       |
                                       ↓
                              Selenium / Playwright
                                       |
                                       ↓
                                    Scrapy
                                       |
                                       ↓
                              Production Crawler
```

---

# 121. Final Formula

## Crawler

```text
Crawler
=
URL Discovery
+
Queue
+
Visited
+
HTTP Request
+
Link Following
```

## Scraper

```text
Scraper
=
HTTP Request
+
HTML Parsing
+
Data Extraction
+
Data Cleaning
+
Data Storage
```

## Complete Web Scraping System

```text
Crawler
   ↓
URL Discovery
   ↓
HTTP Request
   ↓
HTML Parsing
   ↓
Data Extraction
   ↓
Data Cleaning
   ↓
Data Storage
   ↓
Database / CSV / JSON
```

---

# 122. Final Cheat Sheet

```text
┌─────────────────────────────────────────────┐
│       WEB CRAWLING & WEB SCRAPING           │
├─────────────────────────────────────────────┤
│                                             │
│ Crawler                                     │
│ → Find and visit pages                      │
│                                             │
│ Scraper                                     │
│ → Extract useful data                       │
│                                             │
│ requests                                    │
│ → HTTP requests                             │
│                                             │
│ BeautifulSoup                               │
│ → HTML parsing                              │
│                                             │
│ urljoin()                                   │
│ → Relative → Absolute URL                   │
│                                             │
│ urlparse()                                  │
│ → Analyze URL                               │
│                                             │
│ visited set                                 │
│ → Avoid duplicates                          │
│                                             │
│ Queue / deque                               │
│ → Manage URLs                               │
│                                             │
│ Depth                                       │
│ → Control crawl level                       │
│                                             │
│ Domain filtering                            │
│ → Stay inside target domain                 │
│                                             │
│ Session                                     │
│ → Reuse settings / session state            │
│                                             │
│ Timeout                                     │
│ → Limit waiting time                        │
│                                             │
│ Retry + Backoff                             │
│ → Handle temporary failures                 │
│                                             │
│ Rate Limiting                               │
│ → Control request frequency                 │
│                                             │
│ robots.txt                                  │
│ → Check published crawl instructions       │
│                                             │
│ Selenium / Playwright                       │
│ → Browser automation                        │
│                                             │
│ Scrapy                                      │
│ → Large-scale crawling framework            │
│                                             │
└─────────────────────────────────────────────┘
```

# One-Line Memory

```text
Crawler = Find Pages
Scraper = Extract Data
Requests = Get HTML
BeautifulSoup = Parse HTML
urljoin = Fix URLs
Set = Remove Duplicates
Queue = Manage URLs
Depth = Limit Crawling
Session = Reuse Connection/State
Timeout = Stop Waiting Too Long
Retry = Try Again
Rate Limit = Slow Down Requests
Selenium/Playwright = Control Browser
Scrapy = Build Large Crawlers
```

## Most Important Concept

> **Web Crawling finds and visits pages. Web Scraping extracts useful information from those pages.**

The basic workflow is:

```text
URL
 ↓
HTTP Request
 ↓
Response
 ↓
HTML
 ↓
Parse
 ↓
Find Links / Data
 ↓
Normalize URLs
 ↓
Visited Check
 ↓
Queue
 ↓
Next Page
```

"""
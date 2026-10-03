"""
============================================================
      WEB CRAWLING & WEB SCRAPING WITH PYTHON
                    FULL NOTES
============================================================


1. WEB CRAWLING কী?
============================================================

Web Crawling হলো এমন একটি automated process যেখানে একটি
program website-এর webpage visit করে এবং সেই webpage-এর
links follow করে নতুন webpage খুঁজে বের করে।

সহজভাবে:

Crawling = কোথায় কী আছে খুঁজে বের করা।

Example:

Page A
   ↓
Page B
   ↓
Page C
   ↓
Page D

Crawler:
Visit A
   ↓
Find B, C
   ↓
Visit B
   ↓
Find D
   ↓
Visit D


Web Crawler-এর প্রধান কাজ:

- URL সংগ্রহ করা
- নতুন Page খুঁজে বের করা
- এক Page থেকে অন্য Page-এ যাওয়া
- Website structure তৈরি করা
- Search engine indexing-এর জন্য page discover করা
- Website analysis করা


Examples:

- Googlebot
- Bingbot
- Custom Python Crawler
- Scrapy Spider



2. WEB SCRAPING কী?
============================================================

Web Scraping হলো কোনো website থেকে নির্দিষ্ট data
automatedভাবে extract করার process।

সহজভাবে:

Scraping = ওয়েবপেজ থেকে তথ্য বের করা।

Example:

একটি e-commerce website থেকে:

Product Name
Price
Rating
Image
Availability

সংগ্রহ করা।

Web Scraping-এর ব্যবহার:

- Product information
- Price monitoring
- News collection
- Job listing collection
- Research
- Data analysis
- Real-estate data
- Public data collection



3. WEB CRAWLING VS WEB SCRAPING
============================================================

বিষয়              Web Crawling        Web Scraping
------------------------------------------------------------
উদ্দেশ্য           URL/Page খোঁজা      Data বের করা
Focus              Structure           Content
কাজ                Link follow         Data extraction
Output             URLs/Pages          Structured Data
ব্যবহার             Indexing            Analysis/Research
Example             Googlebot           Python Scraper


সহজভাবে:

Crawler = কোথায় আছে?

Scraper = কী আছে?



4. CRAWLING + SCRAPING
============================================================

একটি project-এ দুটো একসাথে ব্যবহার করা যায়:

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



5. WEB CRAWLING-এর ব্যবহার
============================================================

- Search Engine Indexing
- Website Structure Analysis
- Link Discovery
- SEO Analysis
- Research
- Broken Link Detection
- Website Monitoring
- Content Discovery



6. WEB SCRAPING-এর ব্যবহার
============================================================

- Product Information
- Price Monitoring
- News Data
- Job Data
- Research Data
- Real Estate Data
- Public Data Collection
- Data Analysis



7. PYTHON WEB CRAWLING LIBRARIES
============================================================

Basic:

requests
BeautifulSoup
lxml

Crawling Framework:

Scrapy

Browser Automation:

Selenium
Playwright

Async HTTP:

aiohttp
httpx

Data Processing:

pandas
csv
json

Helper:

urllib
re
time



8. কোন LIBRARY কখন ব্যবহার করব?
============================================================

HTTP Request
→ requests

HTML Parsing
→ BeautifulSoup

Fast HTML/XML Parsing
→ lxml

Large-scale Crawling
→ Scrapy

JavaScript Website
→ Selenium / Playwright

Async HTTP
→ aiohttp / httpx

Data Analysis
→ pandas

CSV
→ csv

JSON
→ json



9. REQUESTS INSTALL
============================================================

pip install requests


Import:

import requests



10. BASIC GET REQUEST
============================================================

import requests

url = "https://example.com"

response = requests.get(url)

print(response.status_code)



11. TIMEOUT
============================================================

Timeout ব্যবহার করা ভালো:

response = requests.get(
    url,
    timeout=10
)

Timeout request-কে indefinitely অপেক্ষা করা থেকে
রক্ষা করে।



12. STATUS CODE
============================================================

print(response.status_code)


Common Status Codes:

200 → OK
301 → Permanent Redirect
302 → Temporary Redirect
400 → Bad Request
401 → Unauthorized
403 → Forbidden
404 → Not Found
429 → Too Many Requests
500 → Internal Server Error
502 → Bad Gateway
503 → Service Unavailable



13. RAISE_FOR_STATUS()
============================================================

response.raise_for_status()


Example:

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



14. RESPONSE TEXT
============================================================

print(response.text)


HTML content সাধারণত text হিসেবে পাওয়া যায়।



15. RESPONSE CONTENT
============================================================

print(response.content)


এটি bytes আকারে content দেয়।



16. RESPONSE HEADERS
============================================================

print(response.headers)


নির্দিষ্ট header:

print(
    response.headers.get("Content-Type")
)


সব headers:

for key, value in response.headers.items():

    print(
        f"Key: {key} <-------> Value: {value}"
    )



17. RESPONSE URL
============================================================

print(response.url)



18. RESPONSE HISTORY
============================================================

print(response.history)


Redirect history দেখতে ব্যবহার করা হয়।



19. RESPONSE TIME
============================================================

print(response.elapsed)



20. REQUEST OBJECT
============================================================

print(response.request)



21. COOKIES
============================================================

print(response.cookies)



22. JSON RESPONSE
============================================================

data = response.json()

print(data)


API response JSON হলে এটি ব্যবহার করা যায়।



23. RAW RESPONSE
============================================================

print(response.raw)

print(
    response.raw.read()
)



24. REQUESTS SESSION
============================================================

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



25. USER-AGENT
============================================================

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


Production crawler-এ descriptive User-Agent ব্যবহার করা
ভালো।

Site-এর access rules, terms এবং applicable restrictions
মেনে crawling করতে হবে।



26. BEAUTIFULSOUP
============================================================

Install:

pip install beautifulsoup4


Import:

from bs4 import BeautifulSoup



27. HTML PARSE করা
============================================================

import requests

from bs4 import BeautifulSoup

url = "https://example.com"

response = requests.get(
    url,
    timeout=10
)

soup = BeautifulSoup(
    response.text,
    "html.parser"
)

print(soup)



28. PAGE TITLE
============================================================

title = soup.title

print(title)


শুধু text:

print(
    soup.title.get_text(strip=True)
)


Safe version:

title = (
    soup.title.get_text(strip=True)
    if soup.title
    else "No Title"
)



29. HEADING বের করা
============================================================

for heading in soup.find_all("h1"):

    print(
        heading.get_text(strip=True)
    )



30. PARAGRAPH বের করা
============================================================

for paragraph in soup.find_all("p"):

    print(
        paragraph.get_text(strip=True)
    )



31. LINKS বের করা
============================================================

for link in soup.find_all(
    "a",
    href=True
):

    print(
        link["href"]
    )



32. IMAGES বের করা
============================================================

for image in soup.find_all(
    "img",
    src=True
):

    print(
        image["src"]
    )



33. HTML ATTRIBUTES
============================================================

HTML:

<a href="/about" class="menu">
    About
</a>


Python:

link = soup.find("a")

print(
    link.get("href")
)

print(
    link.get("class")
)



34. FIND()
============================================================

প্রথম matching element:

heading = soup.find("h1")

print(heading)



35. FIND_ALL()
============================================================

সব matching elements:

headings = soup.find_all("h1")

for heading in headings:

    print(
        heading.get_text(strip=True)
    )



36. CSS SELECTOR
============================================================

Class:

items = soup.select(".product")

for item in items:

    print(
        item.get_text(strip=True)
    )


ID:

element = soup.select_one("#main")


Class:

element = soup.select_one(".product")



37. URL HANDLING
============================================================

from urllib.parse import (
    urljoin,
    urlparse
)



38. RELATIVE URL
============================================================

ধরা যাক:

Base URL:

https://example.com

Link:

/about


Convert:

from urllib.parse import urljoin

full_url = urljoin(
    "https://example.com",
    "/about"
)

print(full_url)


Output:

https://example.com/about



39. URLPARSE()
============================================================

from urllib.parse import urlparse

url = "https://example.com/products?id=10"

parsed = urlparse(url)

print(parsed.scheme)
print(parsed.netloc)
print(parsed.path)
print(parsed.query)


Conceptually:

scheme = https
netloc = example.com
path = /products
query = id=10



40. BASIC WEB CRAWLER
============================================================

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



41. MULTI-PAGE CRAWLER
============================================================

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

        crawl(
            next_url,
            depth - 1
        )


crawl(
    "https://example.com",
    depth=2
)



42. VISITED SET কেন দরকার?
============================================================

ধরা যাক:

A → B
B → C
C → A


Visited না থাকলে:

A → B → C → A → B → C → ...


এভাবে infinite loop হতে পারে।

তাই:

visited = set()



43. DEPTH CONTROL
============================================================

max_depth = 2


Example:

Depth 0
Start

Depth 1
 ├── A
 ├── B
 └── C

Depth 2
 ├── A1
 ├── A2
 ├── B1
 └── C1



44. QUEUE-BASED CRAWLER
============================================================

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



45. DOMAIN RESTRICTION
============================================================

Crawler যেন অন্য website-এ না যায়।

from urllib.parse import urlparse


def is_same_domain(
    url,
    domain
):

    return (
        urlparse(url).netloc
        == domain
    )



46. DOMAIN-RESTRICTED CRAWLER
============================================================

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



47. URL FRAGMENT
============================================================

Example:

https://example.com/about#team

এখানে:

#team

হলো fragment।

Crawler-এ fragment remove করা যায়:

url = url.split(
    "#",
    1
)[0]



48. TITLE + LINKS DATA EXTRACTION
============================================================

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



49. DATA EXTRACT
============================================================

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



50. JSON SAVE
============================================================

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



51. CSV SAVE
============================================================

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



52. PANDAS SAVE
============================================================

Install:

pip install pandas


Code:

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



53. HTML FILE SAVE
============================================================

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



54. RATE LIMITING
============================================================

import time

time.sleep(1)


Example:

for url in urls:

    response = requests.get(
        url,
        timeout=10
    )

    time.sleep(1)


Rate limiting server-এর উপর অতিরিক্ত load কমাতে সাহায্য
করে।



55. ERROR HANDLING
============================================================

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



56. RETRY
============================================================

import time

import requests


def fetch(
    url,
    retries=3
):

    for attempt in range(
        retries
    ):

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



57. THREADING
============================================================

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



58. QUEUE + THREADING
============================================================

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



59. THREADING + VISITED LOCK
============================================================

import threading


visited = set()

lock = threading.Lock()


with lock:

    if url not in visited:

        visited.add(url)


Multiple threads একই URL process করা থেকে prevent
করতে lock ব্যবহার করা যায়।



60. ROBOTS.TXT
============================================================

Website crawler rules দেখতে:

https://example.com/robots.txt


Python:

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


Robots.txt-এর নির্দেশনা respect করা উচিত।



61. DYNAMIC WEBSITE
============================================================

কিছু website-এর initial HTML-এ actual data থাকে না।

Flow:

Browser
   ↓
HTML
   ↓
JavaScript
   ↓
API
   ↓
Data
   ↓
DOM Update


এক্ষেত্রে ব্যবহার করা যেতে পারে:

Selenium
Playwright


তবে আগে public API/network request ব্যবহার করা সম্ভব কিনা
দেখা ভালো।



62. SELENIUM
============================================================

Install:

pip install selenium


Basic:

from selenium import webdriver


driver = webdriver.Chrome()


driver.get(
    "https://example.com"
)


print(
    driver.title
)


driver.quit()



63. PLAYWRIGHT
============================================================

Install:

pip install playwright


Browser install:

playwright install


Code:

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



64. SCRAPY
============================================================

Install:

pip install scrapy


Create project:

scrapy startproject mycrawler


Create spider:

scrapy genspider example example.com



65. BASIC SCRAPY SPIDER
============================================================

import scrapy


class ExampleSpider(
    scrapy.Spider
):

    name = "example"


    allowed_domains = [
        "example.com"
    ]


    start_urls = [
        "https://example.com"
    ]


    def parse(
        self,
        response
    ):

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



66. REQUESTS + BEAUTIFULSOUP VS SCRAPY
============================================================

Feature             Requests + BS4      Scrapy
------------------------------------------------
Learning             Easy               Medium
Small Project        Good               Good
Large Crawler        Limited            Excellent
Queue                Manual             Built-in
Pipeline             Manual             Built-in
Middleware           Manual             Built-in
Concurrency          Manual             Built-in
Project Structure    Simple             Structured



67. ASYNC CRAWLING
============================================================

অনেক HTTP request concurrently করতে:

asyncio
aiohttp
httpx


Concept:

Request 1 ──┐
Request 2 ──┤
Request 3 ──┼── Async Event Loop
Request 4 ──┤
Request 5 ──┘



68. PRODUCTION CRAWLER ARCHITECTURE
============================================================

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



69. PRODUCTION CRAWLER FEATURES
============================================================

Basic:

✓ Requests
✓ BeautifulSoup
✓ Queue
✓ Visited
✓ Depth
✓ Domain Filtering


Intermediate:

✓ Headers
✓ Timeout
✓ Error Handling
✓ Retry
✓ Rate Limiting
✓ URL Normalization


Advanced:

✓ Threading
✓ Async
✓ Logging
✓ Persistent Queue
✓ Database
✓ Duplicate Detection
✓ Robots.txt
✓ Content-Type Validation



70. COMPLETE PRODUCTION CRAWLER
============================================================

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

            file_name = (
                "index.html"
            )

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



71. PRODUCTION CRAWLER FLOW
============================================================

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



72. IMPORTANT PYTHON DATA STRUCTURES
============================================================

Set:

visited = set()

Purpose:
Duplicate URL prevent করা।


List:

urls = []

Purpose:
Simple collection।


Dictionary:

data = {
    "title": "Python",
    "url": "https://example.com"
}

Purpose:
Structured data।


Queue:

from queue import Queue

Purpose:
Worker-based processing।


Deque:

from collections import deque

Purpose:
Fast queue operations / BFS crawling।



73. CRAWLER-এর IMPORTANT CONCEPT
============================================================

Crawler-এর core:

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
Links
 ↓
Queue
 ↓
Visited
 ↓
Next URL



74. SCRAPER-এর CORE
============================================================

URL
 ↓
Request
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
JSON/CSV/Database



75. COMMON MISTAKES
============================================================

Mistake 1:

requests.get(url)

Better:

requests.get(
    url,
    timeout=10
)


Mistake 2:

visited না রাখা।

Result:

Infinite Loop


Mistake 3:

Relative URL handle না করা।

Wrong:

next_url = link["href"]

Better:

next_url = urljoin(
    current_url,
    link["href"]
)


Mistake 4:

External domain crawl করা।

Better:

Domain filtering ব্যবহার করা।


Mistake 5:

Error handling না করা।

Better:

try:
    ...
except requests.RequestException:
    ...


Mistake 6:

অতিরিক্ত দ্রুত request পাঠানো।

Better:

Rate limiting
Retry
Backoff



76. URL NORMALIZATION
============================================================

Crawler-এ একই resource-এর duplicate URL আসতে পারে।

Example:

https://example.com/page

https://example.com/page#section

Fragment remove করলে duplicate কমে:

url = url.split(
    "#",
    1
)[0]

আর প্রয়োজন অনুযায়ী query parameters, trailing slash,
case sensitivity ইত্যাদিও project-এর requirements অনুযায়ী
normalize করা যায়।



77. CRAWLER OPTIMIZATION
============================================================

Optimization:

1. Session ব্যবহার
2. Connection reuse
3. URL deduplication
4. Domain filtering
5. Depth limiting
6. Rate limiting
7. Concurrent requests
8. Async I/O
9. Efficient parser
10. Database indexing
11. Retry
12. Logging



78. DATA STORAGE
============================================================

Small Project:

JSON
CSV


Medium Project:

SQLite


Large Project:

PostgreSQL
MongoDB



79. DYNAMIC WEBSITE
============================================================

Static Website:

Requests
   ↓
HTML
   ↓
BeautifulSoup
   ↓
Data


Dynamic Website:

Requests
   ↓
HTML
   ↓
JavaScript
   ↓
API
   ↓
Data


এই ক্ষেত্রে:

Selenium
Playwright

ব্যবহার করা যায়।



80. CRAWLER বনাম SPIDER
============================================================

Crawler:

General concept

Find URLs
Visit URLs
Follow Links


Spider:

Scrapy-এর context-এ crawler logic implement করা
একটি component/class।



81. CRAWLER বনাম SCRAPER
============================================================

Crawler:

URL Discovery
Page Navigation


Scraper:

Data Extraction
Data Cleaning
Data Storage



82. WEB CRAWLING ROADMAP
============================================================

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
Async
    ↓
STEP 15
Selenium / Playwright
    ↓
STEP 16
Scrapy
    ↓
STEP 17
Production Crawler



83. PRACTICE PROJECTS
============================================================

Project 1:
Link Extractor

Input:
Website URL

Output:
All Links


Project 2:
Website Crawler

Input:
Start URL

Output:
Visited URLs


Project 3:
Website Structure Mapper

URL
 ↓
Links
 ↓
Tree Structure


Project 4:
News Scraper

Title
Author
Date
URL


Project 5:
Product Scraper

Product
Price
Rating
URL


Project 6:
Job Scraper

Job Title
Company
Location
URL


Project 7:
Multi-threaded Crawler

Queue
+
Threads
+
Visited


Project 8:
Scrapy Project

Spider
Pipeline
Middleware
Database



84. REQUIRED PACKAGES
============================================================

Basic:

pip install requests beautifulsoup4


Pandas:

pip install pandas


Selenium:

pip install selenium


Playwright:

pip install playwright

playwright install


Scrapy:

pip install scrapy


Optional:

pip install lxml

pip install aiohttp

pip install httpx



85. SHORT REVISION
============================================================

Web Crawling
→ Discover and visit pages.


Web Scraping
→ Extract information from pages.


Requests
→ Send HTTP requests.


BeautifulSoup
→ Parse HTML.


urljoin()
→ Relative URL → Absolute URL.


urlparse()
→ Analyze URL.


Set
→ Avoid duplicate URLs.


Queue / deque
→ Manage URLs.


Depth
→ Control crawling levels.


Domain Restriction
→ Stay inside target website.


Session
→ Reuse HTTP connections/session state.


Timeout
→ Prevent indefinite waiting.


Retry
→ Handle temporary failures.


Rate Limiting
→ Control request frequency.


Robots.txt
→ Check crawler access rules.


Selenium / Playwright
→ Browser automation.


Scrapy
→ Large-scale crawling/scraping framework.



86. FINAL MENTAL MODEL
============================================================

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



87. FINAL FORMULA
============================================================

Crawler

= URL Discovery
+ Queue
+ Visited
+ HTTP Request
+ Link Following


Scraper

= HTTP Request
+ HTML Parsing
+ Data Extraction
+ Data Cleaning
+ Data Storage


Complete Web Scraping System

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


============================================================
                    END OF NOTES
============================================================
"""
# Automated Dealer & Distributor Web Scraper

A Python-based web scraping automation that collects dealer and distributor information from manufacturer locator websites using Selenium.

The scraper automatically navigates through states and counties, extracts dealer information, removes duplicate records, and exports clean datasets to Excel and CSV formats.

---

## Features

- Automated website navigation
- Dynamic dropdown handling
- State and county iteration
- Dealer and distributor information extraction
- Contact information collection
- Email extraction
- Phone number extraction
- Website extraction
- Duplicate removal
- Excel export (.xlsx)
- CSV export (.csv)
- Headless browser execution
- Progress tracking with tqdm
- Exception handling

---

## Technologies

- Python 3
- Selenium
- Pandas
- OpenPyXL
- Fake UserAgent
- tqdm

---

## Data Collected

The scraper collects:

- Company Name
- Dealer Name
- Address
- Contact Person
- Phone Number
- Toll-Free Number (if available)
- Email Address
- Website
- Dealer Category

---

## Project Structure

```
project/
│
├── distributors_1_scrapping.py
├── distributors_2_scrapping.py
├── distributors_1.xlsx
├── distributors_1.csv
├── distributors_2.xlsx
├── distributors_2.csv
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone [https://github.com/yourusername/dealer-web-scraper.git](https://github.com/EmirSalkin/WebScrapping_2.git)
```

Install dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install selenium pandas openpyxl fake-useragent tqdm
```

---

## Usage

Run one of the scraper scripts.

```bash
python distributors_1_scrapping.py
```

or

```bash
python distributors_2_scrapping.py
```

The scraper will:

1. Open the target website
2. Iterate through all available states
3. Iterate through counties
4. Extract dealer information
5. Remove duplicate records
6. Export results to Excel and CSV

---

## Output

Generated files:

```
distributors_1.xlsx
distributors_1.csv

distributors_2.xlsx
distributors_2.csv
```

---

## Workflow

```
Start
   │
   ▼
Open Website
   │
   ▼
Select State
   │
   ▼
Select County
   │
   ▼
Extract Dealer Information
   │
   ▼
Clean Data
   │
   ▼
Remove Duplicates
   │
   ▼
Export Excel & CSV
   │
   ▼
Finish
```

---

## Example Output

| Name | Address | Phone | Email | Website |
|------|---------|-------|-------|---------|
| ABC Company | Dallas, TX | +1 xxx xxx xxxx | info@example.com | www.example.com |

---

## Disclaimer

This project was created for educational and automation purposes. Always review and comply with the target website's Terms of Service and robots.txt before collecting data.

---

## Author

**Emir Salkin**

Python Backend Developer | Web Scraping | Automation | AI Engineer

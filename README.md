<div align="center">

# 🚀 Automated Dealer & Distributor Web Scraper

### Python • Selenium • Web Scraping • Data Extraction • Automation

A powerful Python automation tool that extracts dealer and distributor information from manufacturer locator websites and exports clean datasets to Excel & CSV.

---

<p align="center">

<img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/Selenium-Automation-43B02A?style=for-the-badge&logo=selenium&logoColor=white">
<img src="https://img.shields.io/badge/Pandas-Data_Processing-150458?style=for-the-badge&logo=pandas">
<img src="https://img.shields.io/badge/OpenPyXL-Excel-success?style=for-the-badge">
<img src="https://img.shields.io/badge/Web_Scraping-Python-blue?style=for-the-badge">

</p>

</div>

---

# 📖 Overview

This project automates the collection of dealer and distributor information from manufacturer locator websites.

Instead of manually searching through hundreds of states and counties, the scraper automatically navigates every available location, extracts business information, removes duplicate records, and exports structured datasets.

The scraper is designed to be reliable, scalable, and suitable for large-scale data collection tasks.

---

# ✨ Features

- 🌎 Automatic state navigation
- 📍 Automatic county selection
- 🏢 Dealer & distributor extraction
- 📞 Phone number collection
- 📧 Email extraction
- 🌐 Website extraction
- 📍 Address extraction
- ⚡ Headless browser automation
- 🔄 Dynamic page handling
- 🧹 Duplicate removal
- 📊 Excel export
- 📄 CSV export
- ⏳ Progress bars with tqdm
- 🛡 Robust exception handling

---

# ⚙️ Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Core programming language |
| Selenium | Browser automation |
| Pandas | Data processing |
| OpenPyXL | Excel export |
| Fake UserAgent | Random browser fingerprint |
| tqdm | Progress visualization |

---

# 📂 Project Structure

```text
Dealer-Web-Scraper/
│
├── distributors_1_scrapping.py
├── distributors_2_scrapping.py
│
├── distributors_1.xlsx
├── distributors_2.xlsx
│
├── distributors_1.csv
├── distributors_2.csv
│
├── requirements.txt
│
└── README.md
```

---

# 🔄 Workflow

```text
                    Start
                      │
                      ▼
          Open Manufacturer Website
                      │
                      ▼
            Select Available State
                      │
                      ▼
            Select Available County
                      │
                      ▼
         Extract Dealer Information
                      │
                      ▼
            Clean & Validate Data
                      │
                      ▼
            Remove Duplicate Records
                      │
                      ▼
             Export Excel & CSV
                      │
                      ▼
                     Finish
```

---

# 📊 Extracted Information

The scraper collects:

- Company Name
- Dealer Name
- Address
- Contact Person
- Phone Number
- Toll-Free Number
- Email Address
- Website
- Dealer Category

---

# 📈 Sample Output

| Company | Address | Phone | Email | Website |
|----------|---------|-------|--------|----------|
| ABC Dealer | Dallas, TX | +1 xxx xxx xxxx | info@company.com | www.company.com |
| XYZ Dealer | Houston, TX | +1 xxx xxx xxxx | sales@company.com | www.company.com |

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/dealer-web-scraper.git
```

Move into the project directory

```bash
cd dealer-web-scraper
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

# ▶️ Usage

Run either scraper.

```bash
python distributors_1_scrapping.py
```

or

```bash
python distributors_2_scrapping.py
```

---

# 📁 Output Files

After execution, the scraper generates:

```text
✔ distributors_1.xlsx
✔ distributors_1.csv

✔ distributors_2.xlsx
✔ distributors_2.csv
```

---

# 💡 Why This Project?

This project demonstrates practical experience with:

- Web Scraping
- Browser Automation
- Dynamic Websites
- Data Cleaning
- Data Extraction
- Python Automation
- Large-scale Data Collection
- Excel Report Generation


# 📌 Future Improvements

- Docker support
- Proxy rotation
- Multi-threading
- CLI arguments
- Database export (PostgreSQL / MySQL)
- Logging system
- Automatic retries
- Cloud deployment

---

# ⚠️ Disclaimer

This project is intended for educational and automation purposes only.

Please ensure that you comply with the target website's Terms of Service and robots.txt before scraping data.

---

<div align="center">

## 👨‍💻 Author

### **Emir Salkin**

**Backend Developer • AI Engineer • Web Scraping Specialist**

⭐ If you found this project useful, consider giving it a star!

</div>

# 🧹 data_cleaning_script_v1.2.0

This repository contains the **first iteration of a data scraping and cleaning script** for collecting structured data from the [Charities Portal (charities.gov.sg)](https://www.charities.gov.sg) — Singapore’s public registry of charities and fundraising events.

## 📌 Purpose

The goal of this project is to automate the extraction of **charity and fundraising-related data** to support **outreach efforts**, research, and transparency. This data will be used to better understand the landscape of registered charities in Singapore.

## 🕸️ What It Does

- Uses **Scrapy** and **Playwright** to scrape JavaScript-rendered pages from the Charities Portal.
- Targets data such as:
  - Charity names and registration details
  - Fundraising campaign information
  - Sector and classification of charities

## 🔧 Tech Stack

- [Scrapy](https://scrapy.org/) – for building the scraping logic.
- [Scrapy-Playwright](https://github.com/scrapy-plugins/scrapy-playwright) – for scraping pages that require JavaScript rendering.
- [GitHub Codespaces](https://github.com/features/codespaces) – for a portable dev environment.
- Python 3.11

## 🚀 Getting Started

This project uses a **pre-configured dev container**, so setup is fast and reproducible in GitHub Codespaces.

### 1. Open in Codespaces

Click the **“Code” → “Codespaces” → “Create codespace”** button on this repo.

### 2. Run the Spider

```bash
cd myproject
scrapy crawl example
```

The spider will visit JavaScript-enabled pages and extract charity quotes as a sample.

## 📂 Folder Structure

```
.
├── .devcontainer/         # GitHub Codespaces setup
│   ├── devcontainer.json
│   └── Dockerfile
├── myproject/             # Scrapy project folder
│   ├── myproject/
│   └── scrapy.cfg
└── README.md              # You're here!
```

## 📈 Roadmap

- [ ] Replace sample spider with one tailored to charities.gov.sg
- [ ] Implement data cleaning pipeline
- [ ] Store structured output in CSV/JSON format
- [ ] Add data validation checks
- [ ] Explore scheduling with cron or GitHub Actions

## 🤝 Contributing

This is an early-stage project. Contributions and suggestions are welcome!

---

*This project is for educational, research, and outreach purposes only. Please use responsibly and respect [charities.gov.sg](https://www.charities.gov.sg)’s terms of use.*

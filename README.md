# GitHub Profile Scraper

This project extracts basic information from a GitHub profile using Python Playwright and stores the data in a Supabase database.

## Profile Scraped

https://github.com/shantanujain18

## Extracted Data

* Username
* Name
* Bio
* Followers count
* Following count
* Number of repositories

## Technologies Used

* Python
* Playwright
* Supabase

## How to Run

1. Install dependencies

pip install playwright supabase

2. Install Playwright browsers

python -m playwright install

3. Run the scraper

python scraper.py

## Assumptions

* The GitHub profile page structure remains consistent.

## Improvements with More Time

* Add error handling
* Support scraping multiple GitHub profiles
* Add logging and monitoring

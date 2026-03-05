# GitHub Profile Scraper using Playwright & Supabase

This is a small automation project where I built a Python script that extracts basic information from a GitHub profile and stores the data in a Supabase database.

The goal of this project was to practice **browser automation, web scraping, and database integration** using modern tools.

---

## 🚀 Project Overview

The script automatically opens a GitHub profile using Playwright, extracts key profile details, and saves them into a Supabase database.

Profile used for scraping:

https://github.com/shantanujain18

---

## 📌 Extracted Information

The script collects the following information from the profile page:

* Username
* Name (if available)
* Bio
* Followers count
* Following count
* Number of repositories

If any field (like name or bio) is not available, the script safely handles it without breaking.

---

## 🛠 Technologies Used

* **Python**
* **Playwright** – for browser automation and scraping
* **Supabase** – for storing the scraped data in a PostgreSQL database

---

## ⚙️ How to Run the Project

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/github-profile-scraper.git
cd github-profile-scraper
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Install Playwright browsers

```bash
python -m playwright install
```

### 4️⃣ Run the script

```bash
python scraper.py
```

The script will scrape the GitHub profile and store the data in the Supabase table.

---

## 📊 Example Output

```text
Scraped Data:
{
 'username': 'Shantanujain18',
 'name': 'Not Available',
 'bio': 'Learning to build full-stack websites using Django',
 'followers': 2,
 'following': 3,
 'repositories': 25
}
```

The data is then saved into the Supabase database.

---

## 🧠 What I Learned

While building this project, I learned:

* How to automate browsers using Playwright
* How to scrape structured data from web pages
* How to integrate Python applications with Supabase
* Handling missing data safely during scraping

---

## 🔮 Future Improvements

If I extend this project further, I would:

* Add support for scraping multiple GitHub profiles
* Add error handling and logging
* Create a small dashboard to visualize the collected data
* Schedule the scraper to run automatically

---

## 📌 Note

This project does **not use the GitHub API**.
All information is collected by automating a browser and scraping the profile page.

---

## 👨‍💻 Author

**Manthan Surkar**

MCA Student | Aspiring Software Engineer
Interested in Web Development, Automation, and Backend Development.

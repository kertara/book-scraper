# 📚 Book Scraper

This project is a beginner-friendly web scraper built with Python and BeautifulSoup. It extracts book information from [books.toscrape.com](https://books.toscrape.com), a website made for practicing web scraping.

## 🧠 Purpose

This project was created as part of my self-learning journey to improve my web scraping skills. The goals are:
- To understand and navigate HTML structure
- To locate and extract data using tags and class attributes
- To structure the scraper with clean, reusable functions
- To practice using GitHub for version control and project sharing

## ⚙️ Features

- Retrieves the title, price, and star rating of each book
- Organized using modular Python functions
- Handles missing or malformed data gracefully

## 🚀 How to Run

1. **Install dependencies**:

pip install beautifulsoup4 requests lxml

2. **Run the scraper**:

python scraper.py

📄 **OUTPUT**:
For each book on the page, the scraper prints:

Title

Price

Star rating (1 to 5)

Example output:

A Light in the Attic - £51.77 - Three/Five
Tipping the Velvet - £53.74 - Four/Five

🛠 **Tech Stack**
Python 3

BeautifulSoup4

requests

lxml

🔭 **Future Improvements**
Add pagination support to scrape all pages

Export data to CSV or JSON

Scrape additional fields like image URLs and book detail links

Build a user interface for easier interaction

📌 **Notes**
This is an educational project and does not violate any terms of service. The target website is designed for learning purposes.

🤝 **Contributions**
If you have suggestions or want to contribute improvements, feel free to open an issue or pull request. Feedback is welcome!